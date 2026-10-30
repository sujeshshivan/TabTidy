# 04 · Lock in your decisions ✅

> **Changes Gmail?** No.

Go through the dashboard first. Change any suggestion you disagree with. **Quick wins** shows where one click removes the most mail.

## Prompt (dashboard is a Claude artifact)

```
Read my decisions from the dashboard artifact. The "decisions" collection
only holds senders I changed; everyone else uses the suggested action.
Show the final list grouped by action (keep / label / archive /
unsubscribe / delete / spam) with sender and email count.
Don't do anything yet.
```

## Prompt (local dashboard)

Click **Copy decisions** (or **Download decisions.json**), then:

```
Here are my inbox decisions: <paste>
Show the final list grouped by action with sender and email count.
Don't do anything yet.
```
