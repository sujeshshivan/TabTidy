# The rulebook 📏

Used by the Claude prompts (02-group) and, as regex, by TabTidy. One sender or email → one group → one tab → one label.

| Group | Examples | Tab | Label | Default action |
|---|---|---|---|---|
| 🔐 security | OTP, TAC, "new sign-in", password reset | Primary | Security & Account | Keep |
| ⚠️ action | "payment failed", "action required", overdue | Primary | Bills & Receipts | Keep, then act |
| 🏛️ official | `*.gov`, `*.gov.my`, tax, pension | Primary | Official & Gov | Keep |
| 👤 people | anyone writing to you personally | Primary | — | Keep |
| 🧾 bills | receipts, invoices, bank and utility statements | Updates | Bills & Receipts | Label |
| 🔁 subscriptions | plan started/ended, trial ending, renewal | Updates | Subscriptions | Label |
| 📦 orders | shipped, out for delivery, tracking | Updates | Orders & Deliveries | Label |
| 🎫 travel | booking confirmation, e-ticket, itinerary | Updates | Travel & Bookings | Label |
| 💼 jobs | job alerts, applications | Updates | Jobs | Label |
| 📰 newsletters | digests you signed up for | Updates | Newsletters | Label, or unsubscribe if never read |
| 🛠️ notices | app, cloud, policy and terms updates | Updates | Notices | Label or archive |
| 💬 social | social network notifications | Social | Social | Unsubscribe in app settings, delete old |
| 🛍️ promotions | sales, vouchers, "we miss you" | Promotions | Ads & Promotions | Unsubscribe and delete |
| 🚩 suspicious | look-alike brands, prize bait | — | — | Mark as spam |
| 🤷 review | bulk mail nothing recognised | Forums | Review needed | You decide |

## Signals

- **Subject words beat sender names** for money mail: "receipt", "invoice", "payment failed".
- **Marketing senders** look like `marketing@`, `offers@`, `news@`, or `mail.` / `email.` / `engage.` subdomains, and always carry an unsubscribe header.
- **Unsubscribe header present** = mass mail. Absent = probably a person.
- **You replied** = a real conversation, so it stays in Primary.
- **Recipient isn't you** (mail for another address reaching your inbox) → review. You may have a forwarding rule or alias you forgot about.

## Never

- Suggest deleting or unsubscribing from security, action, official or people mail.
- Unsubscribe from suspicious mail. Mark it as spam instead.
- Delete permanently. Trash only.
