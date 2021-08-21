import time
from managers import DriverManger, OPERATOR_IDS

manager = DriverManger(
    {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.google.android.calculator",
        "appActivity": "com.android.calculator2.Calculator",
    }
)
time.sleep(5)
manager.click_num(1)
manager.click_operator(OPERATOR_IDS["+"])
manager.click_num(2)
manager.click_operator(OPERATOR_IDS["="])
