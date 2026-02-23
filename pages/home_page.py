from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    page_title = (By.CLASS_NAME, "title")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def verify_home_page(self):
        return self.get_text(self.page_title)

    def add_product_by_name(self, product_name):
        add_button = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        )
        self.click(add_button)

    def go_to_cart(self):
        self.click(self.cart_icon)