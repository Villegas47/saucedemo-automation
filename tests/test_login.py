from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    # Go to the SauceDemo login page
    page.goto("https://www.saucedemo.com/")

    # Fill in username and password
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    # Click the login button
    page.click("#login-button")

    # Check we landed on the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")



def test_invalid_login(page: Page):
    # Go to the SauceDemo login page
    page.goto("https://www.saucedemo.com/")

    # Fill in a valid username but a WRONG password
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")

    # Click the login button
    page.click("#login-button")

    # Check the correct error message appears
    error = page.locator("[data-test='error']")
    expect(error).to_contain_text("Username and password do not match")



def test_locked_out_user(page: Page):
    # Go to the SauceDemo login page
    page.goto("https://www.saucedemo.com/")

    # Log in with the locked-out account
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")

    # Click the login button
    page.click("#login-button")

    # Check the locked-out error message appears
    error = page.locator("[data-test='error']")
    expect(error).to_contain_text("locked out")