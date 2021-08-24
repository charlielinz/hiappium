OPERATOR_IDS = {
    "+": "plus",
    "-": "minus",
    "*": "multiply",
    "/": "divide",
    "=": "equals",
}

# find element by id


class CalculatorApp:
    def __init__(self, manager):
        self.manager = manager

    def _find_num(self, num):
        app_package = self.manager.desired_cap['appPackage']
        id_ = app_package + ":id" + "/digit_" + str(num)
        num = self.manager.driver.find_element_by_id(id_)
        return num

    def _find_operator(self, operator):
        operator = self.manager.driver.find_element_by_accessibility_id(operator)
        return operator

    def click_num(self, num):
        num = self._find_num(num)
        num.click()

    def click_operator(self, operator):
        operator = self._find_operator(operator)
        operator.click()
