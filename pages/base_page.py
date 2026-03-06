# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class BasePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def click(self, locator):
#         self.wait.until(EC.element_to_be_clickable(locator)).click()
#
#     def send_keys(self, locator, text):
#         self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
#
#     def get_text(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator)).text


import time
from utils.config_reader import get_bool_value, get_float_value
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def slow_down(self):
        if get_bool_value("slow_mode"):
            time.sleep(get_float_value("delay"))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        self.slow_down()

    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
        self.slow_down()

    def get_text(self, locator):
        text = self.wait.until(EC.visibility_of_element_located(locator)).text
        self.slow_down()
        return text