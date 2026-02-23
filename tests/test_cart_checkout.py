from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config_reader import get_config_value


def test_complete_order_flow(driver):

    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.login(
        get_config_value("username"),
        get_config_value("password")
    )

    assert "Products" in home_page.verify_home_page()

    # Add Product
    product_name = "Sauce Labs Backpack"
    home_page.add_product_by_name(product_name)

    home_page.go_to_cart()

    cart_page = CartPage(driver)
    assert product_name in cart_page.get_cart_item()

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_details("John", "Doe", "411001")
    checkout_page.finish_order()

    assert "Thank you for your order!" in checkout_page.get_success_message()