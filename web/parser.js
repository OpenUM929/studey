// parser.js — 마크다운 문제지를 브라우저에서 직접 파싱.
// tools/md2quiz.py 와 동일 로직. output/*.md 를 굳이 변환 안 거치고
// 웹에서 드래그앤드롭/파일선택으로 바로 불러오기 위함.
(function () {
  "use strict";

  var OPTION_RE = /^\s*([①②③④⑤])\s*(.*)$/m;
  var PROB_RE = /^\s*\*\*(\d+)\.\*\*\s*(.*)$/m;
  var TAG_RE = /\[([A-Za-z0-9\-]+)·?(T\d)\s*\]/;
  var H1_RE = /^\s*#\s+(.*)$/m;
  var ANSWER_H_RE = /^\s*#\s*정답/m;

  var SUBJECT_MAP = [
    [/통합과학|과학/, "science"],
    [/영어/, "english"],
    [/수학/, "math"],
    [/국어/, "korean"]
  ];

  function detectSubject(text) {
    for (var i = 0; i < SUBJECT_MAP.length; i++) {
      if (SUBJECT_MAP[i][0].test(text)) return SUBJECT_MAP[i][1];
    }
    return "unknown";
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
        var tm = TAG_RE.exec(typeTier);
        answers[num] = {
          answer: cells[1] || "",
          typeId: tm ? tm[1] : "",
          tier: tm ? tm[2] : "",
          explanation: cells[3] || ""
        };
      } else if (inTable && s) {
        break;
      }
    }
    return answers;
  }

  function splitSections(rawLines) {
    var sections = { select: [], essay: [], answer: [] };
    var cur = null;
    for (var i = 0; i < rawLines.length; i++) {
      var ln = rawLines[i];
      var s = ln.trim();
      if (s.indexOf("## 선택형") === 0) { cur = "select"; continue; }
      if (s.indexOf("## 서답형") === 0 || s.indexOf("## 서술형") === 0 || s.indexOf("## 단답형") === 0) { cur = "essay"; continue; }
      if (ANSWER_H_RE.test(ln)) { cur = "answer"; continue; }
      if (/^\s*#{1,2}\s/m.test(ln) && cur !== null && cur !== "answer") {
        if (cur === "select" || cur === "essay") cur = null;
        continue;
      }
      if (cur !== null) sections[cur].push(ln);
    }
    return sections;
  }

  function convertText(text, sourceKey) {
    var rawLines = text.split("\n");
    var title = "";
    for (var i = 0; i < rawLines.length; i++) {
      var m = H1_RE.exec(rawLines[i]);
      if (m) { title = m[1].trim(); break; }
    }
    var subject = detectSubject(title + " " + (sourceKey || ""));
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
      if (!ans.typeId) {
        var tm = TAG_RE.exec(stem);
        if (tm) { ans.typeId = tm[1]; ans.tier = tm[2]; }
      }
      problems.push({
        id: sourceKey + "#" + blk.number,
        sourceKey: sourceKey,
        subject: subject,
        number: blk.number,
        qtype: qtype,
        stem: stem.replace(/\s*\[[^\]]*\]\s*$/, "").trim(),
        passage: po.passage,
        options: po.options,
        answer: ans.answer || "",
        typeId: ans.typeId || "",
        tier: ans.tier || "",
        explanation: ans.explanation || ""
      });
    }
    return { title: title, subject: subject, problems: problems };
  }

  // 여러 md 텍스트 -> window.QUIZ_DATA 구조
  function parseAll(files) {
    // files: [{ name, text }]
    var sources = [], problems = [];
    for (var i = 0; i < files.length; i++) {
      var key = files[i].name.replace(/\.[^.]+$/, "") || ("doc" + (i + 1));
      var info = convertText(files[i].text, key);
      sources.push({ file: files[i].name, title: info.title, subject: info.subject, count: info.problems.length });
      problems = problems.concat(info.problems);
    }
    return { generatedAt: new Date().toISOString(), sources: sources, problems: problems };
  }

  window.QuizParser = { convertText: convertText, parseAll: parseAll };
})();
