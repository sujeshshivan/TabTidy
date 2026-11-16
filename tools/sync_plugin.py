#!/usr/bin/env python3
"""Copy the shared TabTidy files into the Claude plugin, or check they match.

    python tools/sync_plugin.py           # copy repo files into plugins/tabtidy
    python tools/sync_plugin.py --check   # fail if the plugin copies are out of date (CI)

The plugin is installed on its own (only plugins/tabtidy is copied to the user's
machine), so it carries its own copies of the dashboard template, rulebook, data
format, filter files and the Apps Script. Edit the originals, then run this.
"""
import pathlib, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "tabtidy" / "skills"
COPIES = {
    "dashboard/template.html": "dashboard/assets/template.html",
    "tools/build_dashboard.py": "dashboard/scripts/build_dashboard.py",
    "docs/data-schema.md": "dashboard/references/data-schema.md",
    "docs/classification-rules.md": "group/references/classification-rules.md",
    "filters/primary-essentials.xml": "filters/assets/primary-essentials.xml",
    "filters/labels.xml": "filters/assets/labels.xml",
    "filters/build_filters.py": "filters/assets/build_filters.py",
    "apps-script/TabTidy.gs": "keep-clean/assets/TabTidy.gs",
}


def expected(src: str) -> bytes:
    data = (ROOT / src).read_bytes()
    if src == "tools/build_dashboard.py":
        # Inside the plugin the template sits at ../assets/template.html.
        data = data.replace(
            b'(ROOT / "dashboard" / "template.html")',
            b'(pathlib.Path(__file__).resolve().parent.parent / "assets" / "template.html")',
        )
    return data


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for src, dst in COPIES.items():
        want, out = expected(src), SKILLS / dst
        if out.exists() and out.read_bytes() == want:
            continue
        if check:
            stale.append(f"plugins/tabtidy/skills/{dst} (from {src})")
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(want)
            print(f"updated plugins/tabtidy/skills/{dst}")
    if stale:
        print("Plugin copies are out of date. Run: python tools/sync_plugin.py\n  " + "\n  ".join(stale))
        return 1
    print("OK: plugin files are in sync." if check else "Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
