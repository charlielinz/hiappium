from appium import webdriver

OPERATOR_IDS = {
    "+": "plus",
    "-": "minus",
    "*": "multiply",
    "/": "divide",
    "=": "equals",
}


class DriverManger:
    DESIRED_CAP = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.google.android.calculator",
        "appActivity": "com.android.calculator2.Calculator",
    }

    def __init__(self, desired_cap):
        self._remote()
        self.desired_cap = desired_cap

    def _remote(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.DESIRED_CAP)

    def _find_num(self, num):
        app_package = self.DESIRED_CAP['appPackage']
        id_ = app_package + ":id" + "/digit_" + str(num)
        num = self.driver.find_element_by_id(id_)
        return num

    def _find_operator(self, operator):
        operator = self.driver.find_element_by_accessibility_id(operator)
        return operator

    def click_num(self, num):
        num = self._find_num(num)
        num.click()

    def click_operator(self, operator):
        operator = self._find_operator(operator)
        operator.click()
