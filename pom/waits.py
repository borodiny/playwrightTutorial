import time

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    # Assess - pre-requisites \ Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # Custom time out
    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log In\")")
        else:
            login_issue = False
        time.sleep(0.1)

    page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
    page.locator("[data-testid=\"switchToEmailLink\"] >> [data-testid=\"buttonElement\"]").click()
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("test@test.com")
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").press("Tab")
    page.locator("input[type=\"password\"]").fill("Test1234")
    page.locator("[data-testid=\"submit\"] >> [data-testid=\"buttonElement\"]").click()
    page.locator("[aria-label=\"test account menu\"]").click()
    page.wait_for_load_state()
    page.wait_for_selector("[aria-label=\"test account menu\"]")
    assert page.is_visible("text= My Orders")



    # # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
