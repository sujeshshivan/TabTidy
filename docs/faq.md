# FAQ & troubleshooting 🙋

### Filter import says "Could not create"
Gmail's importer rejects "Categorize as" anything except Primary. Use [`filters/labels.xml`](../filters/labels.xml) (label-only), and let TabTidy or Gmail's own sorting choose the tab. If a filter still fails, check its search is under ~1,500 characters.

### "Google hasn't verified this app"
Normal for personal scripts. See [Path 2 → verification](path-2-script-and-filters.md#-google-hasnt-verified-this-app).

### The library says "not found" when I paste the Script ID
The library owner hasn't shared it, or you're signed in to a different Google account. The project must be shared as **Anyone with the link → Viewer**.

### I get "Gmail is not defined"
You haven't added the **Gmail API** service to *your* project: **Services ➕ → Gmail API → Add**. Library users need it in their own project too.

### TabTidy moved something to the wrong tab
Move it back by hand. It won't be touched again, because of the hidden **Sorted** label. For the future, add the sender to `alwaysPrimary` or `alwaysPromotions`, or adjust a rule.

### Do labels apply themselves to new mail?
No. Something has to add them: a **filter** (instantly, on arrival) or **TabTidy** (on its schedule). Labels are just tags.

### Why does new mail sit in Primary for a while?
TabTidy runs on a schedule; Google gives scripts no "new email" signal. Shorten `schedule` for faster sorting. Security and payment mail can be instant with `primary-essentials.xml`.

### Can Claude create Gmail filters for me?
Not through the Gmail connector. Claude can write the XML file, and you import it (2 clicks).

### Will this delete my email?
TabTidy: never. Claude (Path 1): only when you ask, only to **Trash** (undo for 30 days), and only after showing you counts and checking for security mail.

### Is my email sent anywhere?
No. TabTidy runs inside your Google account. With Claude, mail metadata is read through Gmail's official connector, using your own sign-in.

### I want to undo everything
- Labels: Gmail sidebar → label ⋮ → **Remove label** (emails stay).
- Filters: Settings → Filters → select → **Delete**.
- TabTidy: run `stop`, then remove its access in your Google Account → Security → Third-party apps.
- Deleted mail: **Trash** → select → **Move to Inbox** (within 30 days).
