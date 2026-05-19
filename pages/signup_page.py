from pages.base_page import BasePage

class SignupPage(BasePage):

    NAME_FIELD = "input[data-qa='signup-name']"
    EMAIL_FIELD = "input[data-qa='signup-email']"
    SIGNUP_BTN = "button[data-qa='signup-button']"

    ACCOUNT_CREATED_TEXT = "h2[data-qa='account-created']"
    CONTINUE_BTN = "a[data-qa='continue-button']"

    def signup(self, name, email):
        self.fill(self.NAME_FIELD, name)
        self.fill(self.EMAIL_FIELD, email)
        self.click(self.SIGNUP_BTN)

    def verify_account_created(self):
        return self.is_visible(self.ACCOUNT_CREATED_TEXT)