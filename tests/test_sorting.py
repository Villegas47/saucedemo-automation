from playwright.sync_api import Page, expect

def test_sort_products_by_name_za(page: Page):
    # Log in
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Sort products Z to A using the dropdown
    page.select_option("[data-test='product-sort-container']", "za")

    # The first product should now be the last one alphabetically
    first_item = page.locator(".inventory_item_name").first
    expect(first_item).to_have_text("Test.allTheThings() T-Shirt (Red)")