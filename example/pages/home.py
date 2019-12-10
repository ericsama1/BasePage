from basepage import BasePage
from baseelement import BaseElement
from baseselect import BaseSelect
from example.locators.home import HomeLocator


class Home(BasePage):
    def __init__(self, driver, log):
        """Inicialize the Home page, finding all element in the page

        Arguments:
            BasePage {BasePage} -- Inherit BasePage's method
            driver {Webdriver} -- Webdriver to use
            log {log} -- Logger
        """
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

    def select_menu(self):
        """
        Select the menu button.
        """
        self.__menu.click()

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

    def select_all_items(self):
        """
        Select the option 'all items' in the menu.
        """
        self.select_menu()
        self.__all_item.click()

    def select_about(self):
        """
        Select the option 'select about' in the menu.
        """
        self.select_menu()
        self.__about.click()

    def select_logout(self):
        """
        Select the option 'logout' in the menu.
        """
        self.select_menu()
        self.__logout.click()

    def select_reset(self):
        """
        Select the option 'reset' in the menu.
        """
        self.select_menu()
        self.__reset.click()

    def close_menu(self):
        """
        Select the button to close the menu.
        """
        self.select_menu()
        self.close_menu()

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
