# Post-render: tidy page titles.
# Homepage gets its own title; other pages use "Page | Christos Mammides" (Quarto default is "Page – Christos Mammides").
import glob, re
for p in glob.glob("_site/*.html"):
    s = open(p, encoding="utf-8").read()
    if p.endswith("/index.html"):
        s = re.sub(r"<title>.*?</title>", "<title>Christos Mammides | Conservation Scientist</title>", s, count=1, flags=re.S)
    else:
        s = s.replace(" – Christos Mammides", " | Christos Mammides")
    open(p, "w", encoding="utf-8").write(s)
