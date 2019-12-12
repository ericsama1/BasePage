from pytest import fail
from settings import browser
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from i18n import CHROME, FIREFOX, IE, OPERA, EDGE, Message


class BaseBrowser():
    """ Method to open a browser to use"""
    __NEW_WINDOW = "window.open('{}')"

    def __init__(self, url, log=None):
        """ Method to inicialize the browser

        Arguments:
            url {String} -- URL to automatize
        """
        self.log = log
        self.driver = self.open_browser()
        self.set_url(url)
        self.maximize_windows()

    def open_browser(self):
        """ Method to open a browser. Get the browser name from settings and
        open the browser

        Returns:
            Webdriver -- webdriver element. Depends of browser name in the
                         settings
        """
        # Dict with the diferent browser to use
        open_driver = {
            CHROME: self.__open_chrome,
            FIREFOX: self.__open_firefox,
            IE: self.__open_ie,
            OPERA: self.__open_opera,
            EDGE: self.__open_edge
        }
        try:
            # Try to open the browser
            driver = open_driver.get(browser.lower())()
        except TypeError:
            # If the browser's name don't match with any name in the dict
            fail(Message.BROWSERNOTEXIST)
        self.log.info(Message.OPENBROWSER.format(browser))
        return driver

    def __open_chrome(self):
        """ Method to open a Chrome browser.
        chromedriver need to by in the PATH os enviroment variables

        Returns:
            Webdriver -- Chrome webdriver
        """
        driver = webdriver.Chrome()
        return driver

    def __open_firefox(self):
        """ Method to open a Firefox browser
        geckodriver need to by in the PATH os enviroment variables

        Returns:
            Webdriver -- Firefox webdriver
        """
        driver = webdriver.Firefox()
        return driver

    def __open_ie(self):
        """ Method to open a Internet Explorer browser

        Returns:
            Webdriver -- Internet Explorer browser
        """
        driver = webdriver.Ie()
        return driver

    def __open_opera(self):
        """ Method to open a Opera browser

        Returns:
            Webdriver -- Opera Webdriver
        """
        options = OperaOptions()
        # Set the opera binary location to execute the browser
        options.binary_location = (
            "Path of the opera.exe"
        )
        # Set the path of opera driver
        opera_driver = "Path of the opera driver"
        driver = webdriver.Opera(executable_path=opera_driver, options=options)
        return driver

    def __open_edge(self):
        """ Method to open a Edge browser

        Returns:
        Webdriver -- Edge browser
        """
        driver = webdriver.Edge()
        return driver

    def set_url(self, url):
        """ Method to set the url in the browser

        Arguments:
            url {String} -- URL to enter in the browser
        """
        self.driver.get(url)
        self.log.info(Message.SETURL.format(url))

    def maximize_windows(self):
        """
        Method to maximize the windows size of the browser
        """
        self.driver.maximize_window()
        self.log.info(Message.MAXIMIZE)

    # Tabs

    def new_tab(self, url):
        """ Method to create a new tab in the browser, using javascript

        Arguments:
            url {String} -- URL to open in the new tab
        """
        self.driver.execute_script(self.__NEW_WINDOW.format(url))
        self.change_tab(len(self.get_tabs())-1)
        self.log.info(Message.NEWTAB.format(url))

    def change_tab(self, position):
        """ Method to change the active tab in the browser

        Arguments:
            position {integer} -- Position of the tab to set active tab
        """
        tabs = self.get_tabs()
        try:
            # Try change the active tab
            tab = tabs[position]
        except IndexError:
            # If the position doesn't exist
            fail(Message.TAB_CHANGE_ERROR.format(position))
        finally:
            self.driver.switch_to.window(tab)
            self.log.info(Message.TAB_CHANGE.format(position))

    def close_tab(self):
        """
        Method to close a tab. If the closed tab is the only tab, close the
        browser. If isn't the only tab, after close the tab, set the first
        tab as active tab
        """
        tabs = self.get_tabs()
        self.driver.close()
        if len(tabs) > 1:
            # When close a tab, set the first tab as active tab
            self.change_tab(0)
            self.log.info(Message.CLOSE_TAB)
        else:
            self.log.info(Message.CLOSE_BROWSER)

    # Gets

    def get_tabs(self):
        """ Method to get the tabs of the browser

        Returns:
            browser's handles
        """
        return self.driver.window_handles

    def get_driver(self):
        """ Method to get the driver and log

        Returns:
            Webdriver -- Webdriver to use
            Logging -- logger to write the log
        """
        return self.driver, self.log

    def get_current_url(self):
        """ Method to get the current URL from the active tab

        Returns:
            String -- current URL of the active tab
        """
        return self.driver.current_url
