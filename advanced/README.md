# Advanced Percy on Automate + Selenium-Python

Exercises the full applicable Percy on Automate feature surface for `percy-selenium` (Python, Automate mode).

## What this example covers

A pytest suite (`tests/test_advanced.py`) where each test exercises one row of the Percy on Automate matrix: ignore regions (xpath / CSS selector / custom bbox), consider regions (xpath / CSS selector), freeze_animation, percy_css, sync mode, test_case + labels.

DOM-only options marked `N/A` in `matrix.yml`.

## Run locally

```bash
cd advanced
make install
export BROWSERSTACK_USERNAME="<your username>"
export BROWSERSTACK_ACCESS_KEY="<your access key>"
export PERCY_TOKEN="<your project token>"
make test
```

## CI note

`workflow_dispatch`-only — Percy on Automate CI requires a real BrowserStack Automate session.

## Coverage matrix

Source of truth: [`matrix.yml`](./matrix.yml).
