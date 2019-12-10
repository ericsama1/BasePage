from selenium.webdriver.common.by import By


class HeaderLocator():
    logo = (By.CLASS_NAME, "app_logo")
    menu = (By.CLASS_NAME, "bm-burger-button")
    cart = (By.XPATH, "//*[@data-icon='shopping-cart']")

    # Menu options
    all_item = (By.ID, "inventory_sidebar_link")
    about = (By.ID, "about_sidebar_link")
    logout = (By.ID, "logout_sidebar_link")
    reset = (By.ID, "reset_sidebar_link")
    close_menu = (By.XPATH, "//button[text()='Close Menu']")
