# -*- coding: utf-8 -*-
import csv, json, re, html, os

OUT = os.path.dirname(os.path.abspath(__file__))

def md_inline(s):
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
    s = s.replace('\\*', '*')
    return s

# ---------- SKRYPT ----------
sections = []
cur = None
para = []
def flush_para():
    global para, cur
    text = ' '.join(l.strip() for l in para).strip()
    if text and cur is not None:
        cur['topics'].append(md_inline(text))
    para = []

for line in open(f"{OUT}/skrypt-egzamin.md", encoding="utf-8"):
    if line.startswith('## '):
        flush_para()
        cur = {"title": line[3:].strip(), "topics": []}
        sections.append(cur)
    elif line.strip() == '---':
        flush_para()
    elif line.startswith('# ') or line.strip()=='' :
        flush_para()
    else:
        if cur is not None:
            para.append(line)
flush_para()

# ---------- FISZKI ----------
cards = []
for q,a,d in csv.reader(open(f"{OUT}/fiszki-egzamin.csv", encoding="utf-8")):
    cards.append({"q":q,"a":a,"d":d})

# ---------- TEST ----------
raw = open(f"{OUT}/testy-egzamin.md", encoding="utf-8").read()
qpart, kpart = raw.split("# KLUCZ ODPOWIEDZI")
# questions
questions = {}
order = []
blocks = re.split(r'\n\*\*(\d+)\.\s', qpart)
# blocks[0] intro, then pairs (num, body)
for i in range(1, len(blocks), 2):
    num = int(blocks[i])
    body = blocks[i+1]
    # first line up to ** is the question text
    m = re.match(r'(.+?)\*\*(.*)', body, re.S)
    qtext = m.group(1).strip()
    rest = m.group(2)
    opts = {}
    for om in re.finditer(r'([A-D])\)\s*(.+)', rest):
        opts[om.group(1)] = om.group(2).strip()
    questions[num] = {"n":num, "q":qtext, "opts":opts}
    order.append(num)

# key
for km in re.finditer(r'(\d+)\.\s\*\*([A-D])\*\*\s*[—-]\s*(.+)', kpart):
    num = int(km.group(1))
    if num in questions:
        questions[num]["correct"] = km.group(2)
        questions[num]["expl"] = km.group(3).strip()

quiz = [questions[n] for n in order if "correct" in questions[n]]

# ---------- ELI5 (Prosto) ----------
eli5 = json.load(open(f"{OUT}/eli5-egzamin.json", encoding="utf-8"))["sections"]

# ---------- KRZYZOWKI ----------
krzyz = json.load(open(f"{OUT}/krzyzowki-egzamin.json", encoding="utf-8"))["puzzles"]

data = {"sections":sections, "cards":cards, "quiz":quiz, "eli5":eli5, "krzyz":krzyz}
DATA_JSON = json.dumps(data, ensure_ascii=False)

HTML = r'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Egzamin kwalifikacyjny — Informatyka / Data Science (AGH)</title>
<style>
:root{
  --bg:#0f1720; --panel:#16212e; --panel2:#1d2b3a; --border:#2a3b4d;
  --text:#e6edf3; --muted:#93a4b5; --accent:#4aa3ff; --accent2:#7ee0b8;
  --good:#3fb950; --bad:#f85149; --chip:#243546;
}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
  background:var(--bg);color:var(--text);line-height:1.55;font-size:16px}
