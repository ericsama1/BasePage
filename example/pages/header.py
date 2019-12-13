from basepage import BasePage
from baseelement import BaseElement
from example.locators.header import HeaderLocator


class Header(BasePage):
    def __init__(self, driver, log, allure):
        super().__init__(driver, log, allure)
        self.__logo = BaseElement(driver, HeaderLocator.logo, log)
        self.__menu = BaseElement(driver, HeaderLocator.menu, log)
        self.__cart = BaseElement(driver, HeaderLocator.cart, log)

        # Menu options
        self.__all_item = BaseElement(driver, HeaderLocator.all_item, log, 0)
        self.__about = BaseElement(driver, HeaderLocator.about, log, 0)
        self.__logout = BaseElement(driver, HeaderLocator.logout, log, 0)
        self.__reset = BaseElement(driver, HeaderLocator.reset, log, 0)
        self.__close_menu = BaseElement(
            driver, HeaderLocator.close_menu, log, 0
        )

    def select_menu(self):
        """
        Select the menu button.
        """
        msg = "Click on menu button"
        with self.allure.step(msg):
            self.__menu.click()
            self.allure.attach_image(msg)

    def select_cart(self):
        """
        Select the cart button
        """
        msg = "Click on cart button"
        with self.allure.step(msg):
            self.__cart.click()

    def select_all_items(self):
        """
        Select 'all items' option in the menu.
        """
        msg = "Click on 'all items' option"
        with self.allure.step(msg):
            self.select_menu()
            self.__all_item.wait(5)
            self.__all_item.click()

    def select_about(self):
        """
        Select 'select about' option in the menu.
        """
        msg = "Click on 'select about' option"
        with self.allure.step(msg):
            self.select_menu()
            self.__about.wait(5)
            self.__about.click()

    def select_logout(self):
        """
        Select 'logout' option in the menu.
        """
        msg = "Click on 'logout' option"
        with self.allure.step(msg):
            self.select_menu()
            self.__logout.wait(5)
            self.__logout.click()

    def select_reset(self):
        """
        Select 'reset' option in the menu.
        """
        msg = "Click on 'reset' option"
        with self.allure.step(msg):
            self.select_menu()
            self.__reset.wait(5)
            self.__reset.click()

    def close_menu(self):
        """
        Select the button to close the menu.
        """
        msg = "Close menu"
        with self.allure.step(msg):
            self.__close_menu.wait(5)
            self.__close_menu.click()
            self.allure.attach_image(self.driver, msg)
