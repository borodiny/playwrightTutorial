from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    # Assess - pre-requisites \ Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500) #slow_mo - замедляет скорость отображения в эмуляторе
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)  # изменяет дефолтный таймаут

    # Act \ When/And
    # Click button:has-text("Log In")
    page.click("button:has-text(\"Log In\")", timeout=7000)  # задает таймаут только для отдельного экшена
    # Click [data-testid="signUp\.switchToSignUp"]
    page.click("[data-testid=\"signUp\\.switchToSignUp\"]")
    # Click [data-testid="switchToEmailLink"] [data-testid="buttonElement"]
    page.click("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]")
    # Fill [data-testid="emailAuth"] input[type="email"]
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill("test@test.com")
    # Press Tab
    page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").press("Tab")
    # Fill input[type="password"]
    page.locator("input[type=\"password\"]").fill("Test1234")
    # Click [data-testid="submit"] [data-testid="buttonElement"]
    page.click("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]")
    # Click [aria-label="test account menu"]
    page.click("[aria-label=\"test account menu\"]")

    # Assertion / Then
    assert page.is_visible("text= My Orders")  # the same as expected result




    # # Click text=My Orders
    # page.locator("text=My Orders").click()
    # # Go to https://symonstorozhenko.wixsite.com/website-1
    # page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # # Go to https://symonstorozhenko.wixsite.com/website-1/account/my-orders
    # page.goto("https://symonstorozhenko.wixsite.com/website-1/account/my-orders")
    # # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
