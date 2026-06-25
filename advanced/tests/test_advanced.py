"""PER-8195 Phase 3 — automate-selenium-python advanced example.

Each test exercises one row of the Percy on Automate matrix.
"""

from percy import percy_screenshot


def test_exercises_baseline(driver):
    percy_screenshot(driver, name="BStackDemo — baseline")


def test_exercises_ignore_region_xpaths(driver):
    percy_screenshot(
        driver,
        name="BStackDemo — ignore via xpath",
        ignore_region_xpaths=['//*[@id="signin"]'],
    )


def test_exercises_ignore_region_selectors(driver):
    percy_screenshot(
        driver,
        name="BStackDemo — ignore via CSS selector",
        ignore_region_selectors=["#signin", ".shelf-container-header"],
    )


def test_exercises_custom_ignore_regions(driver):
    percy_screenshot(
        driver,
        name="BStackDemo — custom ignore region",
        custom_ignore_regions=[{"top": 0, "bottom": 100, "left": 0, "right": 1280}],
    )


def test_exercises_consider_region_xpaths(driver):
    percy_screenshot(
        driver,
        name="BStackDemo — consider via xpath",
        consider_region_xpaths=['//*[@id="__next"]'],
    )


def test_exercises_consider_region_selectors(driver):
    percy_screenshot(
        driver,
        name="BStackDemo — consider via CSS selector",
        consider_region_selectors=["#__next > div > div > main"],
    )


def test_exercises_freeze_animation(driver):
    percy_screenshot(driver, name="BStackDemo — freeze_animation", freeze_animation=True)


def test_exercises_percy_css(driver):
    percy_screenshot(
        driver,
        name="BStackDemo — percy_css",
        percy_css=".shelf-container { background: #fffde7 !important; }",
    )


def test_exercises_sync_mode(driver):
    # sync=True blocks until Percy finishes the comparison and returns the result,
    # so we can consume it inline instead of polling the build separately.
    # With a full-access PERCY_TOKEN this is the comparison payload (a dict);
    # with a write-only token (common in CI) Percy responds 403 and the SDK
    # returns None. Both are valid, so don't couple the assertion to token
    # scope — just exercise the option and, when a payload is returned, check
    # it's structured data.
    result = percy_screenshot(driver, name="BStackDemo — sync", sync=True)
    print(f"Percy sync comparison result: {result}")
    assert result is None or isinstance(result, dict)


def test_exercises_test_case_and_labels(driver):
    percy_screenshot(
        driver,
        name="BStackDemo — test_case + labels",
        test_case="home-smoke",
        labels="smoke,automate-selenium-python",
    )
