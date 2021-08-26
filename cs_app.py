import unittest
from cs_package.driver_manager import DriverManager
from cs_package.cs_android_user import CSUser


class CSApp(unittest.TestCase):
    def setUp(self):
        self.manager = DriverManager(
            {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "appPackage": "com.csapp3",
                "appActivity": "com.csapp3.MainActivity",
            }
        )
        self.cs_user = CSUser(self.manager)

    def tearDown(self):
        self.manager.driver.quit()
