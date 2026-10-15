# Playwright Python Test Script

## What this script does

`tests/test_playwright_test_script.py` is an end-to-end test script 
written in Python for Playwright of the TodoMVC demo app 
(https://demo.playwright.dev/todomvc). It exercises a full item 
lifecycle:

1. Opens the TodoMVC page and verifies it loaded (checks for the "todos" heading).
2. Adds a "Get milk" item via the textbox + Enter key, and verifies it appears.
3. Clicks the **Active** filter — verifies the item is visible.
4. Clicks the **Completed** filter — verifies the item is hidden (it's not completed yet).
5. Clicks the **All** filter, then checks the item's checkbox to complete it.
6. Clicks **Active** — verifies the completed item is now hidden.
7. Clicks **Completed** — verifies the item is visible again.
8. Clicks the item's **delete (×) button** — verifies the item is gone.

Concepts demonstrated: navigation, role/text/XPath locators, keyboard input,
checkboxes, auto-retrying `expect` assertions, and filter-state verification.

## Prerequisites

Python must be installed (it can be installed as extension in VS Code IDE).

```bash
# inside the project folder, with the virtual environment active
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium   # and/or: playwright install firefox
```

## Running the test

```bash
# Default run (headless Chromium, no tracing)
pytest tests/test_playwright_test_script.py

# Show the browser window while it runs (headed = the opposite of headless)
pytest tests/test_playwright_test_script.py --headed

# Slow each action down by 500 ms so you can follow along
pytest tests/test_playwright_test_script.py --headed --slowmo 500
```

## Tracing on / off

```bash
# Record a trace for every test
pytest tests/test_playwright_test_script.py --tracing on

# Keep traces only for FAILED tests (saves disk space)
pytest tests/test_playwright_test_script.py --tracing retain-on-failure

# No tracing (default)
pytest tests/test_playwright_test_script.py --tracing off
```

Traces are saved per test under `test-results/`, one `trace.zip` per test,
e.g. `test-results/tests-test_playwright_test_script-py-test_start-chromium/trace.zip`.

## Different browsers

```bash
pytest tests/test_playwright_test_script.py --browser chromium
pytest tests/test_playwright_test_script.py --browser firefox
pytest tests/test_playwright_test_script.py --browser webkit
```

(Chromium is the default. Install each engine first with
`playwright install <name>`.)

## Browser channels

Channels run the test in a *branded* browser installed on your system
instead of Playwright's bundled build (Chromium only):

```bash
pytest tests/test_playwright_test_script.py --browser chromium --browser-channel chrome
pytest tests/test_playwright_test_script.py --browser chromium --browser-channel msedge
```

Other channels: `chrome-beta`, `chrome-dev`, `chrome-canary`,
`msedge-beta`, `msedge-dev`, `msedge-canary`. The branded browser must be
installed on the machine.

## Combining options

Flags can be combined freely, e.g. watch a traced Firefox run in slow motion:

```bash
pytest tests/test_playwright_test_script.py --browser firefox --headed --slowmo 500 --tracing on
```

## Viewing a trace log

```bash
# List the per-test result folders to find your trace
ls test-results/

# Open a trace in the Trace Viewer (Tab-completion helps with the folder name)
playwright show-trace test-results/<folder-name>/trace.zip
```

The Trace Viewer shows a timeline of every action, before/after screenshots,
DOM snapshots, network activity, and console output — everything needed to
debug a failure after the fact.
