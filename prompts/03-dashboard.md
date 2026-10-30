# 03 · Build the dashboard

**Changes your mailbox:** No.

## Prompt

```
Turn the grouped scan into a JSON file in the format described in this
project's docs/data-schema.md (paste that file into the chat)
(meta + senders, with by_month counts, group, action, reason and one
sample_subject per sender).

Then build the dashboard from this project's dashboard/template.html
(paste or attach it) by putting
the JSON where the template says /*DATA*/, and publish it as an artifact so I
can keep it. If the db capability is available, save my decisions there
(collection "decisions", one document per sender: {email, action, updated})
so you can read them back later.
```

## Without Claude artifacts

Ask Claude for the JSON file only, then build a local copy yourself:

```bash
python tools/build_dashboard.py my-scan.json -o my-dashboard.html
```

Open `my-dashboard.html` in a browser. Decisions are kept in that browser.
