"""Gera os PDFs de material didático do Caderno de Prática.

Uso:  python gerar.py teclado1
Cada tópico vira uma página HTML (com diagramas em SVG) impressa em PDF pelo Chrome sem interface.
O conteúdo de cada módulo fica em um arquivo próprio (ex.: teclado1.py).
"""
import html
import importlib
import os
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
CHROME = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]

# ---------- diagramas ----------

BRANCAS = ["C", "D", "E", "F", "G", "A", "B"]
PRETAS = {"C": "C#", "D": "D#", "F": "F#", "G": "G#", "A": "A#"}
BEMOIS = {"Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#", "Bb": "A#"}
NOMES = {"C": "Dó", "D": "Ré", "E": "Mi", "F": "Fá", "G": "Sol", "A": "Lá", "B": "Si"}


def _norm(k):
    nota, oit = k[:-1], k[-1]
    return BEMOIS.get(nota, nota) + oit


def teclado(marcas=None, oitavas=2, letras=False, solfejo=False, ww=30, wh=128, legenda=None):
    """Teclado em SVG. marcas: {"C0": ("1", "d"), ...}; "d" = mão direita (verde), "e" = mão esquerda (âmbar), "n" = neutro."""
    marcas = {_norm(k): v for k, v in (marcas or {}).items()}
    cores = {"d": ("#99AB59", "#1C2410"), "e": ("#E7A64A", "#2A1A04"), "n": ("#4D5C1B", "#FFFFFF")}
    n = 7 * oitavas + 1
    W, H = n * ww, wh
    bw, bh = ww * 0.62, wh * 0.62
    out = [f'<svg viewBox="-2 -2 {W + 4} {H + 4}" width="100%" style="max-width:{W + 4}px" xmlns="http://www.w3.org/2000/svg" role="img">']
    for i in range(n):
        nota = BRANCAS[i % 7]
        chave = f"{nota}{i // 7}"
        x = i * ww
        m = marcas.get(chave)
        fill = "#F2F5E6" if m else "#FFFFFF"
        out.append(f'<rect x="{x}" y="0" width="{ww}" height="{H}" rx="4" fill="{fill}" stroke="#2B3320" stroke-width="1.4"/>')
        if letras or solfejo:
            txt = (NOMES[nota] if solfejo else nota)
            out.append(f'<text x="{x + ww / 2}" y="{H - 8}" text-anchor="middle" font-size="{10 if solfejo else 12}" font-weight="600" fill="#6B7556">{txt}</text>')
        if m:
            bg, fg = cores[m[1]]
            cy = H - (30 if (letras or solfejo) else 18)
            out.append(f'<circle cx="{x + ww / 2}" cy="{cy}" r="{ww * 0.36}" fill="{bg}"/>')
            out.append(f'<text x="{x + ww / 2}" y="{cy + 4.5}" text-anchor="middle" font-size="13" font-weight="800" fill="{fg}">{html.escape(m[0])}</text>')
    for i in range(n - 1):
        nota = BRANCAS[i % 7]
        if nota not in PRETAS:
            continue
        chave = f"{PRETAS[nota]}{i // 7}"
        x = (i + 1) * ww - bw / 2
        m = marcas.get(chave)
        out.append(f'<rect x="{x}" y="0" width="{bw}" height="{bh}" rx="3" fill="#1B2114"/>')
        if m:
            bg, fg = cores[m[1]]
            out.append(f'<circle cx="{x + bw / 2}" cy="{bh - 14}" r="{bw * 0.42}" fill="{bg}"/>')
            out.append(f'<text x="{x + bw / 2}" y="{bh - 9.5}" text-anchor="middle" font-size="12" font-weight="800" fill="{fg}">{html.escape(m[0])}</text>')
    out.append("</svg>")
    fig = "".join(out)
    if legenda:
        fig += f'<div class="leg">{legenda}</div>'
    return fig


def figura(svg, legenda):
    return f'<figure>{svg}<figcaption>{legenda}</figcaption></figure>'


# ---------- página ----------
def pauta(notas, titulo="", w=600):
    """Pentagrama em SVG. notas: [(posição, rótulo)], posição 0 = 1ª linha (de baixo), 1 = 1º espaço, 2 = 2ª linha...
    Posições negativas ou acima de 8 ganham linhas suplementares."""
    gap = 12
    top = 34
    base = top + 4 * gap   # y da 1ª linha
    h = base + 56
    s = [f'<svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px" xmlns="http://www.w3.org/2000/svg">']
    if titulo:
        s.append(f'<text x="4" y="14" font-size="12" font-weight="800" fill="#4D5C1B">{html.escape(titulo)}</text>')
    for i in range(5):
        y = base - i * gap
        s.append(f'<line x1="4" y1="{y}" x2="{w - 4}" y2="{y}" stroke="#2B3320" stroke-width="1.2"/>')
    passo = (w - 70) / max(len(notas), 1)
    for k, (pos, rot) in enumerate(notas):
        x = 50 + k * passo + passo / 2
        y = base - pos * gap / 2
        for sup in range(-2, pos - 1, -2) if pos <= -2 else []:
            s.append(f'<line x1="{x - 13}" y1="{base - sup * gap / 2}" x2="{x + 13}" y2="{base - sup * gap / 2}" stroke="#2B3320" stroke-width="1.2"/>')
        for sup in range(10, pos + 1, 2) if pos >= 10 else []:
            s.append(f'<line x1="{x - 13}" y1="{base - sup * gap / 2}" x2="{x + 13}" y2="{base - sup * gap / 2}" stroke="#2B3320" stroke-width="1.2"/>')
        s.append(f'<ellipse cx="{x}" cy="{y}" rx="7.5" ry="5.6" transform="rotate(-18 {x} {y})" fill="#1C2410"/>')
        s.append(f'<text x="{x}" y="{h - 8}" text-anchor="middle" font-size="11" font-weight="700" fill="#4D5C1B">{html.escape(rot)}</text>')
    s.append("</svg>")
    return "".join(s)


