from baseelement import BaseElement
from example.pages.header import Header
from example.locators.cart import CartLocator


class Cart(Header):
    def __init__(self, driver, log, allure):
        super().__init__(driver, log, allure)
        self.__continue = BaseElement(driver, CartLocator.continue_button, log)
        self.__checkout = BaseElement(driver, CartLocator.checkout_button, log)
        self.__set_element()
        msg = "Enter to cart page"
        with self.allure.step(msg):
            self.allure.attach_image(self.driver, msg)

    def __set_element(self):
        self.__cart_items = self.get_elements(
            self.driver, CartLocator.cart_items, self.log
        )
        self.__item_quantity = self.get_elements(
            self.driver, CartLocator.item_quantity, self.log
        )
        self.__item_remove = self.get_elements(
            self.driver, CartLocator.item_remove, self.log
        )

    def remove(self, position):
        msg = "Remove an element"
        with self.allure.step(msg):
            self.__item_remove[position].click()
            self.__set_element()
            self.allure.attach(self.driver, msg)

    def select_continue(self):
        self.__continue.click()

    def select_checkout(self):
        self.__checkout.click()

    # GETS

    def get_item_quantity(self, position):
        return self.__item_quantity[position].text

    def get_list_quantity(self):
        return len(self.__cart_items)
