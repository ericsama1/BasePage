from time import sleep
from selenium.webdriver.common.by import By
from settings import evidence_path
from i18n import Message
from baseelement import BaseElement


class BasePage():
    """Base class to initialize a page"""
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

    def highlight(self, element):
        """Method to highlight, capture a screenshot and unhighligher an
        element

        Arguments:
            element {BaseElement} -- Element to highlight
        """
        element.highlight()
        self.capture_screenshot()
        element.remove_highlight()

    def capture_screenshot(self):
        """
        Method to save a screenshot in the evidence path
        """
        if evidence_path is None:
            self.log.error(Message.CAPTURE_IMAGE_ERROR)
        else:
            pass

    def compare_text(self, element, text):
        """ Method to comparte between the element's text and the spected text.
        If the texts doesn't same, then show a AssertionError

        Arguments:
            element {BaseElemenet} -- Element to get the text
            text {String} -- Expected text
        """
        elem_text = element.get_text()
        assert elem_text == text, (
            Message.COMPARE_TEXT_ERROR.format(text, elem_text)
        )

    def get_elements(self, driver, by, log):
        """ Method to obtain sub elements from an element. Search this element
        using xpath.

        Arguments:
            driver {WebDriver} -- WebDriver, to use
            by {(By, String)} -- Method to search the element
            log {Log} -- Driver's logger

        Returns:
            [BaseElement] -- A list with BaseElement from the searched element
        """
        elem = driver.find_elements(*by)
        xpath = '(%s)[{}]' % by[1]
        elements = [
            BaseElement(driver, (By.XPATH, xpath.format(x + 1)), log)
            for x in range(len(elem))
        ]
        return elements

    def sleep(self, seconds):
        """Method to pause the script for x seconds.

        Arguments:
            seconds {integer} -- Seconds to pause the script
        """
        self.log.info(Message.SLEEP_MESSAGE.format(seconds))
        sleep(seconds)
