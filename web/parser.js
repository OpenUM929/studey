// parser.js — 마크다운 문제지를 브라우저에서 직접 파싱.
// tools/md2quiz.py 와 동일 로직. output/*.md 를 굳이 변환 안 거치고
// 웹에서 드래그앤드롭/파일선택으로 바로 불러오기 위함.
(function () {
  "use strict";

  var OPTION_RE = /^\s*([①②③④⑤])\s*(.*)$/m;
  var PROB_RE = /^\s*\*\*(\d+)\.\*\*\s*(.*)$/m;
  // Ruling 260825_07 CB1(amended): body tags carry FOUR slots —
  // [ID · Tier · DFlist · Ecode] (+aux). Unknown tail tokens are preserved
  // (tagExtra), never dropped — principle 3.
  var BODY_TAG_RE = /\[\s*([A-Za-z0-9]+(?:-\d+)?)\s*·\s*(T\d)((?:\s*·\s*[^\]·]+)*)\s*\]/;
  // Bracketless answer-table cell: `SM2-13·T4 (보조 SM2-11)`
  var CELL_TAG_RE = /^\s*([A-Za-z0-9]+(?:-\d+)?)\s*·\s*(T\d)(?:\s*\(보조\s*([A-Za-z0-9\-]+)\))?/;
  var H1_RE = /^\s*#\s+(.*)$/m;

  // DATA_STANDARD §5.8 — 7 subject codes (ruling 07 CB1 / ruling 12 CB2)
  var SUBJECT_MAP = [
    [/통합과학|과학/, "science"],
    [/통합사회|사회/, "social"],
    [/한국사/, "history"],
    [/영어/, "english"],
    [/도형의\s*방정식|공통수학2/, "math2"],
    [/수학/, "math1"],
    [/국어/, "korean"]
  ];

  function detectSubject(text) {
    for (var i = 0; i < SUBJECT_MAP.length; i++) {
      if (SUBJECT_MAP[i][0].test(text)) return SUBJECT_MAP[i][1];
    }
    return "unknown";
  }

  function parseFrontmatter(rawLines) {
    if (!rawLines.length || rawLines[0].trim() !== "---") return null;
    var meta = {};
    for (var i = 1; i < rawLines.length; i++) {
      if (rawLines[i].trim() === "---") return meta;
      var m = /^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$/.exec(rawLines[i]);
      if (m) meta[m[1]] = m[2].split(/\s+#/, 1)[0].trim();
    }
    return null;
  }

  function classifyTail(g3) {
    var out = { df: [], traps: [], aux: [], extra: [] };
    if (!g3) return out;
    g3.split("·").forEach(function (t) {
      t = t.trim();
      if (!t) return;
      var pa = /\(\s*(\+[A-Za-z0-9\-]+)\s*\)/.exec(t);
      if (pa) { out.aux.push(pa[1].slice(1)); t = t.replace(pa[0], "").trim(); if (!t) return; }
      if (/^DF\d+$/.test(t)) out.df.push(t);
      else if (/^E\d+$/.test(t)) out.traps.push(t);
      else if (/^\+[A-Za-z0-9\-]+$/.test(t)) out.aux.push(t.slice(1));
      else out.extra.push(t);
    });
    return out;
  }

  var SPLIT_OPTION_RE = /\s*([①②③④⑤])\s*/;
  var LEADING_OPTION_RE = /^\s*([①②③④⑤])\s*(.*)$/;

  function splitLineOptions(line) {
    // 줄이 원숫자로 '시작'할 때만 선지로 간주(지문 중간 numbering 은 회피).
    // 한 줄에 ①…②…③… 가 몰려 있어도 circle-number 경계로 쪼갠다.
    var lead = LEADING_OPTION_RE.exec(line);
    if (!lead) return [];
    var parts = line.split(SPLIT_OPTION_RE);
    // split 결과: ["", "①", "text", "②", "text", ...]
    var opts = [];
    for (var i = 1; i + 1 < parts.length; i += 2) {
      var num = parts[i];
      var body = (parts[i + 1] || "").trim();
      if (body) opts.push(num + " " + body);
    }
    return opts;
  }

  function parseOptionsAndPassage(lines) {
    var passage = [], options = [], inOption = false;
    for (var i = 0; i < lines.length; i++) {
      var opts = splitLineOptions(lines[i]);
      if (opts.length) {
        inOption = true;
        for (var k = 0; k < opts.length; k++) options.push(opts[k]);
      } else if (inOption) {
        continue;
      } else if (lines[i].trim()) {
        passage.push(lines[i].trim());
      }
    }
    return { passage: passage.join("\n").trim(), options: options };
  }

  function splitProblems(sectionLines) {
    var blocks = [], cur = null;
    for (var i = 0; i < sectionLines.length; i++) {
      var ln = sectionLines[i];
      var m = PROB_RE.exec(ln);
      if (m) {
        if (cur) blocks.push(cur);
        cur = { number: parseInt(m[1], 10), stem: m[2].trim(), body: [] };
      } else if (cur) {
        if (/^\s*#{1,2}\s/m.test(ln)) { blocks.push(cur); cur = null; }
        else cur.body.push(ln);
      }
    }
    if (cur) blocks.push(cur);
    return blocks;
  }

  function parseAnswerTable(lines) {
    var answers = {}, inTable = false;
    for (var i = 0; i < lines.length; i++) {
      var s = lines[i].trim();
      if (s.indexOf("|") === 0) {
        inTable = true;
        var cells = s.replace(/^\|/, "").replace(/\|$/, "").split("|").map(function (c) { return c.trim(); });
        if (!cells.length) continue;
        if (cells[0] === "문항" || cells[0] === "" || /^[-: ]+$/.test(cells[0])) continue;
        var numM = /^\s*(\d+)/.exec(cells[0]);
        if (!numM) continue;
        var num = parseInt(numM[1], 10);
        var typeTier = cells[2] || "";
        var tm = CELL_TAG_RE.exec(typeTier);
        answers[num] = {
          answer: cells[1] || "",
          typeId: tm ? tm[1] : "",
          tier: tm ? tm[2] : "",
          auxTypes: (tm && tm[3]) ? [tm[3]] : [],
          df: [],
          traps: [],
          explanation: cells[3] || ""
        };
      } else if (inTable && s) {
        break;
      }
    }
    return answers;
  }

  function splitSections(rawLines) {
    // Ruling 260825_07 CB2 (F9): section state is driven by TYPE keywords at any
    // heading level. Unit sub-headers (`## I-2 직선의 방정식 …`) must NOT reset
    // the question zone — they are kept as content so splitProblems can flush
    // the previous block. Trailing auxiliary sections (채점 기준/요약/검증) never
    // change state either.
    var sections = { select: [], essay: [], answer: [] };
    var cur = null;
    for (var i = 0; i < rawLines.length; i++) {
      var ln = rawLines[i];
      var s = ln.trim();
      if (/^\s*#{1,4}\s+/.test(s)) {
        if (/채점|기준|요약|검증/.test(s)) continue;
        if (/선택형/.test(s)) { cur = "select"; continue; }
        if (/서답형|서술형|단답형/.test(s)) { cur = "essay"; continue; }
        if (/정답|해설/.test(s)) { cur = "answer"; continue; }
        if (cur !== null) sections[cur].push(ln);
        continue;
      }
      if (cur !== null) sections[cur].push(ln);
    }
    return sections;
  }

  function convertText(text, sourceKey) {
    // CRLF 정규화 — 파이썬 splitlines() 동작과 일치시킨다. \r가 남으면 m 플래그 없는
    // 행 단위 정규식(프론트매터 40행·LEADING_OPTION_RE 63행)의 (.*)$ 가 전부 실패한다.
    var rawLines = text.split(/\r?\n/);
    var fm = parseFrontmatter(rawLines);
    var title = "";
    for (var i = 0; i < rawLines.length; i++) {
      var m = H1_RE.exec(rawLines[i]);
      if (m) { title = m[1].trim(); break; }
    }
    // frontmatter subject_code has priority (ruling 07 CB1)
    var subject = (fm && fm.subject_code) ? fm.subject_code : detectSubject(title + " " + (sourceKey || ""));
    var scopeConfirmed = !!(fm && fm.scope_confirmed === "true");
    var setId = (fm && fm.set_id) ? fm.set_id : sourceKey;
    var sections = splitSections(rawLines);
    var selBlocks = splitProblems(sections.select);
    var essBlocks = splitProblems(sections.essay);
    var answers = parseAnswerTable(sections.answer);
    var problems = [];
    var all = selBlocks.concat(essBlocks);
    all.sort(function (a, b) { return a.number - b.number; });
    for (var j = 0; j < all.length; j++) {
      var blk = all[j];
      var po = parseOptionsAndPassage(blk.body);
      var qtype = po.options.length ? "choice" : "essay";
      var ans = answers[blk.number] || {};
      var stem = blk.stem;
      // slot source: stem first, then passage/body (tags may sit in the stimulus)
      var tm2 = BODY_TAG_RE.exec(stem);
      if (!tm2) tm2 = BODY_TAG_RE.exec(blk.body.join("\n"));
      var tail = classifyTail(tm2 ? tm2[3] : "");
      if (!ans.typeId && tm2) {
        ans.typeId = tm2[1]; ans.tier = tm2[2];
        if (!ans.auxTypes || !ans.auxTypes.length) ans.auxTypes = tail.aux;
      }
      // merge slots regardless of where typeId came from (table or tag)
      ans.df = (tail.df || []).concat(ans.df || []);
      ans.traps = (tail.traps || []).concat(ans.traps || []);
      problems.push({
        id: setId + "#" + blk.number,
        sourceKey: sourceKey,
        setId: setId,
        scopeConfirmed: scopeConfirmed,
        subject: subject,
        number: blk.number,
        qtype: qtype,
        stem: stem.replace(/\s*\[[^\]]*\]\s*$/, "").trim(),
        passage: po.passage,
        options: po.options,
        answer: ans.answer || "",
        typeId: ans.typeId || "",
        tier: ans.tier || "",
        df: ans.df || [],
        traps: ans.traps || [],
        auxTypes: ans.auxTypes || [],
        tagExtra: tail.extra || [],
        explanation: ans.explanation || ""
      });
    }
    return { title: title, subject: subject, problems: problems,
             meta: { scopeConfirmed: scopeConfirmed, setId: setId,
                     unit: (fm && fm.unit) || "", intendedUse: (fm && fm.intended_use) || "" } };
  }

  // 여러 md 텍스트 -> window.QUIZ_DATA 구조
  function parseAll(files) {
    // files: [{ name, text }]
    var sources = [], problems = [];
    for (var i = 0; i < files.length; i++) {
      var key = files[i].name.replace(/\.[^.]+$/, "") || ("doc" + (i + 1));
      var info = convertText(files[i].text, key);
      sources.push({ file: files[i].name, title: info.title, subject: info.subject,
                     count: info.problems.length,
                     scopeConfirmed: info.meta.scopeConfirmed,
                     setId: info.meta.setId });
      problems = problems.concat(info.problems);
    }
    return { generatedAt: new Date().toISOString(), sources: sources, problems: problems };
  }

  window.QuizParser = { convertText: convertText, parseAll: parseAll };
})();
