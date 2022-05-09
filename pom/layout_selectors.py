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
#     page.goto("https://symonstorozhenko.wixsite.com/website-1", timeout=7000)
#     page.set_default_timeout(5000)
#
#     # Act \ When/And
#     # page.locator("p:has-text(\"Contact Us\")").click()
#     # time.sleep(5)  # page timeout in seconds
#     page.locator("text=Log In").click()
#     page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
#     page.locator("[data-testid=\"switchToEmailLink\"] >> [data-testid=\"buttonElement\"]").click()
#     # page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("test@test.com")
#     page.fill('input:below(:text("Email"))', "test@test.com")  # its the same as above but it's better to user this way
#     # page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").click()
#     # page.locator("input[type=\"password\"]").fill("Test1234")
#     page.fill('input:below(:text("Password"))', "Test1234") # the same as above, click on the input fild is extra
#     page.locator("[data-testid=\"submit\"] >> [data-testid=\"buttonElement\"]").click()
#     page.locator("[aria-label=\"test account menu\"]").click()
#
#     # Assertion / Then
#     assert page.is_visible("text= My Orders")
#
#     # # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
