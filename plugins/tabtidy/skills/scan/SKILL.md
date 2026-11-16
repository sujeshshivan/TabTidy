---
name: scan
description: Read-only scan of the user's Gmail that counts conversations per sender per month, unread totals and tab totals, and spots bills. Use when the user asks who fills their inbox, wants an inbox scan or overview, or starts a TabTidy clean-up.
---

# TabTidy step 1 · Scan the inbox 🔍

**Changes Gmail: no.** Do not label, move, archive, trash or mark anything in this step.

You read *who* sends mail and *how often*. You don't open message bodies.

## Inputs

- Range: default the last 6 months. Use what the user asks for if they say otherwise.

## Recipe

1. Exclude sent mail: add `-in:sent` to every query.
2. Search in **date windows** small enough that each returns fewer than 50 conversations
   (half-months usually work; busy inboxes may need weeks). Use the thread search tool
   with `pageSize: 50` and the metadata-only view, and follow `pageToken` if it is
   returned. **If a window returns exactly 50 with no further page, split it** or you
   will miss mail.
   - `after:` is inclusive and `before:` is exclusive, both at midnight. Windows like
     `after:2026/05/01 before:2026/05/16` then `after:2026/05/16 before:2026/06/01` cover
     every day once.
3. For every conversation, record the sender address, the brand (display name) and the
   month. Keep one `sample_subject` per sender (use the minimal view for one search per
   sender if needed).
4. Get these totals with ids-only searches (count the ids, following pages):
   `is:unread`, `category:promotions`, `category:social`, `category:updates`,
   `category:forums`, `category:primary`, each with the same date range and `-in:sent`.
5. Search subjects for money mail that hides among other senders:
   `subject:(receipt OR invoice OR "payment failed" OR subscription OR renewal OR "order confirmation")`.
6. **Save the counts to `tabtidy-scan.json` before doing anything else**, using the
   `meta` and `senders` shape from `../dashboard/references/data-schema.md`
   (leave `group` and `action` empty until step 2).

## Report to the user

- Total conversations, unique senders, how many are unread (and %).
- The top 10 senders with counts.
- Any **payment failed / action required** emails spotted. Say these should be dealt with first.
- Ask them to compare the total with Gmail's own count for the range. If it is far off,
  re-split windows that came back with exactly 50.

Then offer step 2 (`group`).
