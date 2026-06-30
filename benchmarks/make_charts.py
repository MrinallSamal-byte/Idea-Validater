#!/usr/bin/env python3
"""Generate SVG bar charts from the benchmark numbers, into assets/.
Charts are built from the same values the scorer reports, so they can't drift.
Static SVG (no scripts) — renders as an <img> on GitHub."""
import os
BG="#0d1117"; GRID="#30363d"; TXT="#c9d1d9"; MUT="#8b949e"; TITLE="#f0f6fc"
GRAY="#6e7681"; GREEN="#2ea043"

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def chart(path, title, subtitle, groups, series, caption, legend=None, bar_colors=None):
    # groups: list of (line1,line2); series: list of (label,color,[values per group])
    W,H=820,470; L,R,T,B=64,24,112,104
    pw=W-L-R; ph=H-T-B; base=T+ph
    n=len(groups); gw=pw/n
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif">']
    svg.append(f'<rect width="{W}" height="{H}" rx="10" fill="{BG}"/>')
    svg.append(f'<text x="{L}" y="34" fill="{TITLE}" font-size="19" font-weight="600">{esc(title)}</text>')
    svg.append(f'<text x="{L}" y="56" fill="{MUT}" font-size="12.5">{esc(subtitle)}</text>')
    # legend
    if legend:
        lx=L
        for lab,col in legend:
            svg.append(f'<rect x="{lx}" y="64" width="13" height="13" rx="2" fill="{col}"/>')
            svg.append(f'<text x="{lx+18}" y="75" fill="{TXT}" font-size="12.5">{esc(lab)}</text>')
            lx+=18+9*len(lab)+24
    # gridlines + y labels
    for p in (0,25,50,75,100):
        y=base-p/100*ph
        svg.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
        svg.append(f'<text x="{L-8}" y="{y+4:.1f}" fill="{MUT}" font-size="11" text-anchor="end">{p}</text>')
    nb=len(series); bw=min(46,(gw-26)/nb)
    for gi,(l1,l2) in enumerate(groups):
        gx=L+gw*gi; cx=gx+gw/2
        total=nb*bw+(nb-1)*8; start=cx-total/2
        for si,(lab,col,vals) in enumerate(series):
            v=vals[gi]; bh=v/100*ph; bx=start+si*(bw+8); by=base-bh
            fill = bar_colors[gi] if bar_colors else col
            svg.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="3" fill="{fill}"/>')
            svg.append(f'<text x="{bx+bw/2:.1f}" y="{by-6:.1f}" fill="{TXT}" font-size="12" font-weight="600" text-anchor="middle">{v:g}%</text>')
        svg.append(f'<text x="{cx:.1f}" y="{base+20:.1f}" fill="{TXT}" font-size="12" text-anchor="middle">{esc(l1)}</text>')
        if l2: svg.append(f'<text x="{cx:.1f}" y="{base+36:.1f}" fill="{TXT}" font-size="12" text-anchor="middle">{esc(l2)}</text>')
    svg.append(f'<text x="{L}" y="{H-20}" fill="{MUT}" font-size="11.5">{esc(caption)}</text>')
    svg.append('</svg>')
    open(path,"w").write("\n".join(svg))
    print("wrote",path)

# Chart 1 — deterministic behavioral demonstration (reframed so higher = better)
chart("assets/benchmark-behavior.svg",
  "What Reality Check changes",
  "Deterministic demonstration · same model, both arms · rule-based grader · n=10 ideas",
  [("Avoids","empty praise"),("Names the","real flaw"),("States the","case against"),("Verdict matches","ground truth")],
  [("Without",GRAY,[0,0,0,0]),("With Reality Check",GREEN,[100,100,100,100])],
  "Higher is better. A behavioral demonstration that the ruleset induces these habits — not a cross-model efficacy claim.",
  legend=[("Without",GRAY),("With Reality Check",GREEN)])

# Chart 2 — maintainer-reported per-model scores
chart("assets/benchmark-models.svg",
  "Reported scores across model tiers",
  "Maintainer-reported testing · methodology pending documentation",
  [("Reasoning","(no plugin)"),("Flash","+ Reality Check"),("Opus 4.8","(no plugin)"),("Opus 4.8","+ Reality Check")],
  [("score",GRAY,[81.6,93.4,89.5,98.9])],
  "Maintainer-reported. Treat as the maintainer's own measurements until the method is documented in benchmarks/.",
  legend=[("Without plugin",GRAY),("With Reality Check",GREEN)],
  bar_colors=[GRAY,GREEN,GRAY,GREEN])
