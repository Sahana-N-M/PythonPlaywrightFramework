from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CHECKOUT_PAGE_TEXT = "li.active"
    DELIVERY_ADDRESS_BOX = "#address_delivery"
    BILLING_ADDRESS_BOX = "#address_invoice"

    COMMENT_TEXTAREA = "textarea[name='message']"
    PLACE_ORDER_BTN = "a[href='/payment']"

    def verify_checkout_page_loaded(self):
        # Checkout page shows "Checkout" in breadcrumb
        return self.is_visible(self.CHECKOUT_PAGE_TEXT)

    def verify_delivery_address_visible(self):
        return self.is_visible(self.DELIVERY_ADDRESS_BOX)

    def verify_billing_address_visible(self):
        return self.is_visible(self.BILLING_ADDRESS_BOX)

    def add_comment(self, comment):
        self.fill(self.COMMENT_TEXTAREA, comment)

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BTN)