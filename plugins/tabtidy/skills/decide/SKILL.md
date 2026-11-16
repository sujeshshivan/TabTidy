---
name: decide
description: Collect the user's final keep/label/archive/unsubscribe/delete/spam decision per Gmail sender from the TabTidy dashboard or chat, and save them. Use after the dashboard, or when the user says their decisions are ready.
---

# TabTidy step 4 · Lock in decisions ✅

**Changes Gmail: no.**

## Where decisions come from

- **Dashboard artifact with a database**: read the `decisions` collection. It only holds
  senders the user changed; everyone else keeps the suggested `action` from the scan.
- **Local dashboard**: the user pastes the output of **Copy decisions** (or attaches
  `decisions.json`). Its shape is in `../dashboard/references/data-schema.md`.
- **No dashboard**: show the grouped table from `group` and let the user change actions
  in chat ("unsubscribe from all promotions except Shop X").

## Recipe

1. Merge: suggested action from `tabtidy-scan.json`, overridden by the user's changes.
2. Re-apply the safety rules and **warn** (don't silently change) if the user picked
   delete/unsubscribe for `security`, `action`, `official` or `people` senders, or
   unsubscribe for `suspicious` ones.
3. Save the result to `tabtidy-decisions.json`:
   `{ "decided_on": "YYYY-MM-DD", "decisions": { "<action>": [{ "email", "brand", "group", "emails" }] } }`
4. Show the final list grouped by action (keep / label / archive / unsubscribe /
   delete / spam) with sender and email count, and totals per action.

**Don't do anything in Gmail yet.** Offer the next steps: `sort-into-tabs`,
`unsubscribe`, and `/tabtidy:delete-junk`.
