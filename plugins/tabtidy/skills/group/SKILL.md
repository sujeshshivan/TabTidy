---
name: group
description: Put every Gmail sender from a TabTidy scan into one group (security, bills, orders, newsletters, social, promotions, suspicious…) with one suggested action each. Use after a scan, or when the user asks which senders are junk or what to do with each sender.
---

# TabTidy step 2 · Group the senders 🗂️

**Changes Gmail: no.**

One decision per **sender**, not per email. A few dozen decisions instead of thousands.

## Inputs

`tabtidy-scan.json` from the `scan` step. If it doesn't exist, run the `scan` skill first.

## Recipe

1. Read the full rulebook in `references/classification-rules.md` (next to this file).
2. Put every sender into exactly **one** group:
   `security, action, official, people, bills, subscriptions, orders, travel, jobs,
   newsletters, notices, social, promotions, suspicious, review`.
3. Watch out for the two traps:
   - Some senders send **both** ads and bills (a design app sends promos *and*
     "payment failed"). Group those by **subject**, not by sender: split them into two
     entries if needed.
   - Social networks send security alerts from **separate addresses** (`security@…`,
     `registration@…`). Those go to `security`, not `social`.
4. Suggest ONE action per sender: `keep | label | archive | unsubscribe | delete | spam`,
   with a one-line `reason`.
5. Rules:
   - Never suggest removing `security`, `action`, `official` or `people` mail.
   - `suspicious` gets `spam`, never `unsubscribe`.
   - Unsure? Put it in `review` with action `label`.
6. Write `group`, `action` and `reason` back into `tabtidy-scan.json`.

## Report to the user

A table: group → senders → conversations, busiest groups first. Point out the "quick
wins": the 5 busiest senders suggested for unsubscribe or delete.

Then offer `find-bills` (to see money mail on its own) or `dashboard`.
