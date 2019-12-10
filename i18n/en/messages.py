""" This file contains the main menssage to write in the log.
For the other languages, translate the message from this file using google
translate libary
"""


class BaseBrowserConstants():
    BROWSERNOTEXIST = "Please, enter a browser in the settings file."
    OPENBROWSER = "Has opened a {} browser."
    SETURL = "Has opened the url: {}"
    MAXIMIZE = "Has maximized the window."
    NEWTAB = "Has opened a new tab with url: {}"
    TAB_CHANGE_ERROR = "The tab in the position {}, doesn't exist."
    TAB_CHANGE = "Has changed the active tab for the tab in the position {}."
    CLOSE_TAB = "Has closed the active tab."
    CLOSE_BROWSER = "Has closed the browser."


class BaseElementConstants():
    ELEMENT_NOT_VISIBLE = "The element {} isn't visible."
    CLEAR_ELEMENT = "Has cleared the contents of the element {}."
    WRITE_ELEMENT = "Has written the text '{0}' in the element {1}."
    CLICK_ELEMENT = "Has done a click on the element {}."
    DOUBLE_CLICK_ELEMENT = "Has done a double clicks on the element {}."
    SCROLL_ELEMENT = "Has scrolled to the element {}."
    HIGHLIGHT_ELEMENT = "Has highlighted the element {}."
    REMOVE_HIGHLIGHT_ELEMENT = "Has removed the highlight the element {}."


class BasePageConstants():
    CAPTURE_IMAGE_ERROR = "The evidence path isn't defined."
    COMPARE_TEXT_ERROR = (
        "The expected text '{0}', and the element's text '{1}' are different."
    )
    SLEEP_MESSAGE = "Sleep for {} sencods"


class BaseRadioConstants():
    SELECT_OPTION = (
        "Has selected the option with value '{0}' from the radiobutton set "
        "element {1}."
    )
    SELECT_OPTION_ERROR = "The value '{}' isn't in the options."


class BaseSelectConstants():
    SELECT_BY_TEXT = (
        "Has selected the option with the text '{0}' "
        "from the select element {1}."
    )
    SELECT_BY_TEXT_ERROR = (
        "Any option has the text '{0}' in the select element {1}."
    )
    SELECT_BY_VALUE = (
        "Has selected the option with value '{0}' from the select element {1}."
    )
    SELECT_BY_INDEX = (
        "Has selected the option in the position {0} "
        "from the select element {1}."
    )
    SELECT_BY_INDEX_ERROR = (
        "The select element {1}, hasn't got option in the position {0}."
    )
