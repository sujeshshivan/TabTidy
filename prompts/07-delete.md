# 07 · Delete the junk 🗑️

> **Changes Gmail?** Yes: moves mail to **Trash**. Gmail keeps Trash for 30 days, so it's undo-able.
> Claude never empties Trash or deletes permanently.

## Prompt

```
I want to delete mail from these senders: <list, or "everything I marked delete">.

Before deleting:
1. Count how many conversations each sender has and show me.
2. Check whether any of them are security, login, payment or official
   emails. Social networks and shops often send security alerts from a
   related address (security@, registration@). List those separately;
   they must NOT be deleted.
3. Wait for my OK.

Then move the rest to Trash in batches, and confirm with a search that
nothing from those senders is left (except the ones we kept).
```

## Real example

A cleanup like this found **"Did you just log in from a new device in another country?"** hiding among hundreds of social notifications. Step 2 exists for exactly that. 🕵️

## Undo

Gmail → **Trash** → select → **Move to Inbox**. Possible for 30 days.
