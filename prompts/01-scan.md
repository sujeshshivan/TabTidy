# 01 · Scan the inbox (read-only)

**Needs:** Gmail connected to Claude (Settings → Connectors → Gmail).
**Changes your mailbox:** No.

## Prompt

```
Scan my Gmail for the last 6 months (today back to the same date 6 months ago).
This is READ-ONLY: do not label, archive, trash, mark or change anything.

How to scan without missing mail:
- Exclude sent mail (-in:sent).
- Search in date windows small enough that each returns fewer than 50 threads
  (half-months usually work). If a window reports more, split it again.
- Use the metadata-only view to collect the sender of every thread.
- Get the unread total with one count query (is:unread) and the Gmail tab
  totals with count queries (category:promotions, social, updates, primary).
- Fetch subject lines only for the busiest senders, so each has one example.

Count threads per sender per month. Save the raw counts to a file before
doing anything else, then tell me: total threads, unique senders, unread
total, and the top 10 senders by volume.
```

## What to check

- Does the top-10 list match what you feel is cluttering your inbox?
- Is the total close to Gmail's own estimate for the same search? If not, ask Claude to re-split the windows that were cut off at 50.