CSS = """
@page { size: A4; margin: 16mm 16mm 18mm; }
@page { @bottom-left { content: "Caderno de Prática · %(modulo)s"; font: 600 8.5pt 'Figtree', 'Segoe UI', sans-serif; color: #6B7556; }
        @bottom-right { content: "Página " counter(page) " de " counter(pages); font: 600 8.5pt 'Figtree', 'Segoe UI', sans-serif; color: #6B7556; } }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
html { font: 10.5pt/1.55 'Figtree', 'Segoe UI', sans-serif; color: #1C2410; }
body { margin: 0; }
h1, h2, h3 { font-family: 'Bricolage Grotesque', 'Figtree', 'Segoe UI', sans-serif; letter-spacing: -0.01em; margin: 0; }
p { margin: 0 0 8px; }
.hero { background: linear-gradient(135deg, #99AB59 0%, #BCCB82 100%); border-radius: 18px; padding: 20px 22px 18px; margin-bottom: 18px; position: relative; overflow: hidden; }
.hero .kick { font-size: 8.5pt; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; opacity: .8; }
.hero h1 { font-size: 24pt; line-height: 1.08; margin: 6px 0 8px; font-weight: 800; max-width: 82%; }
.hero p { font-size: 11pt; margin: 0; max-width: 80%; }
.hero .num { position: absolute; right: 18px; top: 8px; font: 800 64pt/1 'Bricolage Grotesque', sans-serif; opacity: .18; }
.hero .keys { position: absolute; left: 0; right: 0; bottom: 0; height: 7px; background: repeating-linear-gradient(90deg, rgba(28,36,16,.25) 0 1px, transparent 1px 16px); }
.goals { display: grid; grid-template-columns: 1fr 1fr; gap: 8px 14px; background: #F4F6EC; border: 1px solid #DCE3C6; border-radius: 14px; padding: 12px 14px; margin-bottom: 16px; }
.goals h3 { grid-column: 1 / -1; font-size: 11pt; }
.goals div { display: flex; gap: 8px; align-items: flex-start; font-size: 9.8pt; }
.goals div::before { content: "✓"; flex: none; width: 18px; height: 18px; border-radius: 50%; background: #99AB59; color: #1C2410; font-size: 9pt; font-weight: 800; display: grid; place-items: center; margin-top: 1px; }
h2 { font-size: 14pt; margin: 12px 0 6px; display: flex; align-items: center; gap: 8px; break-after: avoid; }
h2::before { content: ""; width: 6px; height: 18px; border-radius: 3px; background: #99AB59; }
figure { margin: 10px 0 14px; padding: 14px; border: 1px solid #DCE3C6; border-radius: 14px; text-align: center; break-inside: avoid; background: #FCFDF8; }
figcaption { font-size: 9pt; color: #5A6447; margin-top: 8px; }
.leg { font-size: 8.5pt; color: #5A6447; margin-top: 6px; }
.leg i { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin: 0 4px 0 10px; vertical-align: -1px; }
.call { border-radius: 14px; padding: 12px 14px; margin: 12px 0; break-inside: avoid; background: #ECF1DB; border-left: 5px solid #99AB59; }
.call b.t { display: block; font-family: 'Bricolage Grotesque', sans-serif; font-size: 11pt; margin-bottom: 4px; }
.call.warm { background: #FBF1E2; border-left-color: #E7A64A; }
table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 9.6pt; margin: 6px 0 12px; break-inside: avoid; border: 1px solid #DCE3C6; border-radius: 12px; overflow: hidden; }
th { background: #4D5C1B; color: #fff; text-align: left; padding: 7px 10px; font-weight: 700; }
td { padding: 7px 10px; border-top: 1px solid #E5EAD3; vertical-align: top; }
tr:nth-child(even) td { background: #F7F9F0; }
.steps { counter-reset: s; list-style: none; padding: 0; margin: 2px 0 6px; display: grid; gap: 5px; }
.steps li { counter-increment: s; display: grid; grid-template-columns: 26px 1fr; gap: 10px; align-items: start; break-inside: avoid; }
.steps li::before { content: counter(s); width: 24px; height: 24px; border-radius: 8px; background: #1C2410; color: #DDE7B5; font-weight: 800; font-size: 10pt; display: grid; place-items: center; }
.ex { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; margin: 4px 0 8px; }
.ex > div { display: grid; grid-template-columns: 18px 1fr; gap: 10px; align-items: start; border: 1px solid #DCE3C6; border-radius: 12px; padding: 8px 10px; break-inside: avoid; }
.ex > div::before { content: ""; width: 14px; height: 14px; border: 2px solid #99AB59; border-radius: 4px; margin-top: 2px; }
.ex b { display: block; }
.ex small { color: #5A6447; font-size: 9pt; }
.ex .meta { grid-column: 2; justify-self: start; font-size: 8.5pt; font-weight: 700; color: #4D5C1B; background: #ECF1DB; padding: 1px 8px; border-radius: 99px; white-space: nowrap; }
.err { display: grid; grid-template-columns: 1fr 1fr; gap: 0; border: 1px solid #DCE3C6; border-radius: 12px; overflow: hidden; break-inside: avoid; margin: 4px 0 10px; font-size: 9.4pt; }
.err > div { padding: 6px 12px; border-top: 1px solid #E5EAD3; }
.err > div:nth-child(-n+2) { border-top: 0; font-weight: 700; color: #fff; }
.err > div:nth-child(1) { background: #B4542B; }
.err > div:nth-child(2) { background: #4D5C1B; }
.err > div:nth-child(odd) { border-right: 1px solid #E5EAD3; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.res { background: #1C2410; color: #EEF3DD; border-radius: 16px; padding: 12px 16px; margin-top: 10px; break-inside: avoid; }
.res h3 { color: #C9D88E; font-size: 12pt; margin-bottom: 6px; }
.res ul { margin: 0; padding-left: 18px; }
.res li { margin: 3px 0; }
.pb { break-before: page; }
.notes { border: 1px solid #DCE3C6; border-radius: 14px; padding: 2mm 6mm 6mm; }
.notes div { height: 9mm; border-bottom: 1px solid #DCE3C6; }
.chip { display: inline-block; font-weight: 700; padding: 1px 8px; border-radius: 6px; background: #ECF1DB; color: #4D5C1B; }
.mono { font-family: Consolas, 'Courier New', monospace; font-weight: 700; }
"""

