from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_cart_checkout_flow(page):
    home = HomePage(page)

    assert home.verify_home_page_loaded()

    home.click_products()

    products = ProductsPage(page)

    products.search_product("Dress")

    products.add_first_product_to_cart()

    home.click_cart()

    cart = CartPage(page)

    assert cart.verify_product_added()

    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)

    # If user is not logged in, it will redirect to login page
    assert ("checkout" in page.url) or ("login" in page.url)

    # If checkout page opened, validate address sections
    if "checkout" in page.url:
        assert checkout.verify_delivery_address_visible()
        assert checkout.verify_billing_address_visible()