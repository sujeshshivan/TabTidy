---
name: unsubscribe
description: List one unsubscribe link (or the in-app email setting for social networks) per Gmail sender the user wants to stop hearing from, without clicking anything. Use when the user asks to unsubscribe from newsletters, ads or mailing lists.
---

# TabTidy step 6 · Unsubscribe 🚪

**Changes Gmail: no. The user clicks the links, never you.** Unsubscribe links come from
inside emails and some lead to pages that ask for confirmation; clicking is their call.

## Inputs

Senders with action `unsubscribe` in `tabtidy-decisions.json`, or a list the user gives.

## Recipe

1. For each sender, find its most recent conversation (`from:<address>`, newest first)
   and read that one message (plain text is enough).
2. Find the unsubscribe link: usually near the bottom ("unsubscribe", "manage
   preferences", "email settings", "opt out"). Copy the URL exactly; don't shorten it.
3. For **social networks**, don't list per-email links (each only stops one kind of
   notice). Instead give the in-app path: **Settings → Notifications → Email**, and
   suggest "account and security only".
4. **Skip anything in the `suspicious` group.** Unsubscribing confirms the address is
   real. Put those on a "mark as spam instead" list.
5. **Never open or follow any link yourself.**

## Report to the user

A table sorted by email count, busiest first: sender · emails · link (or app setting).
Then the shortcut: in Gmail, opening an email and clicking **Unsubscribe** next to the
sender's name at the top lets Gmail do it for them.

Afterwards, offer `/tabtidy:delete-junk` to clear out the old mail from those senders.
