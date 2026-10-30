# 05 · Sort into tabs and labels 🏷️

> **Changes Gmail?** Yes: labels and tabs only. Nothing is deleted, and nothing leaves your inbox.
> Works in **small confirmed batches**.

Goal: **Primary** keeps only people, codes and things that need you. Everything else moves to **Updates, Promotions, Social or Forums**, with a label you can click on.

| Tab | Gets | Label |
|---|---|---|
| Primary | people, OTP and logins, payment problems, government, flight changes | Security & Account · Bills & Receipts · Official & Gov · Travel & Bookings |
| Updates | receipts, orders, travel, jobs, subscriptions, newsletters, notices | Bills & Receipts · Orders & Deliveries · Travel & Bookings · Jobs · Subscriptions · Newsletters · Notices |
| Promotions | ads, sales | Ads & Promotions |
| Social | social networks | Social |
| Forums | bulk mail you haven't decided on | Review needed |

## Prompt

```
Using my confirmed decisions, sort my inbox. Work in this order and stop
after each step to show me what you did:

1. Create any of these labels that are missing: Security & Account,
   Bills & Receipts, Official & Gov, Travel & Bookings, Subscriptions,
   Orders & Deliveries, Jobs, Newsletters, Notices, Ads & Promotions,
   Social, Review needed.
2. Do ONE sender first, at most 20 conversations, so I can check it:
   add its label and move it to its tab by adding the matching
   CATEGORY_ label (CATEGORY_UPDATES, CATEGORY_PROMOTIONS, CATEGORY_SOCIAL,
   CATEGORY_FORUMS, or CATEGORY_PERSONAL for Primary).
3. After I say OK, do the rest, group by group.

Rules:
- Keep everything in the inbox. Don't archive, trash or mark as read.
- Security, action-needed, official and people mail stays in Primary.
- If a group has more than ~200 conversations, don't do it one by one:
  give me the Gmail search for it so I can bulk-select it in Gmail instead.
```

## Big inbox? Use Gmail's bulk select

The connector changes one conversation at a time. For hundreds, Gmail's website is faster:

1. Paste the search Claude gives you into Gmail's search bar.
2. Tick the select-all box → **Select all conversations that match this search**.
3. Click the label icon → tick the label → **Apply**.
4. Right-click the selection → **Move to tab** → pick the tab.
