from pages.base_page import BasePage


class CartPage(BasePage):

    CART_PRODUCT_ROW = "tr[id^='product-']"
    PROCEED_TO_CHECKOUT_BTN = "a.btn.btn-default.check_out"
    REGISTER_LOGIN_BTN = "u:has-text('Register / Login')"

    def verify_product_added(self):
        return self.page.locator(self.CART_PRODUCT_ROW).count() > 0

    def proceed_to_checkout(self):
        # Scroll and click Proceed to Checkout
        self.page.locator(self.PROCEED_TO_CHECKOUT_BTN).scroll_into_view_if_needed()
        self.page.locator(self.PROCEED_TO_CHECKOUT_BTN).click()

        # If popup appears, click Register/Login
        if self.page.locator(self.REGISTER_LOGIN_BTN).is_visible():
            self.page.locator(self.REGISTER_LOGIN_BTN).click()