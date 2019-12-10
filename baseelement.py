from pytest import fail
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_c
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from i18n import Message


class BaseElement():
    """ BaseElement of Webelement class """
    # JS scripts
    __SCROLL = "arguments[0].scrollIntoView({block:'center'});"
    __APPLY_STYLE = "arguments[0].setAttribute('style', arguments[1])"
    __HIGHTLIGHT = "border: 4px solid red"

    def __init__(self, driver, by, log, timeout=10):
        """ Method to inicialize the BaseElement

        Arguments:
            driver {webdriver} -- Webdriver to use
            by {(By, String)} -- Method to identify a element in the POM. Use
                                 By class from selenium.
                                 For example, (By.ID, 'id')
            log {Logging} -- Logger to write the log

        Keyword Arguments:
            timeout {int} -- Timeout to wait an element form POM
                             (default: {10})
        """
        wait = WebDriverWait(driver, timeout)
        self.log = log
        self.driver = driver
        self.by = by
        try:
            self.element = wait.until(exp_c.visibility_of_element_located(by))
        except TimeoutException:
            try:
                self.element = self.driver.find_element(*(by))
            except NoSuchElementException:
                msg = Message.ELEMENT_NOT_VISIBLE.format(by)
                self.log.error(msg)
                fail(msg)

    def wait(self, seconds=10):
        """Method to wait the element

        Keyword Arguments:
            seconds {int} -- Seconds to wait the elemento be visible
                             (default: {10})
        """
        wait = WebDriverWait(self.driver, seconds)
        wait.until(exp_c.visibility_of_element_located(self.by))

    # Write

    def clear(self):
        """
        Method to clear the content of the element
        """
        self.scroll_to()
        self.element.clear()
        self.log.info(Message.CLEAR_ELEMENT.format(self.by))

    def send_keys(self, text):
        """ Method to write a text in the element

        Arguments:
            text {String} -- Text to write in the element
        """
        self.scroll_to()
        self.clear()
        self.element.send_keys(text)
        self.log.info(Message.WRITE_ELEMENT.format(text, self.by))

    # Click

    def click(self):
        """
        Method to click in the element
        """
        self.scroll_to()
        self.element.click()
        self.log.info(Message.CLICK_ELEMENT.format(self.by))

    def double_click(self):
        """
        Method to do a double click in the element
        """
        self.scroll_to()
        actionchains = ActionChains(self.driver)
        actionchains.double_click(self.element).perform()
        self.log.info(Message.DOUBLE_CLICK_ELEMENT.format(self.by))

    # Scroll

    def scroll_to(self):
        """
        Method to scroll to the element
        """
        self.driver.execute_script(self.__SCROLL, self.element)
        self.log.info(Message.SCROLL_ELEMENT.format(self.by))

    # Highlight

    def highlight(self):
        """
        Method to highlight the element
        """
        # Get the original style of the element. This use to unhighlight the
        # element
        self.original_style = self.element.get_attribute('style')
        # Apply the style to highlight an element
        self.__apply_style(self.__HIGHTLIGHT)
        self.log.info(Message.HIGHLIGHT_ELEMENT.format(self.by))

    def remove_highlight(self):
        """
        Method to unhighlight the element
        """
        try:
            # Try to obtain the original style
            style = self.original_style
        except AttributeError:
            # If the element hasn't original style, the element didn't
            # highlight
            style = None
        self.__apply_style(style)
        self.log.info(Message.REMOVE_HIGHLIGHT_ELEMENT.format(self.by))

    def __apply_style(self, style):
        """ Method to apply the style to the element

        Arguments:
            style {String} -- Style to apply
        """
        self.driver.execute_script(self.__APPLY_STYLE, self.element, style)

    # Move

    def move_mouse_to(self):
        """
        Method to move the mouse over the element
        """
        actionchains = ActionChains(self.driver)
        actionchains.move_to_element(self.element).perform()

    # Gets

    def get_text(self):
        """ Method to get element's text

        Returns:
            String -- Element's text
        """
        return self.element.text

    def get_value(self):
        """ Method to get the element's value

        Returns:
            String -- Element's value
        """
        return self.get_attribute('value')

    def get_attribute(self, attribute):
        """ Method to obtain the attribute from the element

        Arguments:
            attribute {String} -- Name of the attribute to get

        Returns:
            String -- value of the attribute
        """
        return self.element.get_attribute(attribute)

    def get_location(self):
        """ Method to get the element's location

        Returns:
            integer -- x value
            integer -- y value
        """
        location = self.element.location
        return location.get('x'), location.get('y')

    def get_size(self):
        """ Method to get the element's size

        Returns:
            integer -- height value
            integer -- width value
        """
        size = self.element.size
        return size.get('height'), size.get('width')

    def get_element(self):
        """ Method to get the webelement

        Returns:
            WebElement -- WebElement
        """
        return self.element
