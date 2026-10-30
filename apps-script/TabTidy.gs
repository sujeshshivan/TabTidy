/**
 * TabTidy — keeps Gmail's Primary tab for things that matter.
 * https://github.com/sujeshshivan/TabTidy (open source, MIT).
 *
 * Every run, each unsorted inbox email gets ONE Gmail tab and ONE label:
 *
 *   Tab          What lands there                                  Label
 *   Primary      people you write to                               (none)
 *                login codes, security alerts                      Security & Account
 *                payment failed, overdue, action required          Bills & Receipts
 *                government mail                                   Official & Gov
 *                flight cancelled / schedule change                Travel & Bookings
 *   Updates      receipts, bank & utility bills                    Bills & Receipts
 *                plan, trial and renewal mail                      Subscriptions
 *                shipped, out for delivery, tracking               Orders & Deliveries
 *                booking confirmations, e-tickets                  Travel & Bookings
 *                job alerts, applications                          Jobs
 *                newsletters and digests                           Newsletters
 *                app, cloud and policy notices                     Notices
 *   Promotions   sales, vouchers, "we miss you"                    Ads & Promotions
 *   Social       social networks                                   Social
 *   Forums       other bulk mail no rule recognised                Review needed
 *
 * SAFE BY DESIGN: it only adds labels and moves mail between tabs.
 * It never deletes, archives, replies, forwards or opens links.
 * It only reads sender, subject and the unsubscribe header — never bodies.
 *
 * TWO WAYS TO USE THIS FILE
 *   A. Copy-paste (simplest): paste this whole file into a new Apps Script
 *      project, add the Gmail API service, run `preview`, then `setup`.
 *      Edit CONFIG below to change rules.
 *   B. As a library: add TabTidy by its Script ID (see README) with the
 *      identifier `TabTidy`, then use apps-script/Wrapper.gs.
 *   Full steps: docs/path-2-script-and-filters.md
 *
 * Version 1.0.0
 */

// ─── Configuration ──────────────────────────────────────────────────────────

const TAB = {
  PRIMARY: 'CATEGORY_PERSONAL',
  UPDATES: 'CATEGORY_UPDATES',
  PROMOTIONS: 'CATEGORY_PROMOTIONS',
  SOCIAL: 'CATEGORY_SOCIAL',
  FORUMS: 'CATEGORY_FORUMS',
};

