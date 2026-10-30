# How senders are grouped

Grouping happens per **sender**, not per email. One decision then covers every past and future email from that address, which is what makes the cleanup fast.

| Group | Typical senders | Default action | Why |
|---|---|---|---|
| Promotions / ads | shops, product marketing, onboarding drips ("you haven't finished setting up…") | Unsubscribe | Stops the mail at the source. |
| Newsletters | digests, product-update newsletters | Label, or Unsubscribe if never read | Some are worth keeping, just not in the inbox. |
| Social notifications | Facebook, LinkedIn, Instagram | Unsubscribe via the app's notification settings | Their unsubscribe links often only cover one notification type. |
| Transactional | receipts, bills, bank alerts, OTPs, security alerts | Keep or Label | You may need these later; security alerts must stay visible. |
| Service notices | policy reminders, welcome emails, account notices | Archive | Rarely need action; still searchable. |
| Suspicious | look-alike domains, prize bait | Mark as spam | Never click their links, including unsubscribe. |
| Real people | anyone writing to you personally | Keep | This is the mail the cleanup protects. |
| Needs review | unclear senders; mail addressed to another address that still reaches you | Keep | A human should look first. |

## Signals Claude uses

- **Volume and regularity.** A sender with a steady weekly cadence is almost always automated.
- **Read rate.** A busy sender you never open is the strongest unsubscribe candidate. If nearly everything is unread, read rate stops being useful and volume decides.
- **Address shape.** `noreply@`, `news@`, `marketing@`, `mail.<brand>` and `engage.<brand>` subdomains point to bulk mail.
- **Subject lines.** "Last chance", "misses you", "% off" mark marketing; "receipt", "security alert", "verify" mark mail to keep.
- **Recipient.** Mail addressed to a different address than yours goes to review: it can mean a forwarding rule or alias you forgot about.

## Things the suggestions never do

- Suggest deleting anything. The strongest action is archive.
- Suggest unsubscribing from a suspicious sender.
- Touch security, banking or government mail.
