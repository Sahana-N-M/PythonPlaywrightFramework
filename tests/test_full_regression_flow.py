from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.test_data import generate_email


def test_full_regression_flow(page):
    home = HomePage(page)

    # Verify Home Page
    assert home.verify_home_page_loaded()

    # Login with invalid credentials (Negative test)
    home.click_signup_login()
    login = LoginPage(page)
    login.login("wrong@test.com", "wrongpass")
    assert "Your email or password is incorrect!" in login.get_error_message()

    # Go back Home
    page.goto("https://automationexercise.com")

    # Signup new user
    home = HomePage(page)
    home.click_signup_login()

    signup = SignupPage(page)
    signup.signup("Sahana", generate_email())

    # Validate signup page navigation
    assert "signup" in page.url

    # Go to Products and search product
    page.goto("https://automationexercise.com")
    home = HomePage(page)
    home.click_products()

    products = ProductsPage(page)
    products.search_product("Dress")

    # Add product to cart
    products.add_first_product_to_cart()

    # Go to Cart
    home.click_cart()

    cart = CartPage(page)
    assert cart.verify_product_added()

    # Proceed to Checkout
    cart.proceed_to_checkout()

    # Validate checkout/login redirect
    assert ("checkout" in page.url) or ("login" in page.url)