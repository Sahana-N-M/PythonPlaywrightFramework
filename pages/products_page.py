from pages.base_page import BasePage


class ProductsPage(BasePage):

    SEARCH_BOX = "#search_product"
    SEARCH_BTN = "#submit_search"

    FIRST_PRODUCT_CARD = "(//div[@class='product-image-wrapper'])[1]"
    FIRST_ADD_TO_CART = "(//div[@class='product-image-wrapper'])[1]//a[contains(text(),'Add to cart')]"

    CONTINUE_SHOPPING_BTN = "button.btn.btn-success.close-modal"

    def search_product(self, product_name):
        self.fill(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BTN)

    def add_first_product_to_cart(self):
        
        self.page.locator(self.FIRST_PRODUCT_CARD).hover()

        
        self.page.locator(self.FIRST_ADD_TO_CART).first.click()

        
        self.page.locator(self.CONTINUE_SHOPPING_BTN).click()