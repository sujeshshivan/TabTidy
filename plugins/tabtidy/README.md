# TabTidy plugin for Claude

Sort Gmail into tabs, find bills, unsubscribe and delete junk, with Claude and the
Gmail connector. Start with `/tabtidy:tidy-inbox` or just say "tidy my inbox".

**Install and usage guide:** [docs/claude-plugin.md](../../docs/claude-plugin.md)

| Skill | What it does | Changes Gmail? |
|---|---|---|
| `tidy-inbox` | Runs every step below in order | per step |
| `scan` | Counts mail per sender per month | No |
| `group` | One group and suggested action per sender | No |
| `find-bills` | Payment problems, subscriptions, receipts | No |
| `dashboard` | Interactive triage dashboard | No |
| `decide` | Final decision per sender | No |
| `sort-into-tabs` | Labels and tabs, in confirmed batches | Labels & tabs |
| `unsubscribe` | One unsubscribe link per sender; you click | No |
| `delete-junk` | Trash after checks; only when you type it | Trash (30-day undo) |
| `filters` | Gmail filter XML to import | Only on import |
| `keep-clean` | Weekly check or the TabTidy script | Labels & tabs |

Requires the **Gmail connector** (claude.ai → Settings → Connectors → Gmail).

The files in `skills/*/assets`, `references` and `scripts` are copies of files elsewhere in
this repo. Edit the originals and run `python tools/sync_plugin.py`.
