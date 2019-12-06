from settings import evidence_path
from i18n import Message


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
