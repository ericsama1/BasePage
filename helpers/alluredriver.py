import allure


class Allure():
    def step(self, step_number, text):
        allure_step = allure.step('{}: {}'.format(step_number, text))
        return allure_step

    def simple_step(self, text):
        allure_step = allure.step(text)
        return allure_step

    def attach_image(self):
        pass
