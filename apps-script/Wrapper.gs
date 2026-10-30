/**
 * Your own TabTidy project (library version).
 *
 * 1. New project at https://script.google.com
 * 2. Libraries (+) → paste the TabTidy Script ID → Look up →
 *    pick the latest version → identifier: TabTidy → Add
 *    Script ID: 1sj4sFD5amFGbVXBACvSlhsKh_RApKp3wfu7_1-1s6QHS1O-jAasOGwI7
 * 3. Services (+) → Gmail API → Add
 * 4. Paste this file, save, run `preview`, then `setup`.
 *
 * Keep the function names below exactly as they are: the schedule calls them.
 */

// Your settings. Anything you leave out uses the library's defaults.
const MY_CONFIG = {
  settings: {
    schedule: { minutes: 10 },   // or { hours: 1 }, { days: 1 }, { weeks: 1 }, { months: 1 }
    lookBackDays: 3,
    addLabels: true,             // false = only move mail between tabs
  },
  alwaysPrimary: [
    // 'boss@company.example',
  ],
  alwaysPromotions: [
    // 'shop-you-never-buy-from.example',
  ],
  // To change the rules themselves, see "Custom rules" in
  // docs/path-2-script-and-filters.md
};

function preview()        { TabTidy.preview(MY_CONFIG); }
function setup()          { TabTidy.setup(MY_CONFIG); }
function sortNewMail()    { TabTidy.sortNewMail(MY_CONFIG); }
function continueSorting(){ TabTidy.continueSorting(MY_CONFIG); }
function sortWholeInbox() { TabTidy.sortWholeInbox(MY_CONFIG); }
function stop()           { TabTidy.stop(); }
