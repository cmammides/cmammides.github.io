# Post-render: give the homepage its own browser/search title (Quarto otherwise appends the site title).
import os, re
p = os.path.join("_site", "index.html")
if os.path.exists(p):
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"<title>.*?</title>", "<title>Christos Mammides | Conservation Scientist</title>", s, count=1, flags=re.S)
    open(p, "w", encoding="utf-8").write(s)
