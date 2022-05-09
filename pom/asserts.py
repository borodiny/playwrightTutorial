from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Assess - pre-requisites \ Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    # Assertion / Then
    # assert page.is_visible("text= Celebrating Beauty and Style")   # Python-specific

    expect(page.locator("text= Celebrating Beauty and Style")).to_be_visible() # the same as above but in playwright style

    # # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
