from selenium.webdriver.common.by import By


class CartLocator():
    """
    Cart page's elements locator
    """
    # Items table
    cart_items = (By.XPATH, "//div[@class='cart_item']")
    item_quantity = (By.XPATH, "//div[@class='cart_quantity']")
    item_remove = (By.XPATH, "//div[@class='btn_secondary cart_button']")

    # Buttons
    continue_button = (
        By.XPATH, "//a[@class='btn_secondary' and text()='Continue Shopping']"
    )
    checkout_button = (By.XPATH, "//*[@class='btn_action checkout_button']")
