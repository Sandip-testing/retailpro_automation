from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    cart_item = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.ID, "checkout")

    def get_cart_item(self):
        return self.get_text(self.cart_item)

    def click_checkout(self):
        self.click(self.checkout_button)