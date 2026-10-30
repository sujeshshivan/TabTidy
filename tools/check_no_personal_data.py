#!/usr/bin/env python3
"""Fail if the repository contains anything that looks like real mail data.

Run before every commit or pull request:
    python tools/check_no_personal_data.py

Blocks:
  - addresses at personal mail providers (gmail.com, yahoo.com, outlook.com …)
  - other addresses, unless they're reserved examples (*.example, example.com)
    or a company's automated sender (noreply@, security@, alerts@ …)
  - files that look like scan output or exported decisions
  - phone-number-like and card-number-like digit runs in data files
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
PERSONAL_PROVIDERS = re.compile(
    r"@(gmail|googlemail|yahoo|ymail|hotmail|outlook|live|msn|icloud|me|mac|aol|proton|protonmail|pm|gmx|"
    r"mail|yandex|zoho|qq|163|126|rediffmail)\.(com|net|org|ch|me|de|ru|in|co\.uk|com\.my|co\.jp|fr)$", re.I)
EXAMPLE = re.compile(r"@([\w.-]+\.)?example(\.(com|org|net))?$", re.I)
SYSTEM_SENDER = re.compile(
    r"^(no-?reply|noreply[\w-]*|do-?not-?reply|security[\w-]*|account[\w-]*|registration|appleid|alerts?|"
    r"notifications?|jobs[\w-]*|jobalerts[\w-]*|billing|invoice|receipts?|support|info|hello|news)@", re.I)
OK_EXACT = {"noreply@anthropic.com", "noreply@users.noreply.github.com"}
TEXT = {".md", ".html", ".json", ".py", ".txt", ".yml", ".yaml", ".csv", ".js", ".gs", ".xml", ".css"}
BAD_NAMES = re.compile(r"(scan|inbox-data|decisions|personal|private|my-)[^/]*\.(json|html|csv|xml)$", re.I)
SAFE_FILES = {"dashboard/sample-data.json"}
DIGITS = re.compile(r"\b(?:\+?\d[\d -]{9,}\d)\b")

problems = []
for f in sorted(ROOT.rglob("*")):
    rel = f.relative_to(ROOT).as_posix()
    if rel.startswith(".git/") or not f.is_file():
        continue
    if BAD_NAMES.search(rel) and rel not in SAFE_FILES:
        problems.append(f"{rel}: file name looks like personal scan output")
    if f.suffix.lower() not in TEXT:
        continue
    for n, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        for addr in EMAIL.findall(line):
            a = addr.lower()
            if a in OK_EXACT or EXAMPLE.search(a):
                continue
            if PERSONAL_PROVIDERS.search(a):
                problems.append(f"{rel}:{n}: personal email address {addr}")
            elif not SYSTEM_SENDER.search(a):
                problems.append(f"{rel}:{n}: address that isn't an example or a company system sender: {addr}")
        if f.suffix.lower() in {".json", ".csv"} and DIGITS.search(line):
            problems.append(f"{rel}:{n}: long digit run (phone or card number?)")

if problems:
    print("Possible personal data found:\n  " + "\n  ".join(problems))
    sys.exit(1)
print("OK: no personal data found.")
