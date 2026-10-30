# Security & privacy 🔒

This project touches people's email, so safety is a feature, not a footnote.

## What each part can do

| Part | Reads | Changes | Never |
|---|---|---|---|
| **TabTidy script** | sender, subject, unsubscribe header | labels, Gmail tab, "important" | delete, archive, reply, forward, open links, read bodies |
| **Filter files** | (Gmail applies them) | labels, Primary tab, important, not-spam | anything else |
| **Claude prompts** | sender, subject, dates; a body only to find an unsubscribe link | labels, tabs, Trash, spam, after you approve each batch | empty Trash, send email, click links |
| **Dashboard** | the JSON you give it | nothing in Gmail | contact your mailbox |

## Rules for contributors

1. **No real mail data, ever.** No scans, sender lists, screenshots or addresses from a real inbox. Sample data uses `.example` domains.
2. **No new Gmail permissions** without a clear reason in the PR. TabTidy must never gain delete, send or forward abilities.
3. **No network calls** from the script or dashboard to anywhere except Google's own Gmail service.
4. Run `python tools/check_no_personal_data.py` before committing. CI runs it on every push.

## For library users

- The library runs **in your account, on your mail only**. Its author can't see your mail.
- Each version is frozen. Read the code of a new version before switching to it.
- When a script is shared, Google shows its owner's account to anyone who opens it. That's Google's design, not this project's.
- Remove access any time: Google Account → **Security → Third-party apps**.

## Reporting a problem

Found something that could expose someone's mail? Please **open a private security advisory** on GitHub (Security tab → Report a vulnerability) rather than a public issue.
