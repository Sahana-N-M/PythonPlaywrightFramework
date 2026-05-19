from pages.base_page import BasePage

class LoginPage(BasePage):

    LOGIN_EMAIL = "input[data-qa='login-email']"
    LOGIN_PASSWORD = "input[data-qa='login-password']"
    LOGIN_BTN = "button[data-qa='login-button']"
    LOGOUT_BTN = "a[href='/logout']"
    ERROR_MSG = "p[style='color: red;']"

    def login(self, email, password):
        self.fill(self.LOGIN_EMAIL, email)
        self.fill(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def verify_logout_visible(self):
        return self.is_visible(self.LOGOUT_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)