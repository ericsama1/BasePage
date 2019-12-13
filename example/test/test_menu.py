import unittest
from settings import url
from basebrowser import BaseBrowser
from example.pages.login import Login
from example.pages.home import Home
from example.data.login_data import LoginData
from helpers.log import DriverLog
from helpers.alluredriver import allure, Allure

log = DriverLog()
log = log.create_log()


@allure.feature('Menu Test')
class MenuTest(unittest.TestCase):
    def setUp(self):
        self.done = False
        self.allure = Allure()
        browser = BaseBrowser(url, log)
        self.data = LoginData()
        self.driver, self.log = browser.get_driver()
        login = Login(self.driver, self.log, self.allure)
        login.login(self.data.get_user(), self.data.get_pass())
        self.home = Home(self.driver, self.log, self.allure)

    def test_all_items(self):
        self.log.info("Select the option 'All Items' in the menu")
        self.home.select_all_items()
        Home(self.driver, self.log, self.allure)
        self.done = True

    def test_about(self):
        self.log.info("Select the option 'About' in the menu")
        self.home.select_about()
        self.done = True

    def test_logout(self):
        self.log.info("Select the option 'Logout' in the menu")
        self.home.select_logout()
        Login(self.driver, self.log, self.allure)
        self.done = True

    def test_close_menu(self):
        self.log.info("Close the menu sidebar")
        self.home.select_menu()
        self.home.close_menu()
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
