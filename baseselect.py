from selenium.webdriver.support.ui import Select
from random import choice
from baseelement import BaseElement
from i18n import Message


class BaseSelect(BaseElement):
    """ Base class to manipulate the select element

    Arguments:
        BaseElement {BaseElement} -- Inherit BaseElement method
    """

    def __init__(self, driver, by, log, timeout=10):
        """Inicialize the BaseSelect element

        Arguments:
            driver {Webdriver} -- Webdriver to use
            by {(By, String)} -- Method to identify a element in the POM. Use
                                 By class from selenium.
                                 For example, (By.ID, 'id')
            log {logging} -- Logger to write the log

        Keyword Arguments:
            timeout {int} -- Timeout to wait an element form POM
                             (default: {10})
        """
        super().__init__(driver, by, log, timeout)
        self.element = Select(self.element)

    def select_by_text(self, text):
        """ Method to select an option in the select by text. The text need to
        by same of option's text

        Arguments:
            text {String} -- Option's text to select
        """
        self.element.select_by_visible_text(text)
        self.log.info(Message.SELECT_BY_TEXT.format(text, self.by))

    def select_by_index(self, index):
        """ Method to select an option in the select by index

        Arguments:
            index {int} -- Position of the option to select
        """
        try:
            self.element.select_by_index(index)
            self.log.info(Message.SELECT_BY_INDEX.format(index, self.by))
        except IndexError:
            self.log.error(
                Message.SELECT_BY_INDEX_ERROR.format(index, self.by)
            )

    def select_by_value(self, value):
        """ Method to select an option in the select by value

        Arguments:
            value {String} -- Value of the option to select
        """
        self.element.select_by_value(value)
        self.log.info(Message.SELECT_BY_VALUE.format(value, self.by))

    def select_by_partial_text(self, text):
        """ Method to select an option in the select by partial text

        Arguments:
            text {String} -- Partial text of the option to select
        """
        options = self.__get_options()  # Get the options
        # Filter the text from the options
        options = [option.text for option in options]
        option_text = None
        for option in options:
            # If the partial text in the option, then select and end the
            # iteration
            if text in option:
                option_text = option
                self.element.select_by_visible_text(option_text)
                break
        # If the option_text is None, then show an error
        if option_text is None:
            self.log.error(Message.SELECT_BY_TEXT_ERROR.format(
                                                        option_text, self.by))
        else:
            self.log.info(Message.SELECT_BY_TEXT.format(option_text, self.by))

    def random_select(self):
        """
        Method to select randomly a option in the select
        """
        options = self.__get_options()  # Get the options
        option = choice(options)  # Select an option randomly
        self.element.select_by_visible_text(option.text)  # Select the option
        self.log.info(Message.SELECT_BY_TEXT.format(option.text, self.by))

    def __get_options(self):
        """Method to get the options from the select

        Returns:
            Webelement -- Webelement with option tag from the element
        """
        return self.element.options
