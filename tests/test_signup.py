from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.test_data import generate_email

def test_signup_new_user(page):
    home = HomePage(page)
    home.click_signup_login()

    signup = SignupPage(page)
    signup.signup("Sahana", generate_email())

    assert page.url.__contains__("signup")