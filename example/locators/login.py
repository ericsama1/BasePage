from selenium.webdriver.common.by import By


class LoginLocator():
    user = (By.ID, "user-name")
    passw = (By.ID, "password")
    login = (By.XPATH, "//input[@type='submit']")
    error = (By.XPATH, "//h3[@data-test='error']")
