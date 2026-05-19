from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_login_with_invalid_credentials(page):
    home = HomePage(page)
    assert home.verify_home_page_loaded()

    home.click_signup_login()

    login = LoginPage(page)
    login.login("wrong@test.com", "wrongpass")

    assert "Your email or password is incorrect!" in login.get_error_message()