PAGINA = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{titulo}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;600;700;800&display=block">
<style>{css}</style></head><body>
<div class="hero"><div class="kick">{modulo} · Tópico {n} de {total}</div><h1>{titulo}</h1><p>{sub}</p><div class="num">{n:02d}</div><div class="keys"></div></div>
<div class="goals"><h3>Nesta aula você vai</h3>{goals}</div>
{p1}
<div class="pb"></div>
<h2>Passo a passo</h2><ol class="steps">{passos}</ol>
<h2>Exercícios para marcar</h2><div class="ex">{exercicios}</div>
<h2>Erros comuns</h2><div class="err"><div>O que acontece</div><div>Como corrigir</div>{erros}</div>
<div class="res"><h3>Resumo para lembrar</h3><ul>{resumo}</ul></div>
{extra}
</body></html>"""


def montar(modulo, n, total, t):
    return PAGINA.format(
        css=CSS.replace("%(modulo)s", modulo), modulo=modulo, n=n, total=total,
        titulo=t["titulo"], sub=t["sub"],
        goals="".join(f"<div>{g}</div>" for g in t["objetivos"]),
        p1=t["p1"],
        passos="".join(f"<li><div>{p}</div></li>" for p in t["passos"]),
        exercicios="".join(f'<div><span><b>{e[0]}</b><small>{e[1]}</small></span><span class="meta">{e[2]}</span></div>' for e in t["exercicios"]),
        erros="".join(f"<div>{a}</div><div>{b}</div>" for a, b in t["erros"]),
        extra=('<div class="pb"></div>' + t["extra"] + '<h2>Minhas anotações</h2><div class="notes">' + '<div></div>' * 14 + '</div>') if t.get("extra") else "",
        resumo="".join(f"<li>{r}</li>" for r in t["resumo"]),
    )


def imprimir(html_txt, destino):
    chrome = next(c for c in CHROME if os.path.exists(c))
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "pagina.html")
        with open(src, "w", encoding="utf-8") as f:
            f.write(html_txt)
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--run-all-compositor-stages-before-draw", "--virtual-time-budget=10000",
                        f"--user-data-dir={os.path.join(tmp, 'perfil')}",
                        f"--print-to-pdf={destino}", "file:///" + src.replace("\\", "/")],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)


def main():
    nome = sys.argv[1] if len(sys.argv) > 1 else "teclado1"
    mod = importlib.import_module(nome)
    saida = os.path.normpath(os.path.join(AQUI, "..", mod.PASTA))
    os.makedirs(saida, exist_ok=True)
    total = len(mod.TOPICOS)
    for i, t in enumerate(mod.TOPICOS, 1):
        destino = os.path.join(saida, f"{i:02d}-{t['slug']}.pdf")
        imprimir(montar(mod.MODULO, i, total, t), destino)
        print("ok", os.path.basename(destino))


if __name__ == "__main__":
    sys.path.insert(0, AQUI)
    main()
