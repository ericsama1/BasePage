import unittest
from settings import url
from basebrowser import BaseBrowser
from example.pages.login import Login
from example.pages.home import Home
from example.pages.cart import Cart
from example.pages.checkout import Checkout
from example.data.login_data import LoginData
from example.data.checkout_data import CheckoutData
from helpers.log import DriverLog
from helpers.alluredriver import allure, Allure

log = DriverLog()
log = log.create_log()


@allure.feature('Login')
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
        cart = Cart(self.driver, self.log, self.allure)
        cart.select_checkout()
        self.checkout = Checkout(self.driver, self.log, self.allure)
        self.data_check = CheckoutData()
        self.checkout.sleep(1)

    def test_complete_data(self):
        self.checkout.write_first_name(self.data_check.get_name())
        self.checkout.write_last_name(self.data_check.get_last_name())
        self.checkout.write_postal_code(self.data_check.get_postal_code())
        self.checkout.select_continue()
        self.done = True

    def test_name_error(self):
        self.checkout.select_continue()
        self.checkout.check_error(self.data_check.get_firstname_error())
        self.done = True

    def test_lastname_error(self):
        self.checkout.write_first_name(self.data_check.get_name())
        self.checkout.select_continue()
        self.checkout.check_error(self.data_check.get_lastname_error())
        self.done = True

    def test_postal_error(self):
        self.checkout.write_first_name(self.data_check.get_name())
        self.checkout.write_last_name(self.data_check.get_last_name())
        self.checkout.select_continue()
        self.checkout.check_error(self.data_check.get_postal_error())
        self.done = True

    def test_cancel(self):
        self.checkout.select_cancel()
        Cart(self.driver, self.log, self.allure)
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
