---
name: find-bills
description: Find bills, receipts, invoices, subscription renewals and payment problems ("payment failed", "overdue", "action required") in the user's Gmail, read-only. Use when the user asks to find bills, payments, receipts, subscriptions or missed payment emails.
---

# TabTidy · Find bills and payment problems 💸

**Changes Gmail: no.**

Money mail hides among ad senders: the same company sends "50% off" and "your payment
failed". So search by **subject words**, not just by sender.

## Recipe

Default range: the last 12 months, unless the user says otherwise. Exclude `-in:sent`.
Use the thread search tool with the minimal view (subject, sender, date) and page
through all results.

1. **Problems first** (`kind: problem`):
   `subject:("payment failed" OR "payment declined" OR "failed to process" OR "update your payment" OR "past due" OR overdue OR "final notice" OR "action required" OR "account suspended")`
2. **Plans and renewals** (`kind: plan`):
   `subject:(subscription OR renewal OR "auto-renew" OR "your plan" OR "trial ends" OR "trial ending" OR "has ended" OR cancellation OR membership)`
3. **Receipts and statements** (`kind: receipt`):
   `subject:(receipt OR invoice OR "payment received" OR "payment successful" OR "payment confirmation" OR "e-statement" OR "your bill" OR "bill is ready" OR refund)`
4. De-duplicate by thread. For each item keep: date, service (brand), kind, subject,
   and the thread's `viewUrl`.
5. If `tabtidy-scan.json` exists, store the list under `insights.bills` (see
   `../dashboard/references/data-schema.md`).

## Report to the user

1. **⚠️ Needs action now**: every `problem`, newest first, with a link to open it.
   Say plainly whether the latest email for that service still looks unresolved.
2. **🔁 Subscriptions you're paying for**: one line per service with the latest plan or
   renewal email and its date. Flag ones that look forgotten (renewals but no other mail).
3. **🧾 Receipts**: count per service, last 3 months in detail.

Offer to label them **Bills & Receipts** (the `sort-into-tabs` step) so they're easy to find.
Do not open payment links or log in anywhere for the user.
