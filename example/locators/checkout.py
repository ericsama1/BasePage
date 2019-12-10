from selenium.webdriver.common.by import By


class CheckoutLocator():
    """
    Checkout page's element
    """
    # Input
    first_name = (By.ID, 'first-name')
    last_name = (By.ID, 'last-name')
    postal_code = (By.ID, 'postal-code')

    # Buttons
    cancel = (By.XPATH, "//a[@class='cart_cancel_link btn_secondary']")
    continue_button = (
        By.XPATH, "//input[@class='btn_primary cart_button']"
    )

    # Message
    error_message = (By.XPATH, "//h3[@data-test='error']")
