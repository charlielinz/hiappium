from driver_manager import DriverManager
from cs_android_apps import CSApp

manager = DriverManager(
    {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.csapp3",
        "appActivity": "com.csapp3.MainActivity",
    }
)

csapp = CSApp(manager)
csapp.register(
    lastname="test3",
    firstname="test",
    email="test3 @ test.com",
    password="00000000",
    password_confirmed="00000000",
)
