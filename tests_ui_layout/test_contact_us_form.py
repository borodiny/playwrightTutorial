import time

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

from pom.contact_us_page import ContactUsPage

# two or more markers could be added to the test
@pytest.mark.smoke
@pytest.mark.regression
def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Yevhen", "11 street", "test@test.com", "1234567890", "subject", "message")


@pytest.mark.skip(reason="form is not ready")
def test_submit_form2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Yevhen", "11 street", "test@test.com", "1234567890", "subject", "message")


@pytest.mark.regression
def test_submit_form3(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Yevhen", "11 street", "test@test.com", "1234567890", "subject", "message")


@pytest.mark.xfail(reason="url is not ready")
def test_run2(set_up) -> None:
    page = set_up

    # Act \ When/And
    page.locator("p:has-text(\"Contact Us\")").click()
    time.sleep(5)  # page timeout in seconds
    page.locator("text=Log In").click()
    page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
    page.locator("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]").click()
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("test@test.com")
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").click()
    page.locator("input[type=\"password\"]").fill("Test1234")
    page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()
    page.locator("[aria-label=\"test account menu\"]").click()

    # Assertion / Then
    assert page.is_visible("text= My Orders")