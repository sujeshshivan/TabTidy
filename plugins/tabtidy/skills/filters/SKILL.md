---
name: filters
description: Produce importable Gmail filter XML files (TabTidy's ready-made ones, or customised with the user's own senders) so new mail is labelled automatically, and explain how to import them. Use when the user wants Gmail to sort new mail automatically or asks for Gmail filters.
---

# TabTidy step 8 · Gmail filters ⚙️

**Changes Gmail: only after the user imports a file.** The Gmail connector cannot create
filters, so you write the XML and the user imports it (two clicks).

Steps 5–7 cleaned the past; filters handle the future, the moment mail arrives.

## Option A: ready-made files

In `assets/` next to this file:

- `primary-essentials.xml`: security, action required, government and flight changes →
  label + **Categorize as Primary** + always important + never spam.
- `labels.xml`: bills, orders, travel, jobs, social, newsletters, notices, ads →
  **label only**.

Give the user both files.

## Option B: add the user's own senders

`assets/build_filters.py` holds the lists (`SHOPS`, `BANKS`, `UTILITIES`, `COURIERS`, …).
Copy it to a working folder, add the senders from `tabtidy-decisions.json` to the right
lists, run `python3 build_filters.py` there, and give the user the two XML files it
writes. If you can't run Python, edit the XML by hand. Keep every filter's search under
**1,450 characters**.

## How to import (tell the user)

1. Gmail → ⚙ → **See all settings** → **Filters and Blocked Addresses**.
2. Bottom: **Import filters** → **Choose file** → pick the XML → **Open file**.
3. Tick **Apply new filters to existing email** if wanted → **Create filters**.

## ⚠️ Known Gmail quirk

Import accepts "Categorize as **Primary**" but rejects "Categorize as Promotions /
Social / Updates / Forums" with "Could not create". That's why `labels.xml` only adds
labels. To move new mail between the other tabs automatically, use the TabTidy script
(`keep-clean` skill), or drag one email to a tab in Gmail and click **Yes** when Gmail
asks about future messages.
