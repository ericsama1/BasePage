from selenium.webdriver.common.by import By


class HomeLocator():
    """
    Home page's elements locator
    """
    product_sort = (By.CLASS_NAME, "product_sort_container")
    product_list = (By.XPATH, "//div[@class='inventory_item']")
    products_add_cart = (By.XPATH, "//*[@class='btn_primary btn_inventory']")
