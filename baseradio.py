from baseelement import BaseElement
from i18n import Message, VALUE


class BaseRadio(BaseElement):
    """Base class to use for the radiobuttons element

    Arguments:
        BaseElement {BaseElement} -- Inherit BaseElement method
    """
    # Constant to identify radiobutton from the element
    __RADIO_FORMAT = "//input[@type='radio']"
    __RADIO_VALUE = "//input[@type='radio' and @value='{}']"

    def select_option(self, option):
        """ Method to select an option

        Arguments:
            option {[type]} -- [description]
        """
        options = self.__get_options()
        # If the option is in the list
        if option in options:
            self.scroll_to()
            # Click on option
            self.element.find_element_by_xpath(
                self.__RADIO_VALUE.format(option)).click()
            self.log.info(Message.SELECT_OPTION.format(option, self.by))
        else:
            self.log.error(Message.SELECT_OPTION_ERROR.format(option))

    def __get_options(self):
        """ Method to get the options from the element

        Returns:
            [Strings] -- List of value of the options
        """
        options = self.element.find_elements_by_xpath(self.__RADIO_FORMAT)
        values = [value.get_attribute(VALUE) for value in options]
        return values
