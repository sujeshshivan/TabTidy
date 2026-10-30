# Path 2 · TabTidy script + Gmail filters ⚙️

No AI required. Two tools that run inside your own Google account:

| | **TabTidy script** | **Gmail filters (XML)** |
|---|---|---|
| Speed | On a schedule (every 10 min … monthly) | Instant, as mail arrives |
| Moves mail between tabs | ✅ all five | Only to Primary |
| Adds labels | ✅ | ✅ |
| Regex patterns | ✅ | ❌ (plain words only) |
| Setup | ~5 minutes | ~2 minutes |

**Best combo:** import `primary-essentials.xml` (instant security and payment alerts) **+** run TabTidy (everything else). Skip `labels.xml` if you use TabTidy; the script does that job better.

---

## Part A · TabTidy script 🧹

### What it does

Every run, each **unsorted** inbox email gets one tab and one label (see the table in the [README](../README.md#️-where-everything-ends-up)). Then it's marked with a hidden **Sorted** label and never touched again, so anything you move by hand stays put.

It **never deletes, archives, replies, forwards or opens links**, and never reads message bodies.

### Before you start: turn on all five tabs

Gmail → ⚙ → **See all settings** → **Inbox** → Categories: tick **Primary, Promotions, Social, Updates, Forums** → **Save Changes**.

### Option 1 · Copy-paste (simplest) 📋

1. Open **[script.google.com](https://script.google.com)** → **New project**.
2. Delete the sample code. Paste all of [`apps-script/TabTidy.gs`](../apps-script/TabTidy.gs).
3. Rename the project (top left) to **TabTidy**, then press **Ctrl+S** (⌘S on Mac).
4. Left sidebar: **Services ➕** → **Gmail API** → **Add**.
5. Toolbar dropdown: pick **`preview`** → **▶ Run**. Approve access (see [the warning](#-google-hasnt-verified-this-app)). The log shows where your latest 30 emails *would* go. Nothing changes.
6. Pick **`setup`** → **▶ Run**. Creates labels, sorts recent mail, starts the schedule.
7. Optional: **`sortWholeInbox`** → **▶ Run** to sort older mail too. It keeps going in batches by itself.

To change rules or the schedule, edit `CONFIG` at the top of the file, save, and run `setup` again.

### Option 2 · Use the TabTidy library 📚

The same code, published as a library. You get updates by switching versions, and your own settings live in a tiny wrapper.

```
Script ID:  1sj4sFD5amFGbVXBACvSlhsKh_RApKp3wfu7_1-1s6QHS1O-jAasOGwI7
Identifier: TabTidy
```

1. **[script.google.com](https://script.google.com)** → **New project** → name it **My TabTidy**.
2. Left sidebar: **Libraries ➕** → paste the Script ID → **Look up** → pick the **latest version** → keep identifier **TabTidy** → **Add**.
3. **Services ➕** → **Gmail API** → **Add**. Your project needs this too.
4. Replace the sample code with [`apps-script/Wrapper.gs`](../apps-script/Wrapper.gs). Change `MY_CONFIG` if you like. Save.
5. Run **`preview`**, then **`setup`**, then optionally **`sortWholeInbox`**.

> Keep the function names in the wrapper exactly as they are. The schedule calls them by name.

**Updating to a new version:** Libraries → click **TabTidy** → choose the new version → Save. Nothing updates without you choosing it.

### Which functions to run

| Function | Use it to… | Changes Gmail? |
|---|---|---|
| `preview` | See where your latest 30 emails would go | No |
| `setup` | Start, or apply changed settings | Yes |
| `sortNewMail` | Sort right now instead of waiting | Yes |
| `sortWholeInbox` | Sort everything, old mail included | Yes |
| `stop` | Turn the schedule off | No |

### Settings explained

| Setting | Default | Meaning |
|---|---|---|
| `schedule` | `{ minutes: 10 }` | How often to sort. Also `{ hours: 1 }`, `{ days: 1 }`, `{ weeks: 1 }`, `{ months: 1 }`. Between runs, new mail waits unsorted. |
| `atHour` | `8` | Time of day for daily, weekly and monthly runs (your time zone). |
| `lookBackDays` | `3` | Each run checks unsorted mail from the last N days. Keep it ≥ the gap between runs (e.g. `31` for monthly). |
| `batchSize` | `100` | Emails per batch. Google stops scripts after 6 minutes, so bigger jobs continue in batches, one minute apart. |
| `doneLabel` | `Sorted` | Hidden marker on sorted mail. Mail you move by hand stays where you put it. |
| `addLabels` | `true` | `false` = only move mail between tabs, no labels. |

**Why not every minute?** Free Google accounts get a daily allowance of script run time (about 90 minutes). Every minute uses it up fast; every 10 minutes is about 144 tiny runs a day.

### Custom rules ✏️

Rules live in `CONFIG.rules`. They're checked **top to bottom; the first match wins.**

```js
{
  label: 'Bills & Receipts',          // Gmail label (created if missing)
  tab: TAB.UPDATES,                   // PRIMARY | UPDATES | PROMOTIONS | SOCIAL | FORUMS
  subject: /\b(receipt|invoice)\b/i,  // regex on the subject…
  from: /(mybank|myelectric)\./i,     // …OR on the sender
  unless: /\b(promo|offer)\b/i,       // cancels the rule if the subject matches
  important: false,                   // true = mark important
  bulkOnly: false,                    // true = only mass mail (has an unsubscribe header)
},
```

**Regex cheat sheet**

| Pattern | Matches |
|---|---|
| `/\.gov(\.[a-z]{2})?\b/i` | any government sender: `.gov`, `.gov.my`, `.gov.uk`… |
| `/@(mail\|email\|news)\.[a-z0-9-]+\.[a-z]/i` | marketing subdomains like `mail.shop.example` |
| `/\b(otp\|tac)\b/i` | the whole word "OTP" or "TAC", not "optional" |
| `/\d+\s?% off/i` | "20% off", "50 % off" |
| `/(maybank\|cimb\|paypal)\./i` | any of these senders |

Library users: copy the rules with `TabTidy.defaultConfig().rules`, change them, and pass them in `MY_CONFIG.rules`. Tab ids come from `TabTidy.tabs()`.

Quick personal tweaks without regex: add pieces of addresses to `alwaysPrimary` or `alwaysPromotions`.

---

## Part B · Gmail filters (XML) 📄

| File | What it does | Imports cleanly? |
|---|---|---|
| [`filters/primary-essentials.xml`](../filters/primary-essentials.xml) | Security/OTP, payment problems, government, flight changes → **label + Primary + important + never spam** | ✅ |
| [`filters/labels.xml`](../filters/labels.xml) | Bills, banks, utilities, subscriptions, orders, travel, jobs, social, newsletters, notices, ads → **label only** | ✅ |

### Import

1. Gmail → ⚙ → **See all settings** → **Filters and Blocked Addresses**.
2. Bottom of the page: **Import filters** → **Choose file** → pick the XML → **Open file**.
3. Tick **Apply new filters to existing email** (sorts your old mail too).
4. **Create filters**.

### Customise

Edit the lists in [`filters/build_filters.py`](../filters/build_filters.py) (your banks, shops, couriers…), then:

```bash
python filters/build_filters.py
```

### ⚠️ Lesson learned: "Could not create"

In testing, Gmail's importer accepted **"Categorize as Primary"** but rejected **"Categorize as Promotions / Social / Updates / Forums"**, so those filters failed to import. That's why `labels.xml` only adds labels, and TabTidy handles tab moves.

---

## 🔐 "Google hasn't verified this app"

You'll see this the first time you run TabTidy. It's normal for any script you run in your own account: Google only "verifies" apps published to the public. Click **Advanced → Go to TabTidy (unsafe) → Allow**.

Before allowing, you can (and should) read the code. It's one file. Search it for `delete`, `trash` or `send`: you won't find Gmail calls that do those things.

To remove access later: **myaccount.google.com → Security → Third-party apps → TabTidy → Remove access**.
