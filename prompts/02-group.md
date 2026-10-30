# 02 · Group the senders

**Changes your mailbox:** No.

## Prompt

```
Using the scan counts, put every sender into exactly one group:

- promotions     shops, marketplaces, product marketing, onboarding drips
- newsletters    digests, blogs, product-update newsletters
- social         Facebook, Instagram, LinkedIn and similar notifications
- transactional  KEEP: receipts, bills, bank alerts, OTPs, security alerts
- service        account notices, policy updates, welcome emails
- suspicious     odd or look-alike domains, prize bait, unexpected attachments
- people         real people writing to me
- review         anything you are not sure about, or mail addressed to
                 another address that still reaches me

For each sender suggest ONE action:
unsubscribe | archive | label | keep | spam

Rules:
- Never suggest removing security alerts, banks, government, utilities,
  receipts or OTPs.
- Suspicious senders get "spam", never "unsubscribe".
- When unsure, use group "review" and action "keep".
- Give a one-line reason per sender.

Still read-only. Show me a table of group → number of senders → emails.
```

See [`docs/classification-rules.md`](../docs/classification-rules.md) for the reasoning behind each group.
