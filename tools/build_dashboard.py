#!/usr/bin/env python3
"""Build a self-contained dashboard HTML from a scan JSON file.

Usage:
    python tools/build_dashboard.py my-scan.json -o my-dashboard.html

With no arguments it rebuilds dashboard/index.html from dashboard/sample-data.json.
The output opens in any browser, needs no server, and keeps your decisions in
that browser's local storage. Keep your own scan files out of git (see .gitignore).
"""
import argparse, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
HEAD = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '</head><body>\n')
TAIL = '\n</body></html>\n'

def build(src: pathlib.Path, out: pathlib.Path) -> None:
    data = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(data.get("senders"), list):
        raise SystemExit(f"{src}: missing a 'senders' list (see docs/data-schema.md)")
    template = (ROOT / "dashboard" / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out.write_text(HEAD + template.replace("/*DATA*/", payload) + TAIL, encoding="utf-8")
    print(f"Wrote {out} ({len(data['senders'])} senders)")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("scan", nargs="?", default=str(ROOT / "dashboard" / "sample-data.json"))
    p.add_argument("-o", "--out", default=str(ROOT / "dashboard" / "index.html"))
    a = p.parse_args()
    build(pathlib.Path(a.scan), pathlib.Path(a.out))
