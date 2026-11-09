import glob, os, re
DESC = {
    "research.html": "Research by Christos Mammides on protected areas and landscape ecology, soundscape ecology, computational methods in ecology, and conservation policy.",
    "publications.html": "Peer-reviewed publications by Christos Mammides on protected areas, human pressures on biodiversity, acoustic monitoring, and conservation policy.",
    "media-policy.html": "Media coverage and policy citations of research by Christos Mammides and collaborators.",
    "grants.html": "Research grants and awards received by Christos Mammides.",
    "cv.html": "Curriculum vitae of Christos Mammides: positions, education, academic service, invited talks, and teaching.",
}
for p in glob.glob("_site/*.html"):
    s = open(p, encoding="utf-8").read()
    if p.endswith("/index.html"):
        s = re.sub(r"<title>.*?</title>", "<title>Christos Mammides | Conservation Scientist</title>", s, count=1, flags=re.S)
    else:
        s = s.replace(" – Christos Mammides", " | Christos Mammides")
    d = DESC.get(os.path.basename(p))
    if d and 'name="description"' not in s:
        s = s.replace("</title>", '</title>\n<meta name="description" content="%s">' % d, 1)
    open(p, "w", encoding="utf-8").write(s)
