
from basepage import BasePage
from baseelement import BaseElement
from baseselect import BaseSelect
from example.locators.home import HomeLocator


class Home(BasePage):
    def __init__(self, driver, log):
        self.__logo = BaseElement(driver, HomeLocator.logo, log)
        self.__menu = BaseElement(driver, HomeLocator.menu, log)
        self.__cart = BaseElement(driver, HomeLocator.cart, log)
        self.__product_sort = BaseSelect(driver, HomeLocator.product_sort, log)
        self.__products = self.get_elements(
            driver, HomeLocator.product_list, log)
        self.__products_add_cart = self.get_elements(
            driver, HomeLocator.products_add_cart, log)

        # Menu options
        self.__all_item = BaseElement(driver, HomeLocator.all_item, log, 0)
        self.__about = BaseElement(driver, HomeLocator.about, log, 0)
        self.__logout = BaseElement(driver, HomeLocator.logout, log, 0)
        self.__reset = BaseElement(driver, HomeLocator.reset, log, 0)
        self.__close_menu = BaseElement(driver, HomeLocator.close_menu, log, 0)

    def __get_elements(self, driver, by, log):
        element = driver.find_elements(*by)
        xpath = '(%s)[{}]' % by[1]
        elements = [
            BaseElement(driver, ('xpath', xpath.format(x + 1)), log)
            for x in range(len(element))
        ]
        return elements

    def select_menu(self):
        self.__menu.click()

    def select_sort_by_name_ascendant(self):
        self.__product_sort.select_by_text('Name (A to Z)')

    def select_sort_by_name_descendant(self):
        self.__product_sort.select_by_text('Name (Z to A)')

    def select_sort_by_price_ascendant(self):
        self.__product_sort.select_by_text('Price (low to high)')

    def select_sort_by_price_descendant(self):
        self.__product_sort.select_by_text('Price (high to low)')

    def select_all_items(self):
        self.select_menu()
        self.__all_item.click()

    def select_about(self):
        self.select_menu()
        self.__about.click()

    def select_logout(self):
        self.select_menu()
        self.__logout.click()

    def select_reset(self):
        self.select_menu()
        self.__reset.click()

    def close_menu(self):
        self.select_menu()
        self.close_menu()

    def add_cart(self, position):
        elem = self.__products_add_cart[position]
        elem.click()

    def all_to_cart(self):
        c = len(self.__products_add_cart)
        for x in range(c):
            self.add_cart(x)