const CONFIG = {
  settings: {
    // How often to sort. Pick ONE of:
    //   { minutes: 1|5|10|15|30 }  { hours: 1|2|4|6|8|12 }
    //   { days: 1 }  { weeks: 1 }  { months: 1 }   (days/weeks/months run at atHour)
    // Between runs, new mail waits unsorted in the inbox.
    schedule: { minutes: 10 },
    atHour: 8,              // 0-23, your local time

    // Each run looks at unsorted inbox mail from the last N days.
    // Keep it at least as long as the gap between runs.
    lookBackDays: 3,

    // Conversations per batch. Google stops scripts after 6 minutes, so big
    // jobs run in batches of this size, one minute apart, until done.
    batchSize: 100,

    // Hidden label added once an email is sorted. Sorted mail is never touched
    // again, so anything you move by hand stays where you put it.
    doneLabel: 'Sorted',

    // false = only move between tabs, don't add labels.
    addLabels: true,
  },

  // Your exceptions: plain pieces of an address or domain.
  alwaysPrimary: [ /* 'boss@company.example', 'family.example' */ ],
  alwaysPromotions: [ /* 'shop-you-never-buy-from.example' */ ],

  // Rules are checked top to bottom; the FIRST match wins.
  //   from     regex on the sender, e.g. "Shop <deals@mail.shop.example>"
  //   subject  regex on the subject line
  //   unless   regex on the subject that cancels the rule
  //   bulkOnly true = only for mass mail (has an unsubscribe header)
  // A rule matches when `from` OR `subject` matches and `unless` doesn't.
  rules: [
    // ── Primary: needs you ──
    {
      label: 'Security & Account', tab: TAB.PRIMARY, important: true,
      from: /(accounts\.google\.com|account-security|security@|appleid@|noreply-accounts@)/i,
      subject: /\b(otp|tac|one[- ]time (code|password|pin)|verification code|security (alert|code)|new (sign[- ]?in|login|device)|login alert|sign[- ]?in attempt|password reset|reset your password|confirm your email|verify your (email|account)|2-step|two-factor|suspicious|unusual activity|account locked|kod pengesahan)\b/i,
    },
    {
      label: 'Bills & Receipts', tab: TAB.PRIMARY, important: true,   // money problems
      subject: /\b(action (required|needed)|payment (failed|declined)|failed to process|update your payment|verify your payment|past due|overdue|final (notice|reminder)|account (suspended|on hold)|tindakan diperlukan)\b/i,
    },
    {
      label: 'Official & Gov', tab: TAB.PRIMARY, important: true,
      from: /(\.gov(\.[a-z]{2})?\b|\.gob\.|\.mil\b)/i,               // any *.gov, *.gov.my, *.gov.uk …
    },
    {
      label: 'Travel & Bookings', tab: TAB.PRIMARY, important: true,  // trip changes
      subject: /\b(flight (cancel+ed|delayed?)|schedule change|gate change|booking cancel+ed)\b/i,
    },

    // ── Updates: useful, not urgent ──
    {
      label: 'Bills & Receipts', tab: TAB.UPDATES,
      subject: /\b(receipt|invoice|resit|payment (received|successful|confirmation)|transaction (alert|notification)|e-?statement|statement (is )?(ready|available)|your bill|bill is ready|refund)\b/i,
      from: /\b(billing|invoice|receipts?|payments?)[-.@]|(maybank|cimb|pbebank|publicbank|rhb|hlb|hongleong|ambank|bankislam|bsn|uob|ocbc|hsbc|affin|alliancebank|bankrakyat|tngdigital|touchngo|boost|grabpay|paypal|wise\.com|stripe|tnb|unifi|celcomdigi|celcom|maxis|astro|airselangor|indahwater)\./i,
      unless: /\b(promo|offer|deal|win|contest|reward|cashback|sale)\b/i,
    },
    {
      label: 'Orders & Deliveries', tab: TAB.UPDATES,
      subject: /\b(order (confirmation|confirmed|#?\d+)|your order|thank you for your (order|purchase)|shipped|has shipped|out for delivery|delivered|tracking (number|no)|on its way|parcel|ready for (pick ?up|collection)|penghantaran|dihantar)\b/i,
      from: /(pos\.com\.my|poslaju|jtexpress|ninjavan|dhl|fedex|ups\.com|usps|royalmail|citylink|gdex|spx\.|flashexpress|lalamove|skynet)/i,
    },
    {
      label: 'Travel & Bookings', tab: TAB.UPDATES,
      subject: /\b(booking (confirmation|confirmed|reference)|your (booking|trip|reservation|stay)|e-?ticket|itinerary|boarding pass|tempahan)\b/i,
      unless: /\b(sale|deal|promo|offer|% off)\b/i,
    },
    {
      label: 'Subscriptions', tab: TAB.UPDATES,
      subject: /\b(subscription|renewal|renews?|auto-renew|your (plan|membership)|(new|pro|premium) plan|(free )?trial (ends|ending|expires)|has ended|cancell?ation)\b/i,
      unless: /\b(\d+% off|sale|deal|discount)\b/i,
    },
    {
      label: 'Jobs', tab: TAB.UPDATES,
      from: /(jobstreet|indeed|glassdoor|hiredly|maukerja|jobs-noreply@linkedin|jobalerts-noreply@linkedin|workday|greenhouse|lever\.co|smartrecruiters)/i,
      subject: /\b(job alert|jobs for you|new jobs|application (received|update)|your application|interview)\b/i,
    },
    {
      label: 'Notices', tab: TAB.UPDATES,
      from: /(github|gitlab|bitbucket|vercel|netlify|render\.com|railway\.app|heroku|supabase|firebase|cloudplatform|amazonaws|aws\.amazon|azure|cloudflare|digitalocean|replit|docker|npmjs|sentry|atlassian|slack|notion|zoom\.us|calendly|dropbox|microsoft|apple\.com|google\.com)/i,
      subject: /\b(terms of service|privacy policy|policy update|updates? to our terms|scheduled maintenance|service (update|notice))\b/i,
    },

    // ── Social ──
    {
      label: 'Social', tab: TAB.SOCIAL,
      from: /(facebookmail|instagram|linkedin|twitter|\bx\.com|tiktok|pinterest|reddit|quora|discord|snapchat|threads\.net|youtube|telegram|whatsapp|tumblr|meetup|strava)/i,
    },

    // ── Newsletters (before Promotions, so digests aren't treated as ads) ──
    {
      label: 'Newsletters', tab: TAB.UPDATES,
      from: /(substack|beehiiv|medium\.com|mailchimp|convertkit|ghost\.io|buttondown)/i,
      subject: /(\[[^\]]*\bnews\b[^\]]*\]|\b(newsletter|digest|weekly (roundup|recap)|this week in|monthly (update|recap)|issue #?\d+|what'?s new in)\b)/i,
    },

    // ── Promotions ──
    {
      label: 'Ads & Promotions', tab: TAB.PROMOTIONS, bulkOnly: true,   // never for personal mail
      subject: /(\d+\s?% off|\b(sale|flash sale|mega sale|deals?|discount|voucher|coupon|promo( code)?|limited time|last chance|ends (tonight|today|soon)|don'?t miss|free shipping|cashback|exclusive offer|special offer|giveaway|webinar|misses you|we miss you|come back|haven'?t (finished|explored|seen)|still interested|jualan|diskaun|baucar|tawaran|percuma)\b)/i,
      // Typical marketing senders: marketing@, offers@, news@ … or mail./email./engage./news. subdomains
      from: /(\b(marketing|promo(tions)?|offers?|deals|news|newsletter|campaign|mailer|edm|hello|info)@|@(mail|email|e|em|news|engage|marketing|promo|go|info|m|t|mkt)\.[a-z0-9-]+\.[a-z])/i,
    },
  ],

  // Nothing matched: bulk mail → Forums + this label; anything else (probably
  // a real person) → Primary with no label.
  review: { label: 'Review needed', tab: TAB.FORUMS },
};

// ─── Run these (from the toolbar, or from Wrapper.gs) ───────────────────────

/** Shows where your latest 30 inbox emails would go. Changes nothing. */
function preview(config) {
  const c = config_(config);
  const rows = GmailApp.search('in:inbox', 0, 30).map(t => {
    const d = decide_(describe_(t), c);
    const mail = describe_(t);
    return `${pad_(d.tabName, 10)} ${pad_(d.label || '—', 20)} ${mail.from.slice(0, 40)} | ${mail.subject.slice(0, 60)}`;
  });
  console.log('TAB        LABEL                FROM | SUBJECT\n' + rows.join('\n'));
}

/** Creates labels, sorts recent mail now, and starts the schedule. */
function setup(config) {
  const c = config_(config);
  stop();
  labelIds_(c);
  scheduleTrigger_(c);
  sortNewMail(config);
  console.log(`Schedule set: ${JSON.stringify(c.settings.schedule)}. Run "stop" to turn it off.`);
}

/** Sorts unsorted inbox mail from the last `lookBackDays`, in batches until done. */
function sortNewMail(config) {
  const c = config_(config);
  const left = sort_(`in:inbox newer_than:${c.settings.lookBackDays}d -label:${c.settings.doneLabel}`, c);
  clearTriggers_('continueSorting');
  if (left) ScriptApp.newTrigger('continueSorting').timeBased().after(60 * 1000).create();
}
function continueSorting(config) { sortNewMail(config); }

/** Sorts every unsorted email in the inbox, in batches until done. */
function sortWholeInbox(config) {
  const c = config_(config);
  const left = sort_(`in:inbox -label:${c.settings.doneLabel}`, c);
  clearTriggers_('sortWholeInbox');
  if (left) ScriptApp.newTrigger('sortWholeInbox').timeBased().after(60 * 1000).create();
  else console.log('Whole inbox sorted.');
}

/** Turns automatic sorting off. Labels and sorted mail stay as they are. */
function stop() {
  ['sortNewMail', 'continueSorting', 'sortWholeInbox'].forEach(clearTriggers_);
}

// ─── Internals ──────────────────────────────────────────────────────────────

/** Merges a caller's config over the defaults. Ignores trigger event objects. */
function config_(override) {
  const o = (override && (override.settings || override.rules || override.alwaysPrimary ||
             override.alwaysPromotions || override.review)) ? override : {};
  return {
    settings: Object.assign({}, CONFIG.settings, o.settings || {}),
    alwaysPrimary: o.alwaysPrimary || CONFIG.alwaysPrimary,
    alwaysPromotions: o.alwaysPromotions || CONFIG.alwaysPromotions,
    rules: o.rules || CONFIG.rules,
    review: o.review || CONFIG.review,
  };
}

function sort_(query, c) {
  const ids = labelIds_(c);
  const threads = GmailApp.search(query, 0, c.settings.batchSize);
  const counts = {};
  threads.forEach(t => {
    const d = decide_(describe_(t), c);
    const add = [d.tab, ids[c.settings.doneLabel]];
    if (d.label && c.settings.addLabels) add.push(ids[d.label]);
    if (d.important) add.push('IMPORTANT');
    const remove = Object.values(TAB).filter(x => x !== d.tab);
    Gmail.Users.Threads.modify({ addLabelIds: add, removeLabelIds: remove }, 'me', t.getId());
    const key = `${d.tabName} / ${d.label || 'no label'}`;
    counts[key] = (counts[key] || 0) + 1;
  });
  console.log(`Sorted ${threads.length} conversations:\n` +
    Object.entries(counts).map(([k, n]) => `  ${n}  ${k}`).join('\n'));
  return threads.length === c.settings.batchSize;   // true = probably more left
}

function describe_(thread) {
  const msgs = thread.getMessages();
  const last = msgs[msgs.length - 1];
  const me = Session.getActiveUser().getEmail().toLowerCase();
  return {
    from: last.getFrom(),
    subject: thread.getFirstMessageSubject() || '',
    isBulk: !!last.getHeader('List-Unsubscribe'),
    iReplied: !!me && msgs.some(m => m.getFrom().toLowerCase().includes(me)),
  };
}

function decide_(mail, c) {
  const from = mail.from.toLowerCase();
  const name = tab => Object.keys(TAB).find(k => TAB[k] === tab);
  const out = (tab, label, important) => ({ tab, tabName: name(tab), label, important: !!important });

  if (mail.iReplied || c.alwaysPrimary.some(s => from.includes(s.toLowerCase()))) return out(TAB.PRIMARY, null);
  if (c.alwaysPromotions.some(s => from.includes(s.toLowerCase()))) return out(TAB.PROMOTIONS, 'Ads & Promotions');
  for (const r of c.rules) {
    const hit = (r.from && r.from.test(mail.from)) || (r.subject && r.subject.test(mail.subject));
    if (r.bulkOnly && !mail.isBulk) continue;
    if (hit && !(r.unless && r.unless.test(mail.subject))) return out(r.tab, r.label, r.important);
  }
  return mail.isBulk ? out(c.review.tab, c.review.label) : out(TAB.PRIMARY, null);
}

function labelIds_(c) {
  const wanted = new Set([c.settings.doneLabel, c.review.label, ...c.rules.map(r => r.label)]);
  if (wanted.has('Ads & Promotions') === false) wanted.add('Ads & Promotions');
  const existing = {};
  (Gmail.Users.Labels.list('me').labels || []).forEach(l => existing[l.name] = l.id);
  wanted.forEach(name => {
    if (existing[name]) return;
    const hidden = name === c.settings.doneLabel;
    existing[name] = Gmail.Users.Labels.create({
      name,
      labelListVisibility: hidden ? 'labelHide' : 'labelShow',
      messageListVisibility: hidden ? 'hide' : 'show',
    }, 'me').id;
  });
  return existing;
}

function scheduleTrigger_(c) {
  const s = c.settings.schedule, h = c.settings.atHour;
  const t = ScriptApp.newTrigger('sortNewMail').timeBased();
  if (s.minutes) t.everyMinutes(s.minutes);
  else if (s.hours) t.everyHours(s.hours);
  else if (s.days) t.everyDays(s.days).atHour(h);
  else if (s.weeks) t.everyWeeks(s.weeks).onWeekDay(ScriptApp.WeekDay.MONDAY).atHour(h);
  else if (s.months) t.onMonthDay(1).atHour(h);
  else throw new Error('settings.schedule needs minutes, hours, days, weeks or months');
  t.create();
}

function clearTriggers_(fn) {
  ScriptApp.getProjectTriggers().filter(t => t.getHandlerFunction() === fn).forEach(t => ScriptApp.deleteTrigger(t));
}

function pad_(s, n) { return (s + ' '.repeat(n)).slice(0, n); }

/** For library users: the default config, to copy and change. */
function defaultConfig() { return config_({}); }

/** For library users: tab ids, e.g. TabTidy.tabs().PROMOTIONS */
function tabs() { return TAB; }
