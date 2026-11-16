---
name: dashboard
description: Turn a grouped TabTidy Gmail scan into the interactive TabTidy triage dashboard (charts, top senders, security and bills, a decision dropdown per sender). Use when the user wants to see their inbox as a dashboard or review sender decisions visually.
---

# TabTidy step 3 · Build the dashboard 📊

**Changes Gmail: no.**

## Inputs

`tabtidy-scan.json` with `group` and `action` filled in (steps `scan` and `group`).
Format: `references/data-schema.md` (next to this file). Read it before you start.

## 1. Fill in the insights (optional, powers the charts)

Add an `insights` object as described in the schema. Every part is optional; a chart
without data hides itself.

- `weekly`: emails per 7-day window. Ids-only searches per window are cheap.
- `tabs`: how many emails would land in Primary / Updates / Promotions / Social / Forums
  under the group → tab table in `../group/references/classification-rules.md`.
- `new_senders_by_month`: senders seen for the first time each month.
- `security`: every login alert, code, "app given access", account change and
  verify-email message (search subjects). Per event: date, svc, kind, subject, and
  `flag: true` for new device, new country, phone number or password changes. Plus a
  per-service summary.
- `bills`: reuse `find-bills` output if you have it.

Tip: Gmail message ids start with the arrival time, so a date is
`int(id, 16) >> 20` milliseconds since 1970. No need to open each email.

## 2. Build the page

The template is `assets/template.html` (next to this file). It contains the placeholder
`/*DATA*/` inside a `<script type="application/json">` tag.

- **If you can publish an Artifact** (claude.ai, Cowork, Claude Code with artifacts):
  replace `/*DATA*/` with the JSON (escape every `</` as `<\/`), publish it as an
  artifact, and if the artifact can keep a database, store the user's decisions in a
  collection called `decisions` (one document per sender: `email`, `action`, `updated`).
- **If you can run Python**: run
  `python3 scripts/build_dashboard.py tabtidy-scan.json -o tabtidy-dashboard.html`
  from this skill's folder (pass absolute paths), then give the user the HTML file.
  Decisions are kept in their browser; the **Copy decisions** button hands them back.
- **Otherwise**: do the replacement yourself and save `tabtidy-dashboard.html`.

Never commit the filled-in dashboard or the scan file to git: they contain mail data.

## What the user gets

Headline numbers, emails per week, per tab, per group and per month, top 15 senders,
new senders per month, logins & security per service with risky alerts flagged, bills
with payment problems in red, quick wins, a searchable sender table with a decision
dropdown each, and a **Copy Gmail search** button per action.

Tell the user to change any suggestion they disagree with, then come back for `decide`.
