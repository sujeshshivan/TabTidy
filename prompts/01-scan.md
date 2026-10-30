# 01 · Scan the inbox 🔍

> **Changes Gmail?** No. Look, don't touch.
> **Time:** 2–5 minutes, depending on inbox size.

Claude reads *who* sends you mail and *how often*. It doesn't open message bodies.

## Prompt

```
Scan my Gmail for the last 6 months. READ-ONLY: don't label, move, archive,
trash or change anything.

How to scan without missing mail:
- Exclude sent mail (-in:sent).
- Search in date windows small enough that each returns fewer than 50
  conversations (half-months usually work). If a window hits 50, split it.
- Use the metadata-only view to collect the sender of every conversation.
- Get these totals with count-only queries:
  is:unread, category:promotions, category:social, category:updates.
- Then search subjects for money mail that hides among other senders:
  subject:(receipt OR invoice OR "payment failed" OR subscription OR
  renewal OR "order confirmation").

Count conversations per sender per month and save the counts to a file
before doing anything else.

Then tell me: total conversations, unique senders, how many are unread,
the top 10 senders, and any bills or payment problems you spotted.
```

## What to check

- 👀 Does the top 10 match the clutter you see every day?
- 💸 Any **payment failed** or **action required** emails in the list? Deal with those first.
- 🔢 Is the total close to Gmail's own count for the same date range? If not, ask Claude to re-split the windows that came back with exactly 50.
