from basepage import BasePage
from baseelement import BaseElement
from example.locators.login import LoginLocator


class Login(BasePage):
    def __init__(self, driver, log, allure):
        """Inicialize the login page, finding all element in the page

        Arguments:
            BasePage {BasePage} -- Inherit BasePage's method
            driver {Webdriver} -- Webdriver to use
            log {log} -- Logger
        """
        super().__init__(driver, log, allure)
        self.__user = BaseElement(driver, LoginLocator.user, log)
        self.__password = BaseElement(driver, LoginLocator.passw, log)
        self.__login = BaseElement(driver, LoginLocator.login, log)

    def write_user(self, user):
        """Method to write the user in the user input

        Arguments:
            user {String} -- User
        """
        self.__user.send_keys(user)

    def write_pass(self, passw):
        """Method to write the password in the password input

        Arguments:
            passw {String} -- user's password
        """
        self.__password.send_keys(passw)

    def click_login(self):
        """
        Method to click the login button
        """
        self.__login.click()

    def login(self, user, passw):
        """Method to do the login

        Arguments:
            user {String} -- User
            passw {String} -- User's password
        """
        msg = "Has written the user {} and password.".format(user)
        with self.allure.step(msg):
            self.write_user(user)
            self.write_pass(passw)
            self.allure.attach_image(self.driver, msg)
        self.click_login()

    # Verify

    def verify_locked(self, text):
        """Method to check the locked message

        Arguments:
            text {String} -- Expected message
        """
        msg = "Se intenta visualizar el mensaje de error"
        with self.allure.step(msg):
            self.__error = BaseElement(
                self.driver, LoginLocator.error, self.log
            )
            self.compare_text(self.__error, text)
            self.allure.attach_image(self.driver, "The message is visible")
