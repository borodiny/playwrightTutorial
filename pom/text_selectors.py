# import time
#
# from playwright.sync_api import Playwright, sync_playwright
#
#
# def run(playwright: Playwright) -> None:
#     # Assess - pre-requisites \ Given
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)
#     context = browser.new_context()
#     # Open new page
#     page = context.new_page()
#     page.goto("https://symonstorozhenko.wixsite.com/website-1")
#     page.set_default_timeout(3000)
#
#     # Act \ When/And
#     # page.click("button:has-text(\"Log In\")", timeout=7000)
#
#     page.locator("text='Shop Women'").click()
#     time.sleep(5)  # page timeout in seconds
#     page.locator("text='Log In'").click()
#   #  page.click("'Log In'", timeout=7000)
#     page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
#     page.locator("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]").click()
#     page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("test@test.com")
#     page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").press("Tab")
#     page.locator("input[type=\"password\"]").fill("Test1234")
#     page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()
#     page.locator("[aria-label=\"test account menu\"]").click()
#
#     # Assertion / Then
#     assert page.is_visible("text= My Orders")
#
#
#
#
#     # # Click text=My Orders
#     # page.locator("text=My Orders").click()
#     # # Go to https://symonstorozhenko.wixsite.com/website-1
#     # page.goto("https://symonstorozhenko.wixsite.com/website-1")
#     # # Go to https://symonstorozhenko.wixsite.com/website-1/account/my-orders
#     # page.goto("https://symonstorozhenko.wixsite.com/website-1/account/my-orders")
#     # # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
