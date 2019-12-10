from basepage import BasePage
from baseelement import BaseElement
from example.locators.checkout import CheckoutLocator


class Checkout(BasePage):
    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.__first_name = BaseElement(
            driver, CheckoutLocator.first_name, log)
        self.__last_name = BaseElement(driver, CheckoutLocator.last_name, log)
        self.__postal_code = BaseElement(
            driver, CheckoutLocator.postal_code, log)
        self.__cancel_button = BaseElement(driver, CheckoutLocator.cancel, log)
        self.__continue_button = BaseElement(
            driver, CheckoutLocator.continue_button, log)

    def write_first_name(self, name):
        self.__first_name.send_keys(name)

    def write_last_name(self, lastname):
        self.__last_name.send_keys(lastname)

    def write_postal_code(self, postal):
        self.__postal_code.send_keys(postal)

    def select_cancel(self):
        self.__cancel_button.click()

    def select_continue(self):
        self.__continue_button.click()

    def check_error(self, text):
        self.__error_message = BaseElement(
            self.driver, CheckoutLocator.error_message, self.log)
        self.compare_text(self.__error_message, text)
