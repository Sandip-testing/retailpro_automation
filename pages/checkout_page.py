from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    success_message = (By.CLASS_NAME, "complete-header")

    def enter_checkout_details(self, fname, lname, zip_code):
        self.send_keys(self.first_name, fname)
        self.send_keys(self.last_name, lname)
        self.send_keys(self.postal_code, zip_code)
        self.click(self.continue_button)

    def finish_order(self):
        self.click(self.finish_button)

    def get_success_message(self):
        return self.get_text(self.success_message)