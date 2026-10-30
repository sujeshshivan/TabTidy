#!/usr/bin/env python3
"""Builds the two Gmail filter files in this folder.

    python filters/build_filters.py

primary-essentials.xml  4 filters that keep must-see mail in Primary, mark it
                        important and never send it to spam. Act instantly.
labels.xml              Label-only filters for everything else (bills, orders,
                        travel, jobs, social, newsletters, notices, ads).

Why two files? In testing, Gmail's "Import filters" accepted "Categorize as
Primary" but refused "Categorize as Promotions / Social / Updates / Forums"
("Could not create"). So tab moves for those are left to the Apps Script
(apps-script/InboxSorter.gs) or to Gmail's own tab sorting.

Edit the lists below, run this file, then import the XML.
Each filter's search must stay under ~1,500 characters (Gmail's limit).
"""
import pathlib
from xml.sax.saxutils import quoteattr

HERE = pathlib.Path(__file__).resolve().parent
OR = " OR ".join

# ── What counts as what ─────────────────────────────────────────────────────
SECURITY_FROM = ["accounts.google.com", "noreply-accounts@google.com", "security@facebookmail.com",
                 "registration@facebookmail.com", "security@mail.instagram.com", "security-noreply@linkedin.com",
                 "account-security-noreply@accountprotection.microsoft.com", "appleid@id.apple.com"]
SECURITY_SUBJ = ['"security alert"', '"verification code"', "OTP", "TAC", '"one-time"', '"one time password"',
                 '"new sign-in"', '"sign-in attempt"', '"new login"', '"login alert"', '"new device"',
                 '"password reset"', '"reset your password"', '"verify your email"', '"confirm your email"',
                 '"confirmation code"', '"2-step"', '"two-factor"', '"suspicious"', '"unusual activity"',
                 '"account locked"', '"kod pengesahan"']
ACTION_SUBJ = ['"action required"', '"action needed"', '"payment failed"', '"failed to process"',
               '"update your payment"', '"verify your payment"', '"payment declined"', '"past due"', "overdue",
               '"final notice"', '"account suspended"', '"tindakan diperlukan"']
GOV_FROM = ["gov.my", "gov.uk", "gov.sg", "gov.au", "gov.in", "gov.ph", "go.id", "usa.gov", "irs.gov", "ssm.com.my"]
TRAVEL_URGENT = ['"flight cancelled"', '"flight canceled"', '"schedule change"', '"flight delay"',
                 '"gate change"', '"booking cancelled"']

BANKS = ["maybank2u.com.my", "maybank.com", "cimb.com", "cimbclicks.com.my", "pbebank.com", "publicbank.com.my",
         "rhbgroup.com", "hlb.com.my", "ambankgroup.com", "bankislam.com.my", "bsn.com.my", "uob.com.my",
         "ocbc.com.my", "hsbc.com.my", "affinbank.com.my", "alliancebank.com.my", "bankrakyat.com.my",
         "tngdigital.com.my", "boost.com.my", "grabpay.com", "paypal.com", "wise.com", "stripe.com",
         "gxbank.my", "bigpay.my", "revolut.com"]
UTILITIES = ["tnb.com.my", "mytnb.com.my", "unifi.com.my", "tm.com.my", "celcomdigi.com", "maxis.com.my",
             "u.com.my", "yes.my", "astro.com.my", "airselangor.com", "indahwater.com"]
RECEIPT_SUBJ = ["receipt", "invoice", "resit", '"payment received"', '"payment successful"',
                '"payment confirmation"', '"transaction alert"', '"e-statement"', '"your bill"', '"bill is ready"',
                "refund"]
SUBS_SUBJ = ["subscription", "renewal", '"auto-renew"', '"your plan"', '"new plan"', '"pro plan"',
             '"premium plan"', '"trial ends"', '"trial ending"', '"has ended"', "cancellation", "membership"]
