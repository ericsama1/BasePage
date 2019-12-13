from basepage import BasePage
from baseelement import BaseElement
from example.locators.checkout import CheckoutLocator


class Checkout(BasePage):
    def __init__(self, driver, log, allure):
        super().__init__(driver, log, allure)
        self.__first_name = BaseElement(
            driver, CheckoutLocator.first_name, log)
        self.__last_name = BaseElement(driver, CheckoutLocator.last_name, log)
        self.__postal_code = BaseElement(
            driver, CheckoutLocator.postal_code, log)
        self.__cancel_button = BaseElement(driver, CheckoutLocator.cancel, log)
        self.__continue_button = BaseElement(
            driver, CheckoutLocator.continue_button, log)
        msg = "Enter to checkout page"
        with self.allure.step(msg):
            self.allure.attach_image(self.driver, msg)

    def write_first_name(self, name):
        msg = "Write firstname"
        with self.allure.step(msg):
            self.__first_name.send_keys(name)
            self.allure.attach_image(self.driver, msg)

    def write_last_name(self, lastname):
        msg = "Write lastname"
        with self.allure.step(msg):
            self.__last_name.send_keys(lastname)
            self.allure.attach_image(self.driver, msg)

    def write_postal_code(self, postal):
        msg = "Write postal code"
        with self.allure.step(msg):
            self.__postal_code.send_keys(postal)
            self.allure.attach_image(self.driver, msg)

    def select_cancel(self):
        msg = "Click on cancel button"
        with self.allure.step(msg):
            self.__cancel_button.click()

    def select_continue(self):
        msg = "Click on continue button"
        with self.allure.step(msg):
            self.__continue_button.click()

    def check_error(self, text):
        msg = "Checking error message"
        with self.allure.step(msg):
            self.__error_message = BaseElement(
                self.driver, CheckoutLocator.error_message, self.log)
            self.compare_text(self.__error_message, text)
            self.allure.attach_image(self.driver, msg)
