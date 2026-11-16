---
name: sort-into-tabs
description: Apply TabTidy labels and move Gmail conversations into the right tab (Primary, Updates, Promotions, Social, Forums) per confirmed sender decisions, in small confirmed batches. Use when the user asks to sort, label or organise their Gmail into tabs.
---

# TabTidy step 5 · Sort into tabs and labels 🏷️

**Changes Gmail: yes, labels and tabs only.** Nothing is deleted, archived or marked
read, and nothing leaves the inbox. Tell the user this before you start.

Goal: **Primary** keeps only people, codes and things that need them. Everything else
moves to Updates, Promotions, Social or Forums, with a label they can click.

| Group | Tab (`CATEGORY_` label) | Label |
|---|---|---|
| security | Primary (`CATEGORY_PERSONAL`) | Security & Account |
| action | Primary | Bills & Receipts |
| official | Primary | Official & Gov |
| people | Primary | (none) |
| bills | Updates (`CATEGORY_UPDATES`) | Bills & Receipts |
| subscriptions | Updates | Subscriptions |
| orders | Updates | Orders & Deliveries |
| travel | Updates (flight changes: Primary) | Travel & Bookings |
| jobs | Updates | Jobs |
| newsletters | Updates | Newsletters |
| notices | Updates | Notices |
| promotions | Promotions (`CATEGORY_PROMOTIONS`) | Ads & Promotions |
| social | Social (`CATEGORY_SOCIAL`) | Social |
| review | Forums (`CATEGORY_FORUMS`) | Review needed |
| suspicious | leave for `delete-junk` (spam) | (none) |

## Inputs

`tabtidy-decisions.json` (step `decide`), or the grouped scan if the user wants to sort
by the suggestions.

## Recipe (stop after each numbered step and show what you did)

1. List labels. Create any of these that are missing: Security & Account,
   Bills & Receipts, Official & Gov, Travel & Bookings, Subscriptions,
   Orders & Deliveries, Jobs, Newsletters, Notices, Ads & Promotions, Social,
   Review needed. Note their label ids.
2. **Test batch:** pick ONE sender, at most 20 conversations (`from:<address> in:inbox`).
   For each thread add its label id and the matching `CATEGORY_*` label (Gmail removes
   the old category by itself). Show the user and ask them to check in Gmail.
3. After the user says OK, do the rest **group by group**, reporting counts after each.

## Rules

- Keep everything in the inbox. Don't archive, trash or mark as read.
- Security, action-needed, official and people mail stays in Primary.
- **More than ~200 conversations in a group?** Don't do them one by one. Give the user
  the Gmail search (e.g. `from:(a@x.example OR b@y.example) in:inbox`) and these steps:
  paste it in Gmail's search bar → tick select-all → **Select all conversations that
  match this search** → label icon → tick the label → **Apply** → right-click →
  **Move to tab** → pick the tab.
