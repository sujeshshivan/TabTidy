# 02 · Group the senders 🗂️

> **Changes Gmail?** No.

One decision per **sender**, not per email. A few dozen decisions instead of a few thousand.

## Prompt

```
Using the scan, put every sender into exactly one group:

- security       login codes, OTP, security alerts, "new sign-in"   → KEEP
- action         "payment failed", "action required", overdue       → KEEP
- official       government, tax, pension                           → KEEP
- people         real people writing to me                          → KEEP
- bills          receipts, invoices, bank and utility statements
- subscriptions  plan started, ended, renewing, trial ending
- orders         shipped, out for delivery, tracking
- travel         bookings, e-tickets, itineraries
- jobs           job alerts, applications
- newsletters    digests and newsletters I signed up for
- notices        app, cloud, policy and terms updates
- social         social network notifications
- promotions     ads, sales, "we miss you" emails
- suspicious     look-alike brands, prize bait, odd domains
- review         anything you're unsure about

Watch out:
- Some senders send BOTH ads and bills (e.g. a design app sends promos AND
  "payment failed"). Group those by subject, not by sender.
- Social networks send security alerts from separate addresses
  (e.g. security@…). Those go to "security", not "social".

For each sender suggest ONE action:
keep | label | archive | unsubscribe | delete | spam

Rules: never suggest removing security, action, official or people mail.
Suspicious senders get "spam", never "unsubscribe".

Still read-only. Show me a table: group → senders → conversations.
```

See [`docs/classification-rules.md`](../docs/classification-rules.md) for the full rulebook.
