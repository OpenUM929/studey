"""Unapplied Q1 candidate. Inputs/eligibility are supplied by a separate authority.
Does not infer eligibility from measurement output. Does not edit any source.
"""
from collections import Counter
from fractions import Fraction
import hashlib
from pathlib import Path
import re


def compare_ids(expected, observed):
    return dict(expected=sorted(expected), observed=sorted(observed),
                duplicates=sorted(k for k, n in Counter(observed).items() if n > 1),
                expected_duplicates=sorted(k for k, n in Counter(expected).items() if n > 1),
                missing=sorted(set(expected)-set(observed)),
                extra=sorted(set(observed)-set(expected)))


def require_equal(expected, observed):
    report=compare_ids(expected, observed)
    if any(report[k] for k in ('duplicates','expected_duplicates','missing','extra')):
        raise ValueError(report)
    return report


def frozen_source(root, snapshot):
    """Snapshot schema: uid -> {transcript.md/meta.yml: {bytes, sha256}}."""
    root=Path(root)
    report=require_equal(list(snapshot), [p.name for p in root.glob('EX-*') if p.is_dir()])
    strata={}
    for uid, files in snapshot.items():
        if not re.fullmatch(r'EX-[a-z0-9]+-\d{4}[12][FM]',uid):
            raise ValueError('invalid unit identifier')
        if set(files) != {'transcript.md','meta.yml'}:
            raise ValueError('incomplete file schema')
        for name, expected in files.items():
            b=(root/uid/name).read_bytes()
            if len(b)!=expected['bytes'] or hashlib.sha256(b).hexdigest()!=expected['sha256']:
                raise ValueError('source drift: '+uid+'/'+name)
        meta=(root/uid/'meta.yml').read_text(encoding='utf-8')
        codes=re.findall(r'^exam_code:\s*["\']?(\d{4})-([12])([FM])["\']?\s*(?:#.*)?$',meta,re.M)
        if len(codes)!=1:
            raise ValueError('missing/duplicate exam_code: '+uid)
        year,semester,exam=codes[0]
        if uid.rsplit('-',1)[1]!=year+semester+exam:
            raise ValueError('metadata/id disagreement: '+uid)
        strata[uid]=exam+'-'+year
    return strata,report


def expected_strata(source_strata, dispositions):
    """Every unit needs an independently supplied explicit statistical disposition.
    partial/unresolved prevent official derivation; no quiet exclusions.
    """
    require_equal(list(source_strata),list(dispositions))
    if not all(s in ('eligible','not-applicable','partial','unresolved') for s in dispositions.values()):
        raise ValueError('unknown disposition')
    if any(s in ('partial','unresolved') for s in dispositions.values()):
        raise ValueError('official population unresolved')
    result=sorted({source_strata[u] for u,s in dispositions.items() if s=='eligible'})
    if not result:
        raise ValueError('empty eligible population')
    return result


def validate_aggregate(expected, rows, total, tier_rows, outside):
    """Rows=(stratum,n,fit); total=(n,fit,residual); exact integer counts only."""
    report=require_equal(expected,[r[0] for r in rows])
    require_equal(['T1','T2','T3','T4'],[r[0] for r in tier_rows])
    counts=[v for r in rows for v in r[1:]]+list(total)+[v for _,v in tier_rows]+[outside]
    if any(type(v) is not int or v<0 for v in counts):
        raise ValueError('invalid count')
    n,fit,residual=total
    if n==0 or fit==0 or any(f>n for _,n,f in rows) or fit>n:
        raise ValueError('invalid denominator or fit')
    if sum(r[1] for r in rows)!=n or sum(r[2] for r in rows)!=fit or residual!=n-fit:
        raise ValueError('aggregate mismatch')
    if sum(v for _,v in tier_rows)!=fit or outside!=residual:
        raise ValueError('tier/outside mismatch')
    # Derive yearly rollups from already matched source strata, never fixed years.
    years={}
    for label,n,f in rows:
        year=label.split('-')[1]
        a,b=years.get(year,(0,0)); years[year]=(a+n,b+f)
    if sum(a for a,b in years.values())!=total[0] or sum(b for a,b in years.values())!=total[1]:
        raise ValueError('year mismatch')
    return dict(coverage=report,years=years,fit_fraction=str(Fraction(total[1],total[0])))