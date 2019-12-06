from selenium.webdriver.common.by import By


class HomeLocator():
    """
    Home page's elements locator
    """
    logo = (By.CLASS_NAME, "app_logo")
    menu = (By.CLASS_NAME, "bm-burger-button")
    cart = (By.XPATH, "//*[@data-icon='shopping-cart']")
    product_sort = (By.CLASS_NAME, "product_sort_container")
    product_list = (By.XPATH, "//div[@class='inventory_item']")
    products_add_cart = (By.XPATH, "//*[@class='btn_primary btn_inventory']")

    # Menu options
    all_item = (By.ID, "inventory_sidebar_link")
    about = (By.ID, "about_sidebar_link")
    logout = (By.ID, "logout_sidebar_link")
    reset = (By.ID, "reset_sidebar_link")
    close_menu = (By.XPATH, "//button[text()='Close Menu']")
