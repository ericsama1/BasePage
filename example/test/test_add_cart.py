import unittest
from settings import url
from basebrowser import BaseBrowser
from example.pages.login import Login
from example.pages.home import Home
from example.data.login_data import LoginData
from helpers.log import DriverLog

log = DriverLog()
log = log.create_log()


class SortTest(unittest.TestCase):
    def setUp(self):
        self.done = False
        browser = BaseBrowser(url, log)
        self.data = LoginData()
        self.driver, self.log = browser.get_driver()
        login = Login(self.driver, self.log)
        login.login(self.data.get_user(), self.data.get_pass())
        self.home = Home(self.driver, self.log)

    def test_add_a_product(self):
        self.log.info('Add product to cart')
        self.home.add_cart(0)
        self.done = True

    def test_add_all_products(self):
        self.log.info('Add all products')
        self.home.all_to_cart()
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
