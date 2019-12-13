import unittest
from settings import url
from basebrowser import BaseBrowser
from example.pages.login import Login
from example.pages.home import Home
from example.pages.cart import Cart
from example.data.login_data import LoginData
from helpers.log import DriverLog
from helpers.alluredriver import allure, Allure

log = DriverLog()
log = log.create_log()


@allure.feature('Cart')
class CartTest(unittest.TestCase):
    def setUp(self):
        self.done = False
        self.allure = Allure()
        browser = BaseBrowser(url, log)
        self.data = LoginData()
        self.driver, self.log = browser.get_driver()
        login = Login(self.driver, self.log, self.allure)
        login.login(self.data.get_user(), self.data.get_pass())
        home = Home(self.driver, self.log, self.allure)
        home.add_cart(0)
        home.select_cart()
        self.cart = Cart(self.driver, self.log, self.allure)

    def test_continue(self):
        self.cart.select_continue()
        Home(self.driver, self.log, self.allure)
        self.done = True

    def test_checkout(self):
        self.cart.select_checkout()
        self.done = True

    def test_all_items(self):
        self.cart.select_all_items()
        Home(self.driver, self.log, self.allure)
        self.done = True

    def test_remove(self):
        self.cart.remove(0)
        count = self.cart.get_list_quantity()
        assert count == 0, 'Hay mas elementos'
        self.done = True

    def tearDown(self):
        if self.done:
            self.log.info('The test has finished OK')
        else:
            self.log.error('The test hasn\'t finished OK')
        import time
        time.sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