header{padding:20px 22px;border-bottom:1px solid var(--border);background:linear-gradient(180deg,#16212e,#0f1720)}
h1{margin:0 0 4px;font-size:20px}
.sub{color:var(--muted);font-size:13px}
.wrap{max-width:960px;margin:0 auto;padding:0 16px 60px}
nav{display:flex;gap:8px;position:sticky;top:0;z-index:5;background:var(--bg);
  padding:12px 0;border-bottom:1px solid var(--border);flex-wrap:wrap}
.tab{padding:9px 16px;border:1px solid var(--border);background:var(--panel);color:var(--text);
  border-radius:999px;cursor:pointer;font-size:14px;font-weight:600}
.tab.active{background:var(--accent);border-color:var(--accent);color:#04121f}
.view{display:none;padding-top:18px}
.view.active{display:block}
select,button{font-family:inherit}
.filter{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.filter select{background:var(--panel);color:var(--text);border:1px solid var(--border);
  border-radius:8px;padding:8px 10px;font-size:14px}
.hint{color:var(--muted);font-size:13px}
.search{background:var(--panel);color:var(--text);border:1px solid var(--border);
  border-radius:8px;padding:8px 10px;font-size:14px;min-width:170px}
/* skrypt */
.sec-title{margin:22px 0 10px;font-size:17px;color:var(--accent2);border-left:3px solid var(--accent2);padding-left:10px}
.topic{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:14px 16px;margin:10px 0}
.topic strong:first-child{color:#fff}
.topic em{color:var(--accent2);font-style:italic}
/* prosto (eli5) */
.eli{background:var(--panel);border:1px solid var(--border);border-radius:10px;margin:10px 0;overflow:hidden}
.eli-head{padding:13px 16px;cursor:pointer;display:flex;gap:12px;align-items:flex-start}
.eli-head:hover{background:var(--panel2)}
.eli-caret{color:var(--accent);font-size:13px;margin-top:3px;transition:transform .2s;flex:0 0 auto}
.eli.open .eli-caret{transform:rotate(90deg)}
.eli-head .txt{flex:1}
.eli-head h4{margin:0 0 4px;font-size:15px;color:#fff}
.eli-head .lead{margin:0;color:var(--muted);font-size:14.5px}
.eli-more{display:none;padding:4px 18px 16px 40px;font-size:15px;border-top:1px solid var(--border);background:#111c27}
.eli.open .eli-more{display:block}
.eli-more p{margin:11px 0;color:var(--text)}
.eli-more strong{color:var(--accent2)}
.eli-more code{background:var(--chip);border:1px solid var(--border);border-radius:5px;padding:1px 6px;
  font-size:13px;color:#ffd9a0;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.eli-more ol,.eli-more ul{margin:8px 0;padding-left:22px}
.eli-more li{margin:8px 0}
.eli-more li strong{color:#fff}
/* fiszki */
.card-stage{perspective:1200px;margin:10px 0 16px}
.flip{position:relative;width:100%;min-height:230px;transition:transform .5s;transform-style:preserve-3d;cursor:pointer}
.flip.turned{transform:rotateY(180deg)}
.face{position:absolute;inset:0;backface-visibility:hidden;border:1px solid var(--border);
  border-radius:14px;padding:26px;display:flex;flex-direction:column;justify-content:center;background:var(--panel)}
.face .chip{position:absolute;top:12px;right:14px}
.back{transform:rotateY(180deg);background:var(--panel2)}
.face .lbl{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:10px}
.face .content{font-size:18px}
.back .content{font-size:16px}
.chip{background:var(--chip);border:1px solid var(--border);color:var(--muted);font-size:12px;
  padding:3px 9px;border-radius:999px}
.controls{display:flex;gap:8px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.controls .mid{color:var(--muted);font-size:14px}
.btn{background:var(--panel2);border:1px solid var(--border);color:var(--text);padding:10px 16px;
  border-radius:9px;cursor:pointer;font-size:14px;font-weight:600}
.btn:hover{border-color:var(--accent)}
.btn.primary{background:var(--accent);color:#04121f;border-color:var(--accent)}
.btn.mark-good{background:#12351f;border-color:var(--good);color:#8ff0a6}
.btn.mark-bad{background:#3a1616;border-color:var(--bad);color:#ffb4ae}
/* test */
.q{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:16px;margin:12px 0}
.q .num{color:var(--accent);font-weight:700;margin-right:6px}
.opt{display:block;border:1px solid var(--border);background:var(--panel2);border-radius:8px;
  padding:11px 13px;margin:8px 0;cursor:pointer;font-size:15px}
.opt:hover{border-color:var(--accent)}
.opt.sel{border-color:var(--accent);background:#173049}
.opt.correct{border-color:var(--good);background:#12351f}
.opt.wrong{border-color:var(--bad);background:#3a1616}
.expl{margin-top:10px;font-size:14px;color:var(--muted);border-top:1px dashed var(--border);padding-top:10px;display:none}
.expl.show{display:block}
.scorebar{position:sticky;bottom:0;background:var(--panel);border:1px solid var(--border);
  border-radius:12px;padding:12px 16px;margin-top:16px;display:flex;gap:14px;align-items:center;
  justify-content:space-between;flex-wrap:wrap}
.score-num{font-size:20px;font-weight:800}
.progress{height:8px;background:var(--panel2);border-radius:999px;overflow:hidden;flex:1;min-width:140px}
.progress > i{display:block;height:100%;width:0;background:var(--accent2);transition:width .3s}
.small{font-size:13px;color:var(--muted)}
a{color:var(--accent)}
/* krzyzowki */
.cw-wrap{display:flex;gap:22px;flex-wrap:wrap;align-items:flex-start}
.cw-grid-box{overflow:auto;max-width:100%;padding-bottom:6px}
table.cw{border-collapse:collapse}
table.cw td{width:30px;height:30px;padding:0;border:1px solid var(--border);position:relative;text-align:center}
table.cw td.blank{background:transparent;border:none}
table.cw td.cell{background:var(--panel2)}
table.cw td .num{position:absolute;top:1px;left:2px;font-size:9px;color:var(--muted);line-height:1;z-index:2;pointer-events:none}
table.cw input{width:30px;height:30px;border:none;background:transparent;color:var(--text);
  text-align:center;font-size:15px;font-weight:700;text-transform:uppercase;outline:none;caret-color:var(--accent)}
table.cw input:focus{background:#173049}
table.cw td.ok input{background:#12351f;color:#8ff0a6}
table.cw td.bad input{background:#3a1616;color:#ffb4ae}
table.cw td.hl{outline:2px solid var(--accent);outline-offset:-2px}
.cw-clues{flex:1;min-width:250px}
.cw-clues h4{margin:14px 0 6px;color:var(--accent);font-size:14px}
.cw-clues ol{margin:0;padding-left:26px}
.cw-clues li{margin:6px 0;font-size:14px;color:var(--muted)}
.cw-clues li b{color:var(--text)}
</style>
</head>
<body>
<header>
  <div class="wrap" style="padding-bottom:0">
    <h1>Egzamin kwalifikacyjny — Informatyka / Data Science (AGH)</h1>
    <div class="sub">Skrypt · proste wyjaśnienia · fiszki · test · krzyżówki — wszystko w jednym miejscu. Postęp zapisuje się w przeglądarce.</div>
  </div>
</header>
<div class="wrap">
  <nav>
    <div class="tab active" data-v="skrypt">📖 Skrypt</div>
    <div class="tab" data-v="prosto">🧒 Prosto</div>
    <div class="tab" data-v="fiszki">🃏 Fiszki</div>
    <div class="tab" data-v="test">✅ Test</div>
    <div class="tab" data-v="krzyzowki">🧩 Krzyżówki</div>
  </nav>

  <!-- SKRYPT -->
  <section class="view active" id="v-skrypt">
    <div class="filter">
      <label class="hint">Dział:</label>
      <select id="sec-filter"></select>
      <span class="hint" id="sec-count"></span>
    </div>
    <div id="skrypt-body"></div>
  </section>

  <!-- PROSTO (ELI5) -->
  <section class="view" id="v-prosto">
    <div class="filter">
      <label class="hint">Dział:</label>
      <select id="eli-filter"></select>
      <input id="eli-search" class="search" placeholder="Szukaj pojęcia…">
      <button class="btn" id="eli-expand">⤢ Rozwiń wszystko</button>
      <span class="hint" id="eli-count"></span>
    </div>
    <p class="small" style="margin-top:-6px">Każde zagadnienie wytłumaczone jak dla 5-latka — na szybkie „załapanie" o co chodzi, zanim wejdziesz w szczegóły w Skrypcie.</p>
    <div id="eli-body"></div>
  </section>

  <!-- FISZKI -->
  <section class="view" id="v-fiszki">
    <div class="filter">
      <label class="hint">Dział:</label>
      <select id="card-filter"></select>
      <button class="btn" id="shuffle">🔀 Tasuj</button>
      <span class="hint" id="deck-stats"></span>
    </div>
    <div class="card-stage">
      <div class="flip" id="flip">
        <div class="face front"><span class="chip" id="cf-chip"></span><div class="lbl">Pytanie</div><div class="content" id="cf-q"></div></div>
        <div class="face back"><span class="chip" id="cb-chip"></span><div class="lbl">Odpowiedź</div><div class="content" id="cf-a"></div></div>
      </div>
    </div>
    <div class="controls">
      <button class="btn" id="prev">← Poprzednia</button>
      <span class="mid" id="card-pos"></span>
      <button class="btn primary" id="next">Następna →</button>
    </div>
    <div class="controls" style="margin-top:10px">
      <button class="btn mark-bad" id="mark-bad">Nie umiem 🔁</button>
      <span class="mid small" id="know-stats"></span>
      <button class="btn mark-good" id="mark-good">Umiem ✓</button>
    </div>
    <p class="small">Kliknij kartę, aby ją obrócić. Klawisze: spacja = obróć, ← → = nawigacja, 1 = nie umiem, 2 = umiem.</p>
  </section>

  <!-- TEST -->
  <section class="view" id="v-test">
    <div class="filter">
      <label class="hint">Tryb:</label>
      <select id="test-filter"></select>
      <button class="btn" id="test-reset">↺ Reset</button>
      <span class="hint">Zaznacz odpowiedź — od razu zobaczysz wynik i wyjaśnienie.</span>
    </div>
    <div id="test-body"></div>
    <div class="scorebar">
      <div><span class="score-num" id="score">0 / 0</span> <span class="small" id="score-pct"></span></div>
      <div class="progress"><i id="prog"></i></div>
      <div class="small" id="score-msg">Powodzenia!</div>
    </div>
  </section>

  <!-- KRZYZOWKI -->
  <section class="view" id="v-krzyzowki">
    <div class="filter">
      <label class="hint">Dział:</label>
      <select id="cw-filter"></select>
      <button class="btn" id="cw-new">🔀 Nowa</button>
      <button class="btn" id="cw-check">✅ Sprawdź</button>
      <button class="btn" id="cw-reveal">💡 Pokaż</button>
      <button class="btn" id="cw-clear">↺ Wyczyść</button>
      <span class="hint" id="cw-msg"></span>
    </div>
    <p class="small" style="margin-top:-6px">Hasła zapisujemy bez polskich znaków (np. „ą"→„a", „ł"→„l"). Kliknij podpowiedź, aby podświetlić hasło na planszy.</p>
    <div class="cw-wrap">
      <div id="cw-grid" class="cw-grid-box"></div>
      <div id="cw-clues" class="cw-clues"></div>
    </div>
  </section>
</div>

<script>
const DATA = __DATA__;
const store = {
  get(k,d){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}},
  set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
};

// tabs
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>{
  document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
  document.querySelectorAll('.view').forEach(x=>x.classList.remove('active'));
  t.classList.add('active');
  document.getElementById('v-'+t.dataset.v).classList.add('active');
});

/* ---------- SKRYPT ---------- */
const secFilter=document.getElementById('sec-filter');
secFilter.innerHTML='<option value="-1">Wszystkie działy</option>'+
  DATA.sections.map((s,i)=>`<option value="${i}">${s.title}</option>`).join('');
function renderSkrypt(){
  const f=+secFilter.value;
  const secs=f<0?DATA.sections:[DATA.sections[f]];
  let n=0;
  document.getElementById('skrypt-body').innerHTML=secs.map(s=>{
    n+=s.topics.length;
    return `<div class="sec-title">${s.title}</div>`+
      s.topics.map(t=>`<div class="topic">${t}</div>`).join('');
  }).join('');
  document.getElementById('sec-count').textContent=`${n} zagadnień`;
}
secFilter.onchange=renderSkrypt; renderSkrypt();

/* ---------- PROSTO (ELI5) ---------- */
const eliFilter=document.getElementById('eli-filter');
eliFilter.innerHTML='<option value="-1">Wszystkie działy</option>'+
  DATA.eli5.map((s,i)=>`<option value="${i}">${s.title}</option>`).join('');
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function inl(s){s=esc(s);s=s.replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>');s=s.replace(/`(.+?)`/g,'<code>$1</code>');return s;}
function mdToHtml(md){
  const lines=md.trim().split('\n'); let html='', i=0;
  const isOl=l=>/^\d+\.\s/.test(l), isUl=l=>/^[-•]\s/.test(l);
  while(i<lines.length){
    if(lines[i].trim()===''){i++;continue;}
    if(isOl(lines[i])){
      const it=[]; while(i<lines.length&&isOl(lines[i])){it.push('<li>'+inl(lines[i].replace(/^\d+\.\s/,''))+'</li>');i++;}
      html+='<ol>'+it.join('')+'</ol>'; continue;
    }
    if(isUl(lines[i])){
      const it=[]; while(i<lines.length&&isUl(lines[i])){it.push('<li>'+inl(lines[i].replace(/^[-•]\s/,''))+'</li>');i++;}
      html+='<ul>'+it.join('')+'</ul>'; continue;
    }
    const para=[]; while(i<lines.length&&lines[i].trim()!==''&&!isOl(lines[i])&&!isUl(lines[i])){para.push(inl(lines[i]));i++;}
    html+='<p>'+para.join('<br>')+'</p>';
  }
  return html;
}
let eliAllOpen=false;
function updateExpandBtn(){document.getElementById('eli-expand').textContent=eliAllOpen?'⤡ Zwiń wszystko':'⤢ Rozwiń wszystko';}
function renderEli(){
  const f=+eliFilter.value;
  const q=(document.getElementById('eli-search').value||'').trim().toLowerCase();
  const secs=f<0?DATA.eli5:[DATA.eli5[f]];
  let n=0, out='';
  secs.forEach(s=>{
    const items=s.items.filter(it=>!q||it.term.toLowerCase().includes(q)||it.eli5.toLowerCase().includes(q)||(it.more||'').toLowerCase().includes(q));
    if(!items.length) return;
    out+=`<div class="sec-title">${esc(s.title)}</div>`;
    items.forEach(it=>{
      n++;
      const more=it.more?mdToHtml(it.more):'<p class="small">(brak rozwinięcia)</p>';
      out+=`<div class="eli"><div class="eli-head"><span class="eli-caret">▸</span><div class="txt"><h4>${esc(it.term)}</h4><p class="lead">${esc(it.eli5)}</p></div></div><div class="eli-more">${more}</div></div>`;
    });
  });
  document.getElementById('eli-body').innerHTML=out||'<p class="small">Brak wyników dla tego wyszukiwania.</p>';
  document.getElementById('eli-count').textContent=`${n} pojęć`;
  document.querySelectorAll('#eli-body .eli-head').forEach(h=>h.onclick=()=>h.parentElement.classList.toggle('open'));
  eliAllOpen=false; updateExpandBtn();
}
document.getElementById('eli-expand').onclick=()=>{
  eliAllOpen=!eliAllOpen;
  document.querySelectorAll('#eli-body .eli').forEach(e=>e.classList.toggle('open',eliAllOpen));
  updateExpandBtn();
};
eliFilter.onchange=renderEli;
document.getElementById('eli-search').oninput=renderEli;
renderEli();

/* ---------- FISZKI ---------- */
const dzialy=[...new Set(DATA.cards.map(c=>c.d))];
const cardFilter=document.getElementById('card-filter');
cardFilter.innerHTML='<option value="__all">Wszystkie ('+DATA.cards.length+')</option>'+
  dzialy.map(d=>`<option value="${d}">${d}</option>`).join('');
let deck=[], idx=0;
const known=store.get('agh_known',{});
function buildDeck(){
  const f=cardFilter.value;
  deck=DATA.cards.map((c,i)=>({...c,id:i})).filter(c=>f==='__all'||c.d===f);
  idx=0; showCard();
  updateDeckStats();
}
function updateDeckStats(){
  const total=DATA.cards.length;
  const k=Object.values(known).filter(Boolean).length;
  document.getElementById('deck-stats').textContent=`Umiesz ${k}/${total}`;
  document.getElementById('know-stats').textContent=`Umiesz ${k}/${total}`;
}
function showCard(){
  if(!deck.length){document.getElementById('cf-q').textContent='Brak fiszek';return;}
  const c=deck[idx];
  document.getElementById('flip').classList.remove('turned');
  document.getElementById('cf-q').textContent=c.q;
  document.getElementById('cf-a').textContent=c.a;
  document.getElementById('cf-chip').textContent=c.d;
  document.getElementById('cb-chip').textContent=c.d;
  const mark=known[c.id]?' ✓':'';
  document.getElementById('card-pos').textContent=`${idx+1} / ${deck.length}${mark}`;
}
document.getElementById('flip').onclick=()=>document.getElementById('flip').classList.toggle('turned');
document.getElementById('next').onclick=()=>{idx=(idx+1)%deck.length;showCard();};
document.getElementById('prev').onclick=()=>{idx=(idx-1+deck.length)%deck.length;showCard();};
document.getElementById('shuffle').onclick=()=>{deck.sort(()=>Math.random()-.5);idx=0;showCard();};
document.getElementById('mark-good').onclick=()=>{known[deck[idx].id]=true;store.set('agh_known',known);updateDeckStats();document.getElementById('next').click();};
document.getElementById('mark-bad').onclick=()=>{known[deck[idx].id]=false;store.set('agh_known',known);updateDeckStats();document.getElementById('next').click();};
cardFilter.onchange=buildDeck;
document.addEventListener('keydown',e=>{
  if(!document.getElementById('v-fiszki').classList.contains('active'))return;
  if(e.code==='Space'){e.preventDefault();document.getElementById('flip').classList.toggle('turned');}
  if(e.code==='ArrowRight')document.getElementById('next').click();
  if(e.code==='ArrowLeft')document.getElementById('prev').click();
  if(e.key==='1')document.getElementById('mark-bad').click();
  if(e.key==='2')document.getElementById('mark-good').click();
});
buildDeck();

/* ---------- TEST ---------- */
const testFilter=document.getElementById('test-filter');
testFilter.innerHTML='<option value="all">Wszystkie pytania ('+DATA.quiz.length+')</option>'+
  '<option value="random20">Losowe 20 (symulacja)</option>';
let answered={};
function renderTest(){
  answered={};
  let qs=DATA.quiz.slice();
  if(testFilter.value==='random20'){qs.sort(()=>Math.random()-.5);qs=qs.slice(0,20);}
  document.getElementById('test-body').innerHTML=qs.map((q,qi)=>{
    const letters=Object.keys(q.opts);
    return `<div class="q" data-correct="${q.correct}" data-i="${qi}">
      <div><span class="num">${qi+1}.</span>${q.q}</div>
      ${letters.map(L=>`<div class="opt" data-l="${L}">${L}) ${q.opts[L]}</div>`).join('')}
      <div class="expl"><strong>Poprawna: ${q.correct}.</strong> ${q.expl}</div>
    </div>`;
  }).join('');
  document.querySelectorAll('.q').forEach(qEl=>{
    qEl.querySelectorAll('.opt').forEach(opt=>{
      opt.onclick=()=>{
        const i=qEl.dataset.i;
        if(answered[i])return;
        answered[i]=true;
        const correct=qEl.dataset.correct;
        qEl.querySelectorAll('.opt').forEach(o=>{
          if(o.dataset.l===correct)o.classList.add('correct');
          else if(o===opt)o.classList.add('wrong');
        });
        if(opt.dataset.l===correct)opt.classList.add('correct');
        qEl.querySelector('.expl').classList.add('show');
        updateScore(qs.length);
      };
    });
  });
  updateScore(qs.length);
}
function updateScore(total){
  let ok=0,done=0;
  document.querySelectorAll('.q').forEach(qEl=>{
    const i=qEl.dataset.i;
    if(answered[i]){done++; if(!qEl.querySelector('.opt.wrong'))ok++;}
  });
  document.getElementById('score').textContent=`${ok} / ${done}`;
  const pct=done?Math.round(ok/done*100):0;
  document.getElementById('score-pct').textContent=done?`(${pct}%) · ${done}/${total} rozwiązanych`:'';
  document.getElementById('prog').style.width=(done/total*100)+'%';
  let msg='Powodzenia!';
  if(done===total&&total>0){msg=pct>=95?'🎯 Gotowość egzaminacyjna!':pct>=80?'Blisko — dobij słabe działy.':'Powtórz materiał i spróbuj znów.';}
  document.getElementById('score-msg').textContent=msg;
}
testFilter.onchange=renderTest;
document.getElementById('test-reset').onclick=renderTest;
renderTest();

/* ---------- KRZYZOWKI ---------- */
const cwFilter=document.getElementById('cw-filter');
cwFilter.innerHTML=DATA.krzyz.map((p,i)=>`<option value="${i}">${p.title}</option>`).join('');
let cwState=null;
const PL={'Ą':'A','Ć':'C','Ę':'E','Ł':'L','Ń':'N','Ó':'O','Ś':'S','Ź':'Z','Ż':'Z'};
function cwNorm(s){return (s||'').toUpperCase().split('').map(ch=>PL[ch]||ch).join('').replace(/[^A-Z]/g,'');}
const cwKey=(r,c)=>r+','+c;

function cwLayout(items){
  const grid={}, placed=[];
  function canPlace(a,r,c,dir){
    if(dir==='H'){ if(grid[cwKey(r,c-1)]||grid[cwKey(r,c+a.length)])return false; }
    else { if(grid[cwKey(r-1,c)]||grid[cwKey(r+a.length,c)])return false; }
    for(let i=0;i<a.length;i++){
      const rr=dir==='H'?r:r+i, cc=dir==='H'?c+i:c, cur=grid[cwKey(rr,cc)];
      if(cur){ if(cur!==a[i])return false; }
      else if(dir==='H'){ if(grid[cwKey(rr-1,cc)]||grid[cwKey(rr+1,cc)])return false; }
      else { if(grid[cwKey(rr,cc-1)]||grid[cwKey(rr,cc+1)])return false; }
    }
    return true;
  }
  function put(it,r,c,dir){
    for(let i=0;i<it.ans.length;i++){
      const rr=dir==='H'?r:r+i, cc=dir==='H'?c+i:c;
      grid[cwKey(rr,cc)]=it.ans[i];
    }
    placed.push({ans:it.ans,clue:it.clue,row:r,col:c,dir});
  }
  put(items[0],0,0,'H');
  for(let k=1;k<items.length;k++){
    const it=items[k]; let done=false;
    for(let pIdx=0;pIdx<placed.length&&!done;pIdx++){
      const p=placed[pIdx];
      for(let pi=0;pi<p.ans.length&&!done;pi++){
        for(let ii=0;ii<it.ans.length&&!done;ii++){
          if(p.ans[pi]!==it.ans[ii])continue;
          const pr=p.dir==='H'?p.row:p.row+pi, pc=p.dir==='H'?p.col+pi:p.col;
          const dir=p.dir==='H'?'V':'H';
          const r=dir==='H'?pr:pr-ii, c=dir==='H'?pc-ii:pc;
          if(canPlace(it.ans,r,c,dir)){ put(it,r,c,dir); done=true; }
        }
      }
    }
  }
  return placed;
}
function cwBuild(words){
  const base=words.map(w=>({ans:cwNorm(w.a),clue:w.c})).filter(w=>w.ans.length>=3);
  let best=null;
  for(let att=0;att<80;att++){
    let items=base.slice();
    if(att===0) items.sort((x,y)=>y.ans.length-x.ans.length);
    else items.sort(()=>Math.random()-0.5);
    const placed=cwLayout(items);
    if(!best||placed.length>best.length) best=placed;
    if(best.length===base.length) break;
  }
  let minR=1e9,minC=1e9,maxR=-1e9,maxC=-1e9;
  best.forEach(p=>{for(let i=0;i<p.ans.length;i++){
    const rr=p.dir==='H'?p.row:p.row+i, cc=p.dir==='H'?p.col+i:p.col;
    minR=Math.min(minR,rr);maxR=Math.max(maxR,rr);minC=Math.min(minC,cc);maxC=Math.max(maxC,cc);
  }});
  best.forEach(p=>{p.row-=minR;p.col-=minC;});
  const rows=maxR-minR+1, cols=maxC-minC+1, cells={}, starts={};
  best.forEach(p=>{
    starts[cwKey(p.row,p.col)]=true;
    for(let i=0;i<p.ans.length;i++){
      const rr=p.dir==='H'?p.row:p.row+i, cc=p.dir==='H'?p.col+i:p.col;
      if(!cells[cwKey(rr,cc)]) cells[cwKey(rr,cc)]={r:rr,c:cc,sol:p.ans[i]};
    }
  });
  let num=0; const numAt={};
  for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){
    if(cells[cwKey(r,c)]&&starts[cwKey(r,c)]){num++;numAt[cwKey(r,c)]=num;}
  }
  const across=[],down=[];
  best.forEach(p=>{
    const n=numAt[cwKey(p.row,p.col)];
    const cellKeys=[];
    for(let i=0;i<p.ans.length;i++){
      const rr=p.dir==='H'?p.row:p.row+i, cc=p.dir==='H'?p.col+i:p.col;
      cellKeys.push(cwKey(rr,cc));
    }
    (p.dir==='H'?across:down).push({n,clue:p.clue,len:p.ans.length,keys:cellKeys});
  });
  across.sort((a,b)=>a.n-b.n); down.sort((a,b)=>a.n-b.n);
  return {rows,cols,cells,numAt,across,down,placed:best.length,total:base.length};
}
function cwRender(){
  const p=DATA.krzyz[+cwFilter.value];
  cwState=cwBuild(p.words);
  const {rows,cols,cells,numAt}=cwState;
  let h='<table class="cw"><tbody>';
  for(let r=0;r<rows;r++){
    h+='<tr>';
    for(let c=0;c<cols;c++){
      const cell=cells[cwKey(r,c)];
      if(!cell){h+='<td class="blank"></td>';continue;}
      const n=numAt[cwKey(r,c)];
      h+=`<td class="cell" data-k="${r},${c}">${n?`<span class="num">${n}</span>`:''}<input maxlength="1" data-k="${r},${c}" aria-label="litera"></td>`;
    }
    h+='</tr>';
  }
  h+='</tbody></table>';
  document.getElementById('cw-grid').innerHTML=h;
  const cl=document.getElementById('cw-clues');
  const li=w=>`<li value="${w.n}" data-keys="${w.keys.join(' ')}"><b></b>${esc(w.clue)} <span class="small">(${w.len})</span></li>`;
  cl.innerHTML='<h4>Poziomo →</h4><ol>'+cwState.across.map(li).join('')+
    '</ol><h4>Pionowo ↓</h4><ol>'+cwState.down.map(li).join('')+'</ol>';
  document.getElementById('cw-msg').textContent=`${cwState.placed}/${cwState.total} haseł na planszy`;
  document.querySelectorAll('.cw input').forEach(inp=>{
    inp.addEventListener('input',()=>{
      inp.value=cwNorm(inp.value).slice(-1);
      inp.parentElement.classList.remove('ok','bad');
    });
  });
  cl.querySelectorAll('li').forEach(item=>{
    item.onclick=()=>{
      document.querySelectorAll('table.cw td.hl').forEach(td=>td.classList.remove('hl'));
      item.dataset.keys.split(' ').forEach(k=>{
        const td=document.querySelector(`td[data-k="${k}"]`);
        if(td)td.classList.add('hl');
      });
      const first=document.querySelector(`input[data-k="${item.dataset.keys.split(' ')[0]}"]`);
      if(first)first.focus();
    };
  });
}
function cwCheck(){
  let ok=0,tot=0;
  document.querySelectorAll('.cw input').forEach(inp=>{
    const sol=cwState.cells[inp.dataset.k].sol; tot++;
    const td=inp.parentElement; td.classList.remove('ok','bad');
    const v=cwNorm(inp.value);
    if(v===sol){td.classList.add('ok');ok++;}
    else if(v){td.classList.add('bad');}
  });
  const msg=ok===tot?'🎯 Wszystko poprawnie!':`Poprawne litery: ${ok}/${tot}`;
  document.getElementById('cw-msg').textContent=msg;
}
function cwReveal(){
  document.querySelectorAll('.cw input').forEach(inp=>{
    inp.value=cwState.cells[inp.dataset.k].sol;
    inp.parentElement.classList.remove('bad');inp.parentElement.classList.add('ok');
  });
  document.getElementById('cw-msg').textContent='Pokazano rozwiązanie';
}
function cwClear(){
  document.querySelectorAll('.cw input').forEach(inp=>{inp.value='';inp.parentElement.classList.remove('ok','bad');});
  document.getElementById('cw-msg').textContent=`${cwState.placed}/${cwState.total} haseł na planszy`;
}
cwFilter.onchange=cwRender;
document.getElementById('cw-new').onclick=cwRender;
document.getElementById('cw-check').onclick=cwCheck;
document.getElementById('cw-reveal').onclick=cwReveal;
document.getElementById('cw-clear').onclick=cwClear;
cwRender();
</script>
</body>
</html>'''

HTML = HTML.replace("__DATA__", DATA_JSON)
open(f"{OUT}/egzamin-agh.html","w",encoding="utf-8").write(HTML)
print("OK: sekcje", len(sections), "| fiszki", len(cards), "| pytania", len(quiz),
      "| eli5", sum(len(s['items']) for s in eli5), "| krzyzowki", len(krzyz))
