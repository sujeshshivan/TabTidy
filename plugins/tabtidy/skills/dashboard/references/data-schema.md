# Scan data format

The dashboard reads one JSON object with two keys: `meta` and `senders`. A complete example is in [`dashboard/sample-data.json`](../dashboard/sample-data.json).

```json
{
  "meta": {
    "label": "you@example.com",
    "range_from": "2026-05-01",
    "range_to": "2026-10-31",
    "scanned_on": "2026-10-31",
    "total_threads": 335,
    "unread_threads": 278,
    "months": ["2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10"],
    "gmail_tabs": { "Promotions": 180, "Updates": 61, "Social": 64, "Primary": 21 },
    "notes": "Thread counts, read-only scan. Sent mail excluded.",
    "sample": false
  },
  "senders": [
    {
      "email": "news@vendor.example",
      "domain": "vendor.example",
      "brand": "Vendor",
      "count": 32,
      "by_month": [5, 6, 7, 5, 6, 3],
      "group": "promotions",
      "action": "unsubscribe",
      "reason": "Product marketing.",
      "sample_subject": "New features are here"
    }
  ]
}
```

## `meta`

| Field | Required | Meaning |
|---|---|---|
| `label` | no | Shown in the header, usually the account. |
| `range_from`, `range_to` | no | Scan window, `YYYY-MM-DD`. |
| `scanned_on` | no | Date of the scan. |
| `total_threads` | no | Total threads scanned. |
| `unread_threads` | no | Enables the "Never opened" figure. Omit if unknown. |
| `months` | no | `YYYY-MM` labels, same order as every `by_month` array. Enables the monthly chart and sparklines. |
| `gmail_tabs` | no | Gmail's own tab counts, shown in the footer. |
| `notes` | no | Footer text. |
| `sample` | no | `true` marks the data as an example in the header. |

## `senders[]`

| Field | Required | Meaning |
|---|---|---|
| `email` | yes | Sender address. Also the key decisions are saved under. |
| `brand` | yes | Human name for the sender. |
| `count` | yes | Threads from this sender in the window. |
| `group` | yes | One of `security`, `action`, `official`, `people`, `bills`, `subscriptions`, `orders`, `travel`, `jobs`, `newsletters`, `notices`, `social`, `promotions`, `suspicious`, `review`. See [classification-rules.md](classification-rules.md). |
| `action` | yes | Suggested action: `keep`, `label`, `archive`, `unsubscribe`, `delete`, `spam`. |
| `domain` | no | Sender domain. |
| `by_month` | no | Counts per month, aligned with `meta.months`. |
| `reason` | no | One line explaining the suggestion. |
| `sample_subject` | no | One real subject line. |

## `insights` (optional: powers the charts)

Every part is optional. A chart section without its data hides itself.

```json
"insights": {
  "weekly_note": "Mail still in your mailbox, per week.",
  "weekly": [{ "week": "2026-05-01", "count": 11 }],
  "tabs": { "Primary": 38, "Updates": 69, "Promotions": 169, "Social": 60, "Forums": 7 },
  "new_senders_by_month": [9, 2, 1, 1, 1, 1],
  "security": {
    "services": [{ "svc": "Example Mail", "login": 4, "code": 2, "access": 3, "change": 1, "verify": 0,
                   "total": 10, "latest": "2026-10-28" }],
    "events": [{ "date": "2026-09-14", "svc": "FriendSpace", "kind": "login",
                 "subject": "Did you just log in from a new country?", "flag": true }]
  },
  "bills": [{ "date": "2026-09-26", "svc": "PixelStudio", "kind": "problem",
              "subject": "Payment failed: update your card" }]
}
```

| Field | Meaning |
|---|---|
| `weekly` | Emails per 7-day window, oldest first. `week` is the window's first day. |
| `tabs` | Emails per Gmail tab, the way TabTidy would sort them. |
| `new_senders_by_month` | Senders seen for the first time, aligned with `meta.months`. |
| `security.events[].kind` | `login`, `code`, `access` (app given access), `change` (account change), `verify` |
| `security.events[].flag` | `true` for things worth a second look: new device or country, phone or password changes. |
| `bills[].kind` | `receipt`, `plan`, `problem` (shown in red) |

## Decisions output

**Copy decisions** / **Download decisions.json** produce:

```json
{
  "source": "inbox-triage-dashboard",
  "scanned_on": "2026-10-31",
  "range": ["2026-05-01", "2026-10-31"],
  "decisions": {
    "unsubscribe": [{ "email": "...", "brand": "...", "group": "...", "emails": 32, "changed_from_suggestion": false }],
    "keep": []
  }
}
```

When the dashboard is published as a Claude artifact with the `db` capability, only the senders you changed are stored, in collection `decisions`, one document per sender: `{ "email", "action", "updated" }`.
