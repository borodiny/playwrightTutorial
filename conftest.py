import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(page):
    # # Assess - pre-requisites \ Given
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(5000)

    yield page
