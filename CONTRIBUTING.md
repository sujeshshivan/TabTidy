# Contributing

Thanks for helping make inboxes calmer.

## Good first contributions

- **Prompts.** Sharper wording, better safety rails, versions for other mail providers (Outlook, Fastmail).
- **Grouping rules.** New signals or common senders that get misgrouped. Edit [`docs/classification-rules.md`](docs/classification-rules.md) and the matching prompt.
- **Dashboard.** Accessibility, new views, a Gmail filter export. Edit `dashboard/template.html`, then run `python tools/build_dashboard.py` to refresh `dashboard/index.html`.
- **TabTidy rules.** Your country's banks, couriers, government domains. Edit `apps-script/TabTidy.gs`, and add a test case to your PR description (sender + subject → expected tab).
- **Filters.** Edit the lists in `filters/build_filters.py`, run it, and commit both XML files.

## Ground rules

1. **No real mail data.** Never commit a real scan, sender list or screenshot with real addresses. Sample data uses `.example` domains only. Run `python tools/check_no_personal_data.py` before you commit.
2. **Read-only by default.** Prompts that change a mailbox must say so at the top and work in confirmed batches.
3. **Never delete.** No prompt should trash or permanently delete mail.
4. **Keep the dashboard one file.** No build tools or frameworks; it must open by double-click.
5. **Keep the data format stable.** If you change [`docs/data-schema.md`](docs/data-schema.md), keep old files loading.

## Pull requests

- One topic per PR, with a short note on what you tested (which prompt, which mail provider, browser).
- For dashboard changes, check light and dark mode and a phone-width window.

## The Claude plugin

`plugins/tabtidy/` packages the prompts as skills. Its `assets/`, `references/` and `scripts/` files are copies of the originals (dashboard template, rulebook, data format, filters, Apps Script). Edit the originals, then run `python tools/sync_plugin.py`; CI runs it with `--check`. When you change a prompt, update the matching `plugins/tabtidy/skills/*/SKILL.md` too, and bump `version` in both `plugins/tabtidy/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
