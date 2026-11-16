---
name: delete-junk
description: Move junk Gmail from chosen senders to Trash (undo-able for 30 days) after counting and checking for hidden security, login and payment emails, and mark suspicious senders as spam. Runs only when the user invokes it.
disable-model-invocation: true
---

# TabTidy step 7 · Delete the junk 🗑️

**Changes Gmail: yes, moves mail to Trash.** Gmail keeps Trash for 30 days, so it can be
undone. **Never empty Trash and never delete permanently.**

## Inputs

Senders with action `delete` (and `spam`) in `tabtidy-decisions.json`, or the list the
user gives with the command (`$ARGUMENTS`).

## Recipe

1. **Count.** For each sender, count conversations (`from:<address>`, ids-only view,
   follow pages). Show a table: sender · conversations.
2. **Check for mail that must stay.** For each sender's company/domain, search for
   security, login, payment and official mail, including from **sibling addresses**
   (`security@`, `registration@`, `account@`, `billing@` on the same domain):
   `from:(<domain>) subject:(login OR "sign-in" OR "new device" OR code OR OTP OR password OR security OR verify OR "payment failed" OR "action required" OR invoice OR receipt)`.
   List any hits separately and say clearly: **these will NOT be deleted.**
3. **Wait for the user's explicit OK** on the exact list and counts.
4. **Test batch:** trash at most 20 conversations from the first sender, excluding the
   kept ones. Tell the user, and suggest checking Trash in Gmail.
5. After OK, trash the rest in batches of up to 50, reporting progress per sender.
6. For `spam` senders, mark their threads as spam instead of trashing.
7. **Verify:** search each sender again and confirm nothing is left except the kept ones.

## Big numbers

For more than ~200 conversations, give the user the Gmail search (with the kept ones
excluded, e.g. `from:news@shop.example -subject:(receipt OR invoice)`) and the steps:
search → select-all → **Select all conversations that match this search** → 🗑️.

## Undo

Gmail → **Trash** → select → **Move to Inbox**, any time within 30 days.
