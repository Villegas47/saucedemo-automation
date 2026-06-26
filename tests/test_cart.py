from playwright.sync_api import Page, expect

def test_add_item_to_cart(page: Page):
    # Log in first
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Add the backpack to the cart
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")

    # The cart badge should now show "1"
    cart_badge = page.locator("[data-test='shopping-cart-badge']")
    expect(cart_badge).to_have_text("1")


def test_remove_item_from_cart(page: Page):
    # Log in first
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Add the backpack, then remove it
    page.click("[data-test='add-to-cart-sauce-labs-backpack']")
    page.click("[data-test='remove-sauce-labs-backpack']")

    # The cart badge should now be gone entirely
    cart_badge = page.locator("[data-test='shopping-cart-badge']")
    expect(cart_badge).not_to_be_visible()