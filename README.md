# automationtest

This repository contains helper scripts for recording browser interactions with Playwright.

## Setup

Install Playwright and its browsers:

```bash
pip install playwright
playwright install
```

## Recording actions

Use the recording script to launch the Playwright code generator for a URL:

```bash
python scripts/record_actions.py https://example.com
```

After recording your interactions, save the generated test file.

