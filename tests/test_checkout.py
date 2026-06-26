from playwright.sync_api import Page, expect

def test_full_checkout(page: Page):
    # Log in
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Add the backpack and open the cart
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click("[data-test='shopping-cart-link']")

    # Start checkout
    page.click("[data-test='checkout']")

    # Fill in customer info
    page.fill("[data-test='firstName']", "Alexander")
    page.fill("[data-test='lastName']", "Villegas")
    page.fill("[data-test='postalCode']", "78209")
    page.click("[data-test='continue']")

    # Finish the purchase
    page.click("[data-test='finish']")

    # Assert we reached the order-confirmation page
    confirmation = page.locator("[data-test='complete-header']")
    expect(confirmation).to_have_text("Thank you for your order!")