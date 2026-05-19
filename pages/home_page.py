from pages.base_page import BasePage


class HomePage(BasePage):

    SIGNUP_LOGIN_BTN = "a[href='/login']"
    PRODUCTS_BTN = "a[href='/products']"
    CART_BTN = "a[href='/view_cart'] >> text=Cart"
    HOME_LOGO = "img[alt='Website for automation practice']"

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_BTN)

    def click_products(self):
        self.click(self.PRODUCTS_BTN)


    def click_cart(self):
        self.page.locator(self.CART_BTN).first.click()

    def verify_home_page_loaded(self):
        return self.is_visible(self.HOME_LOGO)