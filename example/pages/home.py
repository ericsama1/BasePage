# from basepage import BasePage
# from baseelement import BaseElement
from baseselect import BaseSelect
from example.pages.header import Header
from example.locators.home import HomeLocator


class Home(Header):
    def __init__(self, driver, log):
        """Inicialize the Home page, finding all element in the page

        Arguments:
            BasePage {BasePage} -- Inherit BasePage's method
            driver {Webdriver} -- Webdriver to use
            log {log} -- Logger
        """
        super().__init__(driver, log)
        self.__product_sort = BaseSelect(driver, HomeLocator.product_sort, log)
        self.__products = self.get_elements(
            driver, HomeLocator.product_list, log)
        self.__products_add_cart = self.get_elements(
            driver, HomeLocator.products_add_cart, log)

    def select_sort_by_name_ascendant(self):
        """
        Select the ascendant name sort option.
        """
        self.__product_sort.select_by_text('Name (A to Z)')

    def select_sort_by_name_descendant(self):
        """
        Select the descendant name sort option.
        """
        self.__product_sort.select_by_text('Name (Z to A)')

    def select_sort_by_price_ascendant(self):
        """
        Select the ascendant price sort option.
        """
        self.__product_sort.select_by_text('Price (low to high)')

    def select_sort_by_price_descendant(self):
        """
        Select the descendant price sort option.
        """
        self.__product_sort.select_by_text('Price (high to low)')

    def add_cart(self, position):
        """Select the button add to cart on the item

        Arguments:
            position {integer} -- Position of the element to add to cart
        """
        elem = self.__products_add_cart[position]
        elem.click()

    def all_to_cart(self):
        """
        Select all item to add to cart.
        """
        c = len(self.__products_add_cart)
        for x in range(c):
            self.add_cart(x)
