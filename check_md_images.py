from pathlib import Path
import re
from urllib.parse import unquote

root = Path("student_handouts_md")
ok = True

for md in sorted(root.glob("*.md")):
    text = md.read_text(encoding="utf-8")
    links = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)

    for link in links:
        link = unquote(link.strip())

        if link.startswith("http://") or link.startswith("https://"):
            continue

        img_path = md.parent / link

        if not img_path.exists():
            ok = False
            print(f"BROKEN in {md.name}: {link}")

if ok:
    print("All Markdown image links are OK.")