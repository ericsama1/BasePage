import allure
from allure import attachment_type


class Allure():
    def __init__(self):
        self.step_number = 0

    def step(self, text):
        allure_step = allure.step('Step {}: {}'.format(self.step_number, text))
        self.step_number += 1
        return allure_step

    def simple_step(self, text):
        allure_step = allure.step(text)
        return allure_step

    def attach_image(self, driver, description):
        allure.attach(
            driver.get_screenshot_as_png(),
            '{}'.format(description),
            attachment_type=attachment_type.PNG
        )
