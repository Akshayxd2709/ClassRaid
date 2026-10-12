#!/usr/bin/env python3
"""Fast static acceptance checks for a ClassRaid-style frontend."""
from pathlib import Path
import re
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
public = root / "public"
required = [public / "index.html", public / "manus-routes.json", public / "static" / "mock.js", public / "static" / "battle.js", public / "static" / "style.css"]
missing = [str(p) for p in required if not p.is_file()]
if missing:
    raise SystemExit("missing: " + ", ".join(missing))

for path in [public / "static" / "mock.js", public / "static" / "battle.js"]:
    result = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)
    if result.returncode:
        raise SystemExit(result.stderr)

html = (public / "index.html").read_text()
checks = ["#/student", "#/teacher", "cdn.socket.io/4.7.5/socket.io.min.js", "localStorage", "boss-select", "result-list", "WARRIOR STRIKE", "BOSS SLAIN"]
for marker in checks:
    if marker not in html and marker not in (public / "static" / "battle.js").read_text():
        raise SystemExit(f"missing marker: {marker}")

scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
for index, source in enumerate(scripts):
    temp = Path("/tmp") / f"classraid-inline-{index}.js"
    temp.write_text(source)
    result = subprocess.run(["node", "--check", str(temp)], capture_output=True, text=True)
    if result.returncode:
        raise SystemExit(result.stderr)

if '"routes"' not in (public / "manus-routes.json").read_text():
    raise SystemExit("route manifest missing routes")
print("ClassRaid static validation passed")