COURIERS = ["pos.com.my", "poslaju.com.my", "jtexpress.my", "ninjavan.co", "dhl.com", "fedex.com", "ups.com",
            "usps.com", "royalmail.com", "citylinkexpress.com", "gdexpress.com", "spx.com.my", "flashexpress.my",
            "lalamove.com", "skynet.com.my"]
ORDER_SUBJ = ['"order confirmation"', '"order confirmed"', '"your order"', '"thank you for your order"',
              "shipped", '"out for delivery"', "delivered", '"tracking number"', '"on its way"', "parcel",
              '"ready for pickup"', "penghantaran"]
TRAVEL_FROM = ["airasia.com", "malaysiaairlines.com", "batikair.com", "singaporeair.com", "emirates.com",
               "qatarairways.com", "booking.com", "agoda.com", "traveloka.com", "trip.com", "klook.com",
               "expedia.com", "airbnb.com", "ktmb.com.my", "easybook.com"]
TRAVEL_SUBJ = ['"booking confirmation"', '"booking confirmed"', '"your booking"', '"e-ticket"', "itinerary",
               '"boarding pass"', "reservation", "tempahan"]
JOBS_FROM = ["jobstreet.com", "indeed.com", "glassdoor.com", "hiredly.com", "maukerja.my",
             "jobs-noreply@linkedin.com", "jobalerts-noreply@linkedin.com", "myworkday.com", "greenhouse.io",
             "lever.co"]
JOBS_SUBJ = ['"job alert"', '"jobs for you"', '"new jobs"', '"application received"', '"your application"']
SOCIAL = ["facebookmail.com", "instagram.com", "linkedin.com", "x.com", "twitter.com", "tiktok.com",
          "pinterest.com", "redditmail.com", "quora.com", "discord.com", "snapchat.com", "threads.net",
          "youtube.com", "telegram.org", "tumblr.com", "meetup.com"]
NEWSLETTER_FROM = ["substack.com", "beehiiv.com", "medium.com", "mailchimp.com", "convertkit.com", "ghost.io",
                   "buttondown.email"]
NEWSLETTER_SUBJ = ["newsletter", "digest", '"weekly roundup"', '"this week in"', '"monthly update"']
NOTICE_FROM = ["github.com", "gitlab.com", "bitbucket.org", "vercel.com", "netlify.com", "render.com",
               "railway.app", "heroku.com", "supabase.com", "firebase.google.com", "amazonaws.com",
               "aws.amazon.com", "azure.microsoft.com", "cloudflare.com", "digitalocean.com", "docker.com",
               "npmjs.com", "sentry.io", "atlassian.com", "slack.com", "notion.so", "zoom.us", "dropbox.com"]
NOTICE_SUBJ = ['"terms of service"', '"privacy policy"', '"policy update"', '"updates to our terms"',
               '"scheduled maintenance"']
ADS_SUBJ = ['"% off"', "sale", '"flash sale"', "deal", "deals", "discount", "voucher", "coupon", "promo",
            '"limited time"', '"last chance"', '"ends tonight"', '"free shipping"', "cashback", '"exclusive offer"',
            '"special offer"', "giveaway", '"we miss you"', '"misses you"', "jualan", "diskaun", "baucar",
            "tawaran"]
SHOPS = ["shopee.com.my", "shopee.com", "lazada.com.my", "zalora.com.my", "temu.com", "shein.com",
         "aliexpress.com", "amazon.com", "ebay.com", "taobao.com", "carousell.com", "grab.com", "foodpanda.my",
         "shopback.my"]

NOT_SECURITY = f"-subject:({OR(SECURITY_SUBJ[:10])})"
NOT_MONEY = f"-subject:({OR(['receipt', 'invoice', 'order', 'booking', 'statement', 'OTP', 'TAC'])})"
NO_PROMO = f"-subject:({OR(['promo', 'offer', 'deal', 'cashback', 'win', 'contest', 'reward'])})"

PRIMARY = "^smartlabel_personal"

