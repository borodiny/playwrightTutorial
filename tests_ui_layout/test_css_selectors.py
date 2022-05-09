# import time
#
# import pytest
# from playwright.sync_api import Playwright, sync_playwright
#
#
# @pytest.mark.parametrize("email, password", [("test@test.com", "Test1234"),
#                                               pytest.param("fakeemail", "fakepass", marks=pytest.mark.xfail),
#                                               ("test@test", "Test1234")])
# def test_run(set_up, email, password) -> None:
#     page = set_up
#
#     # Act \ When/And
#     page.locator("p:has-text(\"Contact Us\")").click()
#     time.sleep(5)  # page timeout in seconds
#     page.locator("text=Log In").click()
#     page.locator("[data-testid=\"signUp\\.switchToSignUp\"]").click()
#     page.locator("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]").click()
#     page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").fill(email)
#     page.locator("[data-testid=\"emailAuth\"] input[type=\"email\"]").click()
#     page.locator("input[type=\"password\"]").fill(password)
#     page.locator("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]").click()
#     page.locator("[aria-label=\"test account menu\"]").click()
#
#     # Assertion / Then
#     assert page.is_visible("text= My Orders")
