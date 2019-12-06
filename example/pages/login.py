from basepage import BasePage
from baseelement import BaseElement
from example.locators.login import LoginLocator


class Login(BasePage):
    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.__user = BaseElement(driver, LoginLocator.user, log)
        self.__password = BaseElement(driver, LoginLocator.passw, log)
        self.__login = BaseElement(driver, LoginLocator.login, log)

    def write_user(self, user):
        self.__user.send_keys(user)

    def write_pass(self, passw):
        self.__password.send_keys(passw)

    def click_login(self):
        self.__login.click()

    def login(self, user, passw):
        self.write_user(user)
        self.write_pass(passw)
        self.click_login()

    # Verify

    def verify_locked(self, text):
        self.__error = BaseElement(self.driver, LoginLocator.error, self.log)
        self.compare_text(self.__error, text)
