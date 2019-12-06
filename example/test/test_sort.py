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

    def test_sort_by_name_ascendant(self):
        self.log.info('Name Ascendant')
        self.home.select_sort_by_name_ascendant()
        self.done = True

    # def test_sort_by_name_descendant(self):
    #     self.log.info('Name Descendant')
    #     self.home.select_sort_by_name_descendant()
    #     self.done = True

    # def test_sort_by_price_ascendant(self):
    #     self.log.info('Price Ascendant')
    #     self.home.select_sort_by_price_ascendant()
    #     self.done = True

    # def test_sort_by_price_descendant(self):
    #     self.log.info('Price Descendant')
    #     self.home.select_sort_by_price_descendant()
    #     self.done = True

    def tearDown(self):
        if self.done:
            self.log.info('The test has finished OK')
        else:
            self.log.error('The test hasn\' finished OK')
        import time
        time.sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
