# 03 · Build the dashboard 📊

> **Changes Gmail?** No.

Turns the scan into a page you can actually look at: where the mail comes from, what's growing, and one decision dropdown per sender.

## Prompt (Claude builds and publishes it for you)

```
Export the grouped scan as JSON in the format from this project's
docs/data-schema.md (I'll paste it below), with:
- meta: range, scan date, totals, months
- senders: email, brand, count, by_month, group, action, reason,
  and one sample_subject each

Then build the dashboard from this project's dashboard/template.html
(attached) by putting the JSON where the template says /*DATA*/, and
publish it as an artifact I can keep.

If the artifact can store data, save my decisions in a collection called
"decisions" (one document per sender: email, action, updated) so you can
read them back later.

<paste docs/data-schema.md here and attach dashboard/template.html>
```

## Prompt (you want the data file only)

```
Export the grouped scan as a JSON file in the format from
docs/data-schema.md and send me the file.
```

Then build a local dashboard:

```bash
python tools/build_dashboard.py my-scan.json -o my-dashboard.html
```

Open `my-dashboard.html` in any browser. Decisions are saved in that browser.
**Never commit `my-*.json` or `my-*.html`.** They contain your mail data, and `.gitignore` already blocks them.

## What you get

- 📈 Headline numbers: emails, senders, % unread, % from real people, how much your plan cuts
- 🍩 Emails per group (click to filter) and per month
- 🏆 Quick wins: the busiest senders to unsubscribe from
- 🎛️ A searchable sender table with a decision dropdown each
- 📋 An action plan with a **Copy Gmail search** button per action, plus your decisions as JSON to hand back to Claude
