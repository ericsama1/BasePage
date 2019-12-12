import unittest
import allure
from settings import url
from basebrowser import BaseBrowser
from example.pages.login import Login
from example.pages.home import Home
from example.data.login_data import LoginData
from helpers.log import DriverLog

log = DriverLog()
log = log.create_log()


@allure.feature('Login')
class LoginTest(unittest.TestCase):
    def setUp(self):
        browser = BaseBrowser(url, log)
        self.data = LoginData()
        self.driver, self.log = browser.get_driver()
        self.login = Login(self.driver, self.log)

    @allure.title('Locked User')
    def test_locked_user(self):
        self.login.login(self.data.get_locked_user(), self.data.get_pass())
        text = self.data.get_locked_message()
        self.login.verify_locked(text)

    @allure.title('Correct Login')
    def test_user(self):
        self.login.login(self.data.get_user(), self.data.get_pass())
        Home(self.driver, self.log)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