ESSENTIALS = [
    ("Security, OTP and logins", f"from:({OR(SECURITY_FROM)}) OR subject:({OR(SECURITY_SUBJ)})", "Security & Account"),
    ("Payment problems and action required", f"subject:({OR(ACTION_SUBJ)})", "Bills & Receipts"),
    ("Government and official", f"from:({OR(GOV_FROM)})", "Official & Gov"),
    ("Flight and booking changes", f"subject:({OR(TRAVEL_URGENT)})", "Travel & Bookings"),
]

LABELS = [
    ("Receipts and invoices", f"subject:({OR(RECEIPT_SUBJ)})", "Bills & Receipts"),
    ("Banks and e-wallets", f"from:({OR(BANKS)}) {NO_PROMO}", "Bills & Receipts"),
    ("Utilities, telco and TV", f"from:({OR(UTILITIES)}) {NO_PROMO}", "Bills & Receipts"),
    ("Subscriptions and plans", f"subject:({OR(SUBS_SUBJ)}) -subject:(sale OR discount OR \"% off\")", "Subscriptions"),
    ("Orders and deliveries", f"from:({OR(COURIERS)}) OR subject:({OR(ORDER_SUBJ)})", "Orders & Deliveries"),
    ("Travel bookings", f"from:({OR(TRAVEL_FROM)}) subject:({OR(TRAVEL_SUBJ)})", "Travel & Bookings"),
    ("Travel bookings (any sender)", f"subject:({OR(TRAVEL_SUBJ[:6])}) -subject:(sale OR deal OR promo OR offer)", "Travel & Bookings"),
    ("Jobs", f"from:({OR(JOBS_FROM)}) OR subject:({OR(JOBS_SUBJ)})", "Jobs"),
    ("Social networks", f"from:({OR(SOCIAL)}) -from:({OR(SECURITY_FROM[2:6])}) {NOT_SECURITY}", "Social"),
    ("Newsletters", f"from:({OR(NEWSLETTER_FROM)}) OR subject:({OR(NEWSLETTER_SUBJ)})", "Newsletters"),
    ("App, cloud and policy notices", f"from:({OR(NOTICE_FROM)}) {NOT_SECURITY}", "Notices"),
    ("Policy and maintenance notices", f"subject:({OR(NOTICE_SUBJ)})", "Notices"),
    ("Ads by wording (only mass mail)", f"unsubscribe subject:({OR(ADS_SUBJ)}) {NOT_MONEY}", "Ads & Promotions"),
    ("Shop and marketplace promos", f"from:({OR(SHOPS)}) {NOT_MONEY} -subject:(shipped OR delivered OR refund)", "Ads & Promotions"),
]


def entry(note, query, label, primary=False):
    assert len(query) < 1450, f"{note}: search is {len(query)} characters, over Gmail's limit"
    lines = [f"<!-- {note} -->", "<entry>", "<category term='filter'></category>", "<title>Mail Filter</title>",
             "<content></content>", f"<apps:property name='hasTheWord' value={quoteattr(query)}/>",
             f"<apps:property name='label' value={quoteattr(label)}/>"]
    if primary:
        lines += [f"<apps:property name='smartLabelToApply' value='{PRIMARY}'/>",
                  "<apps:property name='shouldAlwaysMarkAsImportant' value='true'/>",
                  "<apps:property name='shouldNeverSpam' value='true'/>"]
    lines += ["<apps:property name='sizeOperator' value='s_sl'/>",
              "<apps:property name='sizeUnit' value='s_smb'/>", "</entry>"]
    return "\n".join(lines)


def write(name, entries, primary):
    body = "\n".join(entry(n, q, l, primary) for n, q, l in entries)
    xml = ("<?xml version='1.0' encoding='UTF-8'?>\n"
           "<feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>\n"
           f"<title>Mail Inbox Manager filters: {name}</title>\n{body}\n</feed>\n")
    (HERE / name).write_text(xml, encoding="utf-8")
    print(f"Wrote filters/{name}: {len(entries)} filters")


if __name__ == "__main__":
    write("primary-essentials.xml", ESSENTIALS, primary=True)
    write("labels.xml", LABELS, primary=False)
