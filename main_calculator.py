import time
from driver_manager import DriverManager
from calculator_apps import OPERATOR_IDS, CalculatorApp

manager = DriverManager(
    {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.google.android.calculator",
        "appActivity": "com.android.calculator2.Calculator",
    }
)
calculator = CalculatorApp(manager)
time.sleep(3)
calculator.click_num(1)
calculator.click_operator(OPERATOR_IDS["+"])
calculator.click_num(2)
calculator.click_operator(OPERATOR_IDS["="])
