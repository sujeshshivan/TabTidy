#!/usr/bin/env python3
"""Fail if the repository contains anything that looks like real mail data.

Run before every commit or pull request:
    python tools/check_no_personal_data.py

Flags:
  - email addresses whose domain is not a reserved example domain
    (example.com / example.org / *.example) or a known placeholder
  - files that look like scan output or decisions exported from the dashboard
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ALLOWED = re.compile(r"@([\w.-]+\.)?(example(\.com|\.org|\.net)?|example)$|@anthropic\.com$|@users\.noreply\.github\.com$", re.I)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
TEXT = {".md", ".html", ".json", ".py", ".txt", ".yml", ".yaml", ".csv", ".js", ".css"}
BAD_NAMES = re.compile(r"(scan|inbox-data|decisions|personal|private)[^/]*\.(json|html|csv)$", re.I)
SAFE_FILES = {"dashboard/sample-data.json"}

problems = []
for f in ROOT.rglob("*"):
    rel = f.relative_to(ROOT).as_posix()
    if rel.startswith(".git/") or not f.is_file():
        continue
    if BAD_NAMES.search(rel) and rel not in SAFE_FILES:
        problems.append(f"{rel}: file name looks like personal scan output")
    if f.suffix.lower() in TEXT:
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            for m in EMAIL.findall(line):
                if not ALLOWED.search(m):
                    problems.append(f"{rel}:{n}: real-looking email address {m}")

if problems:
    print("Possible personal data found:\n  " + "\n  ".join(problems))
    sys.exit(1)
print("OK: no personal data found.")
