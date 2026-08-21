(function () {
  "use strict";
  var DATA = window.QUIZ_DATA || { problems: [] };
  var LS = {
    status: "quiz_status_v1",
    choice: "quiz_choice_v1",
    revealed: "quiz_revealed_v1",
    md: "quiz_md_v1",
    answer: "quiz_answer_v1"
  };
  var SUBJECT_LABEL = {
    english: "영어", science: "통합과학", math: "수학",
    korean: "국어", unknown: "기타"
  };
  function load(k) { try { return JSON.parse(localStorage.getItem(k)) || {}; } catch (e) { return {}; } }
  function save(k, v) { localStorage.setItem(k, JSON.stringify(v)); }
  var status = load(LS.status);
  var choice = load(LS.choice);
  var revealed = load(LS.revealed);
  var answers = load(LS.answer);

  var state = { list: [], idx: 0, shuffle: false, wrongOnly: false,
                subject: "all", type: "all" };

  // ---- DOM ----
  var $ = function (id) { return document.getElementById(id); };
  var el = {
    title: $("title"), subjectFilter: $("subjectFilter"), typeFilter: $("typeFilter"),
    loadBtn: $("loadBtn"), exportBtn: $("exportBtn"),
    shuffleBtn: $("shuffleBtn"), wrongBtn: $("wrongBtn"), resetBtn: $("resetBtn"),
    progress: $("progress"), progressFill: $("progressFill"),
    qNumber: $("qNumber"), qType: $("qType"), qTier: $("qTier"), qSource: $("qSource"),
    stem: $("stem"), passage: $("passage"), options: $("options"),
    essayBox: $("essayBox"), userAnswer: $("userAnswer"), revealBtn: $("revealBtn"),
    answerPanel: $("answerPanel"), answerText: $("answerText"),
    diffBox: $("diffBox"), autoStatus: $("autoStatus"), explanation: $("explanation"),
    markRow: $("markRow"), correctBtn: $("correctBtn"), wrongMarkBtn: $("wrongMarkBtn"),
    prevBtn: $("prevBtn"), nextBtn: $("nextBtn"), card: $("card"),
    fileInput: $("fileInput"), dropHint: $("dropHint"), dropLoadBtn: $("dropLoadBtn")
  };

  // ---- helpers ----
  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function md(s) {
    return esc(s).replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  }
  function correctNum(answer) {
    var m = /^([①②③④⑤])/.exec(answer || "");
    return m ? m[1] : null;
  }
  function shuffleArr(a) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  // ---- diff (서답형: 모범답안 기준, 구두점/공백/대소문자 무시) ----
  var WORD_RE = /[A-Za-z0-9가-힣]+/g;
  function wordsOf(text) {
    var m, out = [], re = new RegExp(WORD_RE);
    while ((m = re.exec(text)) !== null) out.push(m[0]);
    return out;
  }
  function lcsMatch(a, b) {
    var n = a.length, m = b.length, i, j;
    if (!n || !m) return new Array(n).fill(false);
    var dp = [];
    for (i = 0; i <= n; i++) dp[i] = new Array(m + 1).fill(0);
    for (i = 1; i <= n; i++) {
      for (j = 1; j <= m; j++) {
        dp[i][j] = (a[i - 1] === b[j - 1]) ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
    var matched = new Array(n).fill(false);
    i = n; j = m;
    while (i > 0 && j > 0) {
      if (a[i - 1] === b[j - 1]) { matched[i - 1] = true; i--; j--; }
      else if (dp[i - 1][j] >= dp[i][j - 1]) i--;
      else j--;
    }
    return matched;
  }
  function renderDiff(userText, modelText) {
    userText = (userText || "").trim();
    if (!userText) return md(modelText);
    var uWords = wordsOf(userText).map(function (w) { return w.toLowerCase(); });
    var mWords = wordsOf(modelText);
    var mNorm = mWords.map(function (w) { return w.toLowerCase(); });
    var matched = lcsMatch(mNorm, uWords);
    var re = /([A-Za-z0-9가-힣]+)|([^A-Za-z0-9가-힣])/g, out = "", m, wi = 0;
    while ((m = re.exec(modelText)) !== null) {
      if (m[1] !== undefined) {
        var raw = m[1];
        out += matched[wi] ? esc(raw) : '<span class="diff">' + esc(raw) + "</span>";
        wi++;
      } else {
        out += esc(m[2]);
      }
    }
    return out;
  }

  // ---- filters / list ----
  function buildFilters() {
    var subs = {}, types = {};
    DATA.problems.forEach(function (p) {
      subs[p.subject] = true;
      if (p.typeId) types[p.typeId] = true;
    });
    el.subjectFilter.innerHTML = '<option value="all">과목: 전체</option>' +
      Object.keys(subs).map(function (s) {
        return '<option value="' + s + '">' + (SUBJECT_LABEL[s] || s) + "</option>";
      }).join("");
    el.typeFilter.innerHTML = '<option value="all">유형: 전체</option>' +
      Object.keys(types).sort().map(function (t) {
        return '<option value="' + t + '">' + t + "</option>";
      }).join("");
    if (DATA.sources && DATA.sources[0]) el.title.textContent = DATA.sources[0].title;
  }

  function computeList() {
    var list = DATA.problems.filter(function (p) {
      if (state.subject !== "all" && p.subject !== state.subject) return false;
      if (state.type !== "all" && p.typeId !== state.type) return false;
      if (state.wrongOnly && status[p.id] !== "wrong") return false;
      return true;
    });
    if (state.shuffle) list = shuffleArr(list);
    state.list = list;
    if (state.idx >= list.length) state.idx = list.length - 1;
    if (state.idx < 0) state.idx = 0;
  }

  // ---- render ----
  function render() {
    computeList();
    var total = state.list.length;
    if (total === 0) {
      el.stem.textContent = state.wrongOnly ? "오답 노트가 비어 있습니다." : "해당 조건의 문제가 없습니다.";
      el.qNumber.textContent = ""; el.qType.textContent = ""; el.qTier.textContent = "";
      el.qSource.textContent = ""; el.passage.innerHTML = ""; el.options.innerHTML = "";
      el.essayBox.classList.add("hidden"); el.answerPanel.classList.add("hidden");
      el.progress.textContent = "0 / 0"; el.progressFill.style.width = "0%";
      return;
    }
    var p = state.list[state.idx];
    var isRev = !!revealed[p.id];

    el.qNumber.textContent = p.number + "번";
    el.qType.textContent = p.qtype === "choice" ? "객관식" : "서답형";
    el.qTier.textContent = (p.typeId || "") + (p.tier ? "·" + p.tier : "");
    el.qSource.textContent = (SUBJECT_LABEL[p.subject] || p.subject);
    el.stem.innerHTML = md(p.stem);
    el.passage.innerHTML = md(p.passage);

    el.options.innerHTML = "";
    if (p.qtype === "choice") {
      el.essayBox.classList.add("hidden");
      var cNum = correctNum(p.answer);
      var chNum = choice[p.id];
      p.options.forEach(function (opt) {
        var num = opt.charAt(0);
        var div = document.createElement("div");
        div.className = "option";
        var body = opt.slice(1).trim();
        div.innerHTML = '<span class="num">' + esc(num) + "</span><span>" + md(body) + "</span>";
        if (isRev) {
          if (num === cNum) div.classList.add("correct");
          else if (num === chNum) div.classList.add("wrong");
        } else if (num === chNum) {
          div.classList.add("chosen");
        }
        div.addEventListener("click", function (e) {
          e.stopPropagation();
          choice[p.id] = num; save(LS.choice, choice);
          revealed[p.id] = true; save(LS.revealed, revealed);
          render();
        });
        el.options.appendChild(div);
      });
    } else {
      el.essayBox.classList.remove("hidden");
      if (document.activeElement !== el.userAnswer) el.userAnswer.value = answers[p.id] || "";
    }

    // answer panel
    if (isRev) {
      el.answerPanel.classList.remove("hidden");
      el.revealBtn.classList.add("hidden");
      if (p.qtype === "choice") {
        el.answerText.innerHTML = md(p.answer);
        el.diffBox.classList.add("hidden");
        el.autoStatus.classList.remove("hidden");
        el.markRow.classList.add("hidden");
        var ch = choice[p.id];
        if (ch) {
          status[p.id] = (ch === cNum) ? "correct" : "wrong";
          save(LS.status, status);
        }
        if (!ch) { el.autoStatus.textContent = "보기를 선택하면 자동 채점됩니다"; el.autoStatus.className = "auto-status none"; }
        else if (ch === cNum) { el.autoStatus.textContent = "✅ 정답"; el.autoStatus.className = "auto-status ok"; }
        else { el.autoStatus.textContent = "❌ 오답 (정답 " + cNum + ")"; el.autoStatus.className = "auto-status no"; }
        el.explanation.innerHTML = md(p.explanation);
      } else {
        el.autoStatus.classList.add("hidden");
        el.markRow.classList.remove("hidden");
        updateEssayDiff(p);
        el.explanation.innerHTML = md(p.explanation);
        el.correctBtn.classList.toggle("active", status[p.id] === "correct");
        el.wrongMarkBtn.classList.toggle("active", status[p.id] === "wrong");
      }
    } else {
      el.answerPanel.classList.add("hidden");
      if (p.qtype === "essay") el.revealBtn.classList.remove("hidden");
    }

    el.progress.textContent = (state.idx + 1) + " / " + total;
    el.progressFill.style.width = ((state.idx + 1) / total * 100) + "%";
    el.prevBtn.disabled = state.idx === 0;
    el.nextBtn.disabled = state.idx === total - 1;
    window.scrollTo(0, 0);
  }

  function revealCurrent() {
    var p = state.list[state.idx];
    if (!p) return;
    revealed[p.id] = true; save(LS.revealed, revealed);
    render();
  }

  function updateEssayDiff(p) {
    if (!revealed[p.id]) return;
    el.answerText.innerHTML = renderDiff(answers[p.id] || "", p.answer);
    var ua = (answers[p.id] || "").trim();
    if (ua) {
      el.diffBox.classList.remove("hidden");
      el.diffBox.innerHTML = '<div class="user-answer"><span class="ua-label">내 답</span>' + esc(answers[p.id]) + "</div>";
    } else {
      el.diffBox.classList.add("hidden");
    }
  }

  function go(delta) {
    var n = state.idx + delta;
    if (n < 0 || n >= state.list.length) return;
    state.idx = n;
    render();
  }

  function mark(val) {
    var p = state.list[state.idx];
    if (!p) return;
    if (status[p.id] === val) { delete status[p.id]; }
    else { status[p.id] = val; }
    save(LS.status, status);
    render();
  }

  // ---- 단일 HTML 내보내기 (서버/Python 불필요) ----
  function exportStandalone() {
    if (!DATA.problems.length) { alert("내보낼 문제가 없습니다."); return; }
    var json = JSON.stringify(DATA).replace(/</g, "\\u003c");
    var html = "<!DOCTYPE html>\n" + document.documentElement.outerHTML;
    // 실제 데이터 태그만 제거 (app.js 내 동일 문자열 리터럴과 구분하기 위해
    // 바로 뒤의 window.QUIZ_DATA = 로 앵커링)
    html = html.replace(/<script id="quiz-data">\s*\nwindow\.QUIZ_DATA =[\s\S]*?<\/script>/i, "");
    var injected = "window.QUIZ_EMBEDDED = true;\nwindow.QUIZ_DATA = " + json + ";";
    html = html.replace(/(<head[^>]*>)/i, "$1\n<script>" + injected + "<\/script>");
    var blob = new Blob([html], { type: "text/html;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    var base = (DATA.sources && DATA.sources[0] && DATA.sources[0].title) ? DATA.sources[0].title : "quiz";
    a.href = url; a.download = base.replace(/[\\/:*?"<>|]/g, "_") + ".html";
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 0);
  }

  // ---- MD 파일 로드 (Python 변환 없이 브라우저에서 직접) ----
  function loadFiles(fileList) {
    var files = Array.prototype.slice.call(fileList);
    if (!files.length) return;
    var pending = files.length, store = [];
    files.forEach(function (f) {
      var reader = new FileReader();
      reader.onload = function () {
        store.push({ name: f.name, text: String(reader.result || "") });
        pending--;
        if (pending === 0) finishLoad(store);
      };
      reader.readAsText(f, "utf-8");
    });
  }
  function finishLoad(store) {
    if (!store.length) return;
    DATA = window.QuizParser.parseAll(store);
    save(LS.md, store);
    buildFilters();
    state.idx = 0;
    el.dropHint.classList.add("hidden");
    render();
  }
  function restoreMd() {
    try {
      var store = JSON.parse(localStorage.getItem(LS.md));
      if (store && store.length) { DATA = window.QuizParser.parseAll(store); return true; }
    } catch (e) {}
    return false;
  }

  // ---- events ----
  el.subjectFilter.addEventListener("change", function () { state.subject = this.value; state.idx = 0; render(); });
  el.typeFilter.addEventListener("change", function () { state.type = this.value; state.idx = 0; render(); });
  el.shuffleBtn.addEventListener("click", function () {
    state.shuffle = !state.shuffle; this.classList.toggle("active", state.shuffle);
    state.idx = 0; render();
  });
  el.wrongBtn.addEventListener("click", function () {
    state.wrongOnly = !state.wrongOnly; this.classList.toggle("active", state.wrongOnly);
    state.idx = 0; render();
  });
  el.resetBtn.addEventListener("click", function () {
    if (confirm("맞음/틀림 기록과 공개 상태를 초기화할까요?")) {
      status = {}; choice = {}; revealed = {}; answers = {};
      save(LS.status, status); save(LS.choice, choice); save(LS.revealed, revealed); save(LS.answer, answers);
      render();
    }
  });
  el.revealBtn.addEventListener("click", function (e) { e.stopPropagation(); revealCurrent(); });
  el.card.addEventListener("click", function () { revealCurrent(); });
  el.correctBtn.addEventListener("click", function (e) { e.stopPropagation(); mark("correct"); });
  el.wrongMarkBtn.addEventListener("click", function (e) { e.stopPropagation(); mark("wrong"); });
  el.prevBtn.addEventListener("click", function () { go(-1); });
  el.nextBtn.addEventListener("click", function () { go(1); });
  el.exportBtn.addEventListener("click", function () { exportStandalone(); });

  // 서답형 입력
  el.userAnswer.addEventListener("click", function (e) { e.stopPropagation(); });
  el.userAnswer.addEventListener("input", function () {
    var p = state.list[state.idx];
    if (!p) return;
    answers[p.id] = el.userAnswer.value;
    save(LS.answer, answers);
    if (revealed[p.id]) updateEssayDiff(p);
  });

  el.loadBtn.addEventListener("click", function () { el.fileInput.click(); });
  el.dropLoadBtn.addEventListener("click", function () { el.fileInput.click(); });
  el.fileInput.addEventListener("change", function () { loadFiles(this.files); this.value = ""; });
  ["dragenter", "dragover"].forEach(function (ev) {
    document.addEventListener(ev, function (e) { e.preventDefault(); el.dropHint.classList.add("dragover"); });
  });
  ["dragleave", "drop"].forEach(function (ev) {
    document.addEventListener(ev, function (e) { e.preventDefault(); el.dropHint.classList.remove("dragover"); });
  });
  document.addEventListener("drop", function (e) {
    if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files.length) {
      loadFiles(e.dataTransfer.files);
    }
  });

  document.addEventListener("keydown", function (e) {
    if (e.target && /^(SELECT|INPUT|TEXTAREA)$/.test(e.target.tagName)) return;
    if (e.key === "ArrowRight") { go(1); }
    else if (e.key === "ArrowLeft") { go(-1); }
    else if (e.key === " " || e.key === "Enter") { e.preventDefault(); revealCurrent(); }
  });

  // ---- init ----
  if (window.QUIZ_EMBEDDED) {
    DATA = window.QUIZ_DATA || { problems: [] };
  } else if (!restoreMd() && !(window.QUIZ_DATA && window.QUIZ_DATA.problems.length)) {
    DATA = { problems: [] };
  }
  buildFilters();
  render();
  if (!DATA.problems.length) el.dropHint.classList.remove("hidden");
})();
