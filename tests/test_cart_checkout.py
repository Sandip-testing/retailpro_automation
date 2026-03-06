import os
import allure
from datetime import datetime
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config_reader import get_config_value


# 1️⃣ VALID LOGIN TEST
# -------------------------
# @allure.feature("Login Feature")
# @allure.story("Valid Login")
# def test_valid_login(driver):
#
#     login_page = LoginPage(driver)
#     home_page = HomePage(driver)
#
#     login_page.login(
#         get_config_value("username"),
#         get_config_value("password")
#     )
#
#     assert "Products" in home_page.verify_home_page()
#
#     # Manual screenshot for success
#     os.makedirs("screenshots", exist_ok=True)
#     screenshot_path = "screenshots/valid_login.png"
#     driver.save_screenshot(screenshot_path)
#
#     allure.attach.file(
#         screenshot_path,
#         name="Valid Login Screenshot",
#         attachment_type=allure.attachment_type.PNG    )


# -------------------------# 2️⃣ INVALID LOGIN TEST
# -------------------------
@allure.feature("Login Feature")
@allure.story("Invalid Login")
def test_invalid_login(driver):

    login_page = LoginPage(driver)

    login_page.login("invalid_user", "wrong_password")

    assert "Epic sadface" in login_page.get_error_message()

    # Manual screenshot
    os.makedirs("screenshots", exist_ok=True)
    screenshot_path = "screenshots/invalid_login.png"
    driver.save_screenshot(screenshot_path)

    allure.attach.file(
        screenshot_path,
        name="Invalid Login Screenshot",
        attachment_type=allure.attachment_type.PNG
    )

def take_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(path)

    allure.attach.file(
        path,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


@allure.feature("E2E Order Flow")
@allure.story("Complete Order")
def test_complete_order_flow(driver):

    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # 1️⃣ Login
    login_page.login(
        get_config_value("username"),
        get_config_value("password")
    )

    assert "Products" in home_page.verify_home_page()
    take_screenshot(driver, "01_after_login")

    # 2️⃣ Add Product
    product_name = "Sauce Labs Backpack"
    home_page.add_product_by_name(product_name)
    take_screenshot(driver, "02_after_add_product")

    # 3️⃣ Go to Cart
    home_page.go_to_cart()
    cart_page = CartPage(driver)

    assert product_name in cart_page.get_cart_item()
    take_screenshot(driver, "03_cart_page")

    # 4️⃣ Checkout Page
    cart_page.click_checkout()
    take_screenshot(driver, "04_checkout_info_page")

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_details("John", "Doe", "411001")
    take_screenshot(driver, "05_checkout_overview")

    # 5️⃣ Finish Order
    checkout_page.finish_order()

    assert "Thank you for your order!" in checkout_page.get_success_message()
    take_screenshot(driver, "06_order_success")




# Old code

# from pages.cart_page import CartPage
# from pages.checkout_page import CheckoutPage
# from pages.home_page import HomePage
# from pages.login_page import LoginPage
# from utils.config_reader import get_config_value
#
#
# def test_complete_order_flow(driver):
#
#     login_page = LoginPage(driver)
#     home_page = HomePage(driver)
#
#     login_page.login(
#         get_config_value("username"),
#         get_config_value("password")
#     )
#
#     assert "Products" in home_page.verify_home_page()
#
#     # Add Product
#     product_name = "Sauce Labs Backpack"
#     home_page.add_product_by_name(product_name)
#
#     home_page.go_to_cart()
#
#     cart_page = CartPage(driver)
#     assert product_name in cart_page.get_cart_item()
#
#     cart_page.click_checkout()
#
#     checkout_page = CheckoutPage(driver)
#     checkout_page.enter_checkout_details("John", "Doe", "411001")
#     checkout_page.finish_order()
#
#     assert "Thank you for your order!" in checkout_page.get_success_message()


# New code

# import os
# import allure
# from pages.cart_page import CartPage
# from pages.checkout_page import CheckoutPage
# from pages.home_page import HomePage
# from pages.login_page import LoginPage
# from utils.config_reader import get_config_value
#
#
# # -------------------------
# # 1️⃣ VALID LOGIN TEST
# # -------------------------
# @allure.feature("Login Feature")
# @allure.story("Valid Login")
# def test_valid_login(driver):
#
#     login_page = LoginPage(driver)
#     home_page = HomePage(driver)
#
#     login_page.login(
#         get_config_value("username"),
#         get_config_value("password")
#     )
#
#     assert "Products" in home_page.verify_home_page()
#
#     # Manual screenshot for success
#     os.makedirs("screenshots", exist_ok=True)
#     screenshot_path = "screenshots/valid_login.png"
#     driver.save_screenshot(screenshot_path)
#
#     allure.attach.file(
#         screenshot_path,
#         name="Valid Login Screenshot",
#         attachment_type=allure.attachment_type.PNG
#     )
#
#
# # -------------------------
# # 2️⃣ INVALID LOGIN TEST
# # -------------------------
# @allure.feature("Login Feature")
# @allure.story("Invalid Login")
# def test_invalid_login(driver):
#
#     login_page = LoginPage(driver)
#
#     login_page.login("invalid_user", "wrong_password")
#
#     assert "Epic sadface" in login_page.get_error_message()
#
#     # Manual screenshot
#     os.makedirs("screenshots", exist_ok=True)
#     screenshot_path = "screenshots/invalid_login.png"
#     driver.save_screenshot(screenshot_path)
#
#     allure.attach.file(
#         screenshot_path,
#         name="Invalid Login Screenshot",
#         attachment_type=allure.attachment_type.PNG
#     )
#
#
# # -------------------------
# # 3️⃣ COMPLETE ORDER FLOW
# # -------------------------
# @allure.feature("E2E Order Flow")
# @allure.story("Complete Order")
# def test_complete_order_flow(driver):
#
#     login_page = LoginPage(driver)
#     home_page = HomePage(driver)
#
#     login_page.login(
#         get_config_value("username"),
#         get_config_value("password")
#     )
#
#     assert "Products" in home_page.verify_home_page()
#
#     # Add Product
#     product_name = "Sauce Labs Backpack"
#     home_page.add_product_by_name(product_name)
#     home_page.go_to_cart()
#
#     cart_page = CartPage(driver)
#     assert product_name in cart_page.get_cart_item()
#
#     cart_page.click_checkout()
#
#     checkout_page = CheckoutPage(driver)
#     checkout_page.enter_checkout_details("John", "Doe", "411001")
#     checkout_page.finish_order()
#
#     assert "Thank you for your order!" in checkout_page.get_success_message()
#
#     # Success screenshot
#     os.makedirs("screenshots", exist_ok=True)
#     screenshot_path = "screenshots/order_success.png"
#     driver.save_screenshot(screenshot_path)
#
#     allure.attach.file(
#         screenshot_path,
#         name="Order Success Screenshot",
#         attachment_type=allure.attachment_type.PNG
#     )


