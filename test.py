from cs_package.driver_manager import DriverManager
from cs_package.cs_android_user import CSUser
import unittest
from time import sleep
from xpath import HOMEPAGE_XPATH, ACCOUNTPAGE_XPATH, SIGNUPPAGE_XPATH


class CSAppTest(unittest.TestCase):
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

    def test_sign_up_page(self):
        self.cs_user.sign_up_page()
        sleep(2)
        sign_up_button = self.cs_user._find_element(SIGNUPPAGE_XPATH["sign_up"])
        self.assertEqual(sign_up_button.get_attribute("clickable"), "true")

    def test_sign_up(self):
        self.cs_user.sign_up(
            lastname="test3",
            firstname="test",
            email="test3 @ test.com",
            password="00000000",
            password_confirmed="00000000",
        )
        sleep(2)
        account_page = self.manager.driver.find_element_by_xpath(HOMEPAGE_XPATH["account"])
        self.assertEqual(account_page.get_attribute("clickable"), "true")

    def test_sign_in(self):
        self.cs_user.sign_in("test2@test.com", "00000000")
        sleep(3)
        account_page = self.manager.driver.find_element_by_xpath(HOMEPAGE_XPATH["account"])
        self.assertEqual(account_page.get_attribute("clickable"), "true")


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(CSAppTest)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    print("All case numbers", test_result.testsRun)
    print("Failed case numbers", len(test_result.failures))
    print("Failed case and reason")
    print(test_result.failures)
    for case, reason in test_result.failures:
        print(case.id())
        print(reason)
    print("Errored case numbers", len(test_result.errors))
    print("Errored case and reason")
    print(test_result.errors)
    for case, reason in test_result.errors:
        print(case.id())
        print(reason)


if __name__ == '__main__':
    main()
