---
name: tidy-inbox
description: Run the full TabTidy Gmail clean-up end to end (scan, group, dashboard, decide, sort into tabs, unsubscribe, delete junk, filters, keep clean). Use when the user asks to clean up, tidy, organise or declutter their Gmail or inbox.
---

# TabTidy: tidy my inbox

You are guiding the user through a full, safe Gmail clean-up with the Gmail connector.
The core idea: **decide once per sender, not once per email.** An inbox with thousands of
emails usually has only a few dozen senders, and a handful of them send most of it.

## Before anything else

1. Check that Gmail tools are available (a tool that searches threads, one that labels
   threads, one that trashes threads). If they are not, stop and tell the user:
   "Connect Gmail first: Settings → Connectors → Gmail → Connect, then start a new chat."
2. Tell the user the plan in three lines: steps 1–4 only look, steps 5–7 change Gmail in
   small confirmed batches, steps 8–9 keep it clean.

## The steps

Run them in order. Each step has its own skill in this plugin with the detailed recipe;
follow that skill's instructions when you reach the step.

| # | Step | Skill | Changes Gmail? |
|---|---|---|---|
| 1 | Scan who sends what | `scan` | No |
| 2 | Group senders, suggest an action each | `group` | No |
| 2b | Pull out bills and payment problems | `find-bills` | No |
| 3 | Build the dashboard | `dashboard` | No |
| 4 | Lock in decisions | `decide` | No |
| 5 | Sort into tabs and labels | `sort-into-tabs` | Labels and tabs only |
| 6 | List unsubscribe links | `unsubscribe` | No (the user clicks) |
| 7 | Move junk to Trash | `delete-junk` (user runs `/tabtidy:delete-junk`) | Trash only, undo-able 30 days |
| 8 | Gmail filters for the future | `filters` | Only after the user imports a file |
| 9 | Weekly check or TabTidy script | `keep-clean` | Labels and tabs only |

After each step, stop, show the result, and ask whether to go on. The user may skip
the dashboard (go from 2 straight to 4 with a table in chat) or stop after any step.

## Working state

Keep the scan and the decisions in files so later steps (and later chats) can reuse them:

- `tabtidy-scan.json`: the scan in the format of `dashboard/references/data-schema.md`.
- `tabtidy-decisions.json`: the final decision per sender.

Save them in the current working folder (in Cowork, the outputs folder). These files hold
the user's mail data: never commit them to git and never send them anywhere.

## Golden rules (apply to every step)

1. **Look before you touch.** Scan, group, decide, *then* act.
2. **Small batch first.** One sender, at most 20 conversations, then wait for "OK".
3. **Never remove** security, login/OTP, payment-problem, government or people mail.
4. **Trash only.** Never empty Trash, never delete permanently.
5. **Never click links** (unsubscribe or otherwise). The user clicks.
6. **Suspicious senders** get "mark as spam", never "unsubscribe".
7. **Don't send, reply or forward** any email.
