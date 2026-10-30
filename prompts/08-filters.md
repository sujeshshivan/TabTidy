# 08 · Make it automatic: Gmail filters ⚙️

> **Changes Gmail?** Only after **you** import a file. The Gmail connector can't create filters.

Steps 05–07 cleaned the past. Filters handle the future, the moment mail arrives.

## Option A: use this project's ready-made files

[`filters/primary-essentials.xml`](../filters/primary-essentials.xml) and [`filters/labels.xml`](../filters/labels.xml). Import steps are in [docs/path-2-script-and-filters.md](../docs/path-2-script-and-filters.md#part-b--gmail-filters-xml).

## Option B: let Claude add your own senders

```
Here is this project's filters/build_filters.py (attached). Add the senders
from my decisions to the right lists (shops to SHOPS, banks to BANKS, and
so on) and give me two files:
- primary-essentials.xml: security, action required, government, flight
  changes → label + Categorize as Primary + always important + never spam
- labels.xml: everything else → label ONLY (no "Categorize as")
Keep every filter's search under 1,450 characters.
```

## ⚠️ Lesson learned: tabs in filter files

When importing, Gmail accepted **"Categorize as Primary"** but rejected **"Categorize as Promotions / Social / Updates / Forums"** with "Could not create". That's why `labels.xml` only adds labels.

To also move mail between tabs automatically, use the script ([Path 2](../docs/path-2-script-and-filters.md)), or drag one email to a tab in Gmail and click **Yes** when it asks about future messages from that sender.
