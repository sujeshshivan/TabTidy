---
name: keep-clean
description: Keep a TabTidy-cleaned Gmail tidy, with a weekly Claude check of new mail and new senders, or by installing the TabTidy Apps Script that sorts every new email on a schedule. Use when the user wants their inbox to stay clean, or asks for a weekly inbox check.
---

# TabTidy step 9 · Keep it clean 🧹

Offer both options and let the user pick (doing both is fine).

## Option A: weekly check with Claude

If you can create a scheduled task, set one up for **every Sunday morning** (user's
local time) with this prompt; otherwise give the user the prompt to run each week.

```
TabTidy weekly check. Scan the last 7 days of my Gmail (read-only first, -in:sent).
- For senders already in tabtidy-decisions.json: apply their label and tab
  (labels and CATEGORY_ tabs only; keep everything in the inbox).
- List NEW senders with 3+ emails this week, each with a suggested group and action.
- List anything that landed in Primary but looks like an ad or newsletter.
- List any payment problems or security alerts from the week.
Do not delete, archive, mark spam or unsubscribe without asking me.
```

## Option B: TabTidy script (no Claude needed)

Runs inside the user's own Google account on a schedule. It only adds labels and moves
mail between tabs; it never deletes, archives, replies, forwards or reads bodies. The
script is `assets/TabTidy.gs` next to this file. Walk the user through:

1. Gmail → ⚙ → **See all settings** → **Inbox** → tick all five categories → **Save**.
2. Open **script.google.com** → **New project**.
3. Delete the sample code and paste all of `TabTidy.gs` (give them the file).
4. Rename the project **TabTidy** and save (Ctrl+S / ⌘S).
5. Left sidebar: **Services ➕ → Gmail API → Add**.
6. Pick **`preview`** → **▶ Run** → approve access. Google shows "Google hasn't verified
   this app" for personal scripts: **Advanced → Go to TabTidy (unsafe)** → **Allow**.
   The log shows where the latest 30 emails *would* go; nothing changes.
7. Pick **`setup`** → **▶ Run**. Creates labels, sorts recent mail, starts the schedule.
8. Optional: **`sortWholeInbox`** → **▶ Run** for older mail.

To stop it: run `stop`, then remove access in Google Account → Security → Third-party apps.
Full guide: https://github.com/sujeshshivan/TabTidy/blob/main/docs/path-2-script-and-filters.md
