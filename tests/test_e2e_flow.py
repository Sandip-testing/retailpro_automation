import allure
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.logger import get_logger
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.config_reader import get_config_value


@allure.feature("E2E Order Flow")
@allure.story("Complete Order")
def test_complete_order_flow(driver):

    logger = get_logger("test_complete_order_flow")
    logger.info("Test started")

    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    logger.info("Logging in")
    login_page.login(
        get_config_value("username"),
        get_config_value("password")
    )

    assert "Products" in home_page.verify_home_page()
    logger.info("Login successful")

    product_name = "Sauce Labs Backpack"
    logger.info(f"Adding product: {product_name}")
    home_page.add_product_by_name(product_name)

    home_page.go_to_cart()
    cart_page = CartPage(driver)

    assert product_name in cart_page.get_cart_item()
    logger.info("Product verified in cart")

    cart_page.click_checkout()
    logger.info("Checkout page opened")

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_details("John", "Doe", "411001")
    logger.info("Checkout details entered")

    checkout_page.finish_order()

    assert "Thank you for your order!" in checkout_page.get_success_message()
    logger.info("Order completed successfully")

    logger.info("Test finished successfully")