from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_search_and_add_product_to_cart(page):
    home = HomePage(page)
    home.click_products()

    products = ProductsPage(page)
    products.search_product("Dress")
    products.add_first_product_to_cart()

    home.click_cart()

    cart = CartPage(page)
    assert cart.verify_product_added()