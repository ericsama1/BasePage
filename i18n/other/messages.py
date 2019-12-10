from googletrans import Translator
from i18n.en.messages import (
    BaseBrowserConstants as BrowserEN,
    BaseElementConstants as ElementEN,
    BasePageConstants as PageEN,
    BaseRadioConstants as RadioEN,
    BaseSelectConstants as SelectEN
)
from settings import language

translator = Translator()
dest = language


class BaseBrowserConstants():
    BROWSERNOTEXIST = translator.translate(
        BrowserEN.BROWSERNOTEXIST, dest).text
    OPENBROWSER = translator.translate(BrowserEN.OPENBROWSER, dest).text
    SETURL = translator.translate(BrowserEN.SETURL, dest).text
    MAXIMIZE = translator.translate(BrowserEN.MAXIMIZE, dest).text
    NEWTAB = translator.translate(BrowserEN.NEWTAB, dest).text
    TAB_CHANGE_ERROR = translator.translate(
        BrowserEN.TAB_CHANGE_ERROR, dest).text
    TAB_CHANGE = translator.translate(BrowserEN.TAB_CHANGE, dest).text
    CLOSE_TAB = translator.translate(BrowserEN.CLOSE_TAB, dest).text
    CLOSE_BROWSER = translator.translate(BrowserEN.CLOSE_BROWSER, dest).text


class BaseElementConstants():
    ELEMENT_NOT_VISIBLE = translator.translate(
        ElementEN.ELEMENT_NOT_VISIBLE, dest
    ).text
    CLEAR_ELEMENT = translator.translate(ElementEN.CLEAR_ELEMENT, dest).text
    WRITE_ELEMENT = translator.translate(ElementEN.WRITE_ELEMENT, dest).text
    CLICK_ELEMENT = translator.translate(ElementEN.CLICK_ELEMENT, dest).text
    DOUBLE_CLICK_ELEMENT = translator.translate(
        ElementEN.DOUBLE_CLICK_ELEMENT, dest).text
    SCROLL_ELEMENT = translator.translate(
        ElementEN.SCROLL_ELEMENT, dest).text
    HIGHLIGHT_ELEMENT = translator.translate(
        ElementEN.HIGHLIGHT_ELEMENT, dest).text
    REMOVE_HIGHLIGHT_ELEMENT = translator.translate(
        ElementEN.REMOVE_HIGHLIGHT_ELEMENT, dest).text


class BasePageConstants():
    CAPTURE_IMAGE_ERROR = translator.translate(
        PageEN.CAPTURE_IMAGE_ERROR, dest).text
    COMPARE_TEXT_ERROR = translator.translate(
        PageEN.COMPARE_TEXT_ERROR, dest).text


class BaseRadioConstants():
    SELECT_OPTION = translator.translate(RadioEN.SELECT_OPTION, dest).text
    SELECT_OPTION_ERROR = translator.translate(
        RadioEN.SELECT_OPTION_ERROR, dest).text


class BaseSelectConstants():
    SELECT_BY_TEXT = translator.translate(SelectEN.SELECT_BY_TEXT, dest).text
    SELECT_BY_TEXT_ERROR = translator.translate(
        SelectEN.SELECT_BY_TEXT_ERROR, dest).text
    SELECT_BY_VALUE = translator.translate(SelectEN.SELECT_BY_VALUE, dest).text
    SELECT_BY_INDEX = translator.translate(SelectEN.SELECT_BY_INDEX, dest).text
    SELECT_BY_INDEX_ERROR = translator.translate(
        SelectEN.SELECT_BY_INDEX_ERROR, dest).text
