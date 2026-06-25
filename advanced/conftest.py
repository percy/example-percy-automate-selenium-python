"""PER-8195 — pytest fixtures: BrowserStack Automate selenium driver."""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.set_capability(
        "bstack:options",
        {
            "os": "Windows",
            "osVersion": "11",
            "browserVersion": "latest",
            "projectName": os.environ.get("BROWSERSTACK_PROJECT_NAME", "Percy Automate Selenium-Python Advanced"),
            "buildName": os.environ.get("BROWSERSTACK_BUILD_NAME", "Advanced Selenium Python"),
            "sessionName": "advanced_visual_test",
            "userName": os.environ["BROWSERSTACK_USERNAME"],
            "accessKey": os.environ["BROWSERSTACK_ACCESS_KEY"],
        },
    )
    options.set_capability("browserName", "Chrome")
    drv = webdriver.Remote("https://hub-cloud.browserstack.com/wd/hub", options=options)
    drv.set_window_size(1280, 1024)
    drv.get("https://bstackdemo.com/")
    yield drv
    drv.quit()
