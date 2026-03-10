#!/usr/bin/env python3
"""
generate_cv.py
Extracts the #cv, #publications, and #about sections from index.html
and assembles a print-ready cv.html in the same visual style.
"""

from pathlib import Path

from bs4 import BeautifulSoup

# ── Load source ────────────────────────────────────────────────────────────────
src = Path("index.html").read_text(encoding="utf-8")
soup = BeautifulSoup(src, "lxml")


# ── Helper: extract inner HTML of a section by id ─────────────────────────────
def section_inner(section_id):
    sec = soup.find(id=section_id)
    if not sec:
        raise ValueError(f"Section #{section_id} not found in index.html")
    container = sec.find(class_="container") or sec
    return container


# ── Pull data from index.html ──────────────────────────────────────────────────
about = section_inner("about")
cv = section_inner("cv")
pubs = section_inner("publications")
research = section_inner("research")

# Name & role
name_tag = about.find("h1")
name = name_tag.get_text(strip=True) if name_tag else "Prénom Nom"

role_tag = about.find(class_="hero-role")
role = role_tag.get_text(strip=True, separator="<br>") if role_tag else ""

bio_tag = " ".join(map(str, list(about.find_all(class_="hero-bio"))))
# bio = bio_tag.get_text(strip=True) if bio_tag else ""


# # Contact links (nav hero-links buttons)
# hero_links = about.find(class_="hero-links")
# contact_items = []
# if hero_links:
#     for a in hero_links.find_all("a"):
#         href = a.get("href", "#")
#         label = a.get_text(strip=True)
#         if href and href != "#" and label.lower() not in ("cv",):
#             contact_items.append((label, href))


# ── Rebuild the cv section markup (strip section-label, keep tl + skills) ─────
def clean_section(container):
    """Return inner HTML of container, removing .section-label divs."""
    clone = BeautifulSoup(str(container), "lxml").body
    for label in clone.find_all(class_="section-label"):
        label.decompose()
    # unwrap outer container div
    inner = clone.find(class_="container") or clone
    return inner.decode_contents()


cv_html = clean_section(cv)
pub_html = clean_section(pubs)
res_html = clean_section(research)

# # ── Build contact line ─────────────────────────────────────────────────────────
# contact_html = "\n".join(
#     f'<a href="{href}">{label}</a>' for label, href in contact_items
# )

# ── Assemble cv.html ───────────────────────────────────────────────────────────
output = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>CV — {name}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Serif:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Sans:wght@300;400;500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="cv_style.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
</head>
<body>

<div class="screen-bar">
  <button class="dl-btn primary" onclick="window.print()">⬇ Save as PDF</button>
  <a href="index.html" class="dl-btn">← Back to website</a>
</div>

<div class="page">

  <header>
    <h1>{name}</h1>
    <div class="h-role">{role}</div>
    <div class="h-contacts">
    <span><i class="fa-solid fa-location-dot"></i> Toulouse, France</span>
      <a href="mailto:florian.grivet@cnes.fr"><i class="fa-solid fa-envelope"></i> florian.grivet@cnes.fr</a>
      <a href="https://github.com/fgrivet" target="_blank"><i class="fa-brands fa-github"></i> github.com/fgrivet</a>
      <a href="https://scholar.google.com/citations?user=eT-QkogAAAAJ&hl=fr&oi=ao" target="_blank"><i class="fa-brands fa-google-scholar"></i> Google Scholar</a>
      <a href="https://orcid.org/0009-0007-7096-3258" class="btn btn-ghost" target="_blank"><i class="fa-brands fa-orcid"></i> orcid.org/0009-0007-7096-3258</a>
      <a href="https://linkedin.com/in/floriangrivet" target="_blank"><i class="fa-brands fa-linkedin"></i> linkedin.com/in/floriangrivet</a>
    </div>
    <img src="profile_picture.jpg" alt="Florian Grivet" class="cv-avatar">
  </header>



  <div class="sec-title">About Me</div>
    {bio_tag}

  <div class="sec-title">Research Interests</div>
  {res_html}

  <div class="sec-title">Publications</div>
  {pub_html}

  <div class="sec-title">Education & Experience</div>
  {cv_html}


</div>
</body>
</html>
"""

Path("cv.html").write_text(output, encoding="utf-8")
print("cv.html generated successfully.")
