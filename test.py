import unittest
import HtmlTestRunner
from cs_app import CSApp
from time import sleep
from cs_package.xpath import HOMEPAGE, ACCOUNTPAGE, SIGNUPPAGE


class Test(CSApp):
    def test_facebook_sign_in(self):
        self.cs_user.facebook_sign_in(
            accountname="windylin31@yahoo.com.tw", password="1o42l4d03bp6"
        )
        sleep(3)
        account_page = self.manager.driver.find_element_by_xpath(HOMEPAGE["account"])
        self.assertEqual(account_page.get_attribute("clickable"), "true")

    def test_line_sign_in(self):
        self.cs_user.line_sign_in(
            email="windylin31@yahoo.com.tw", password="1o42l4g8bp6"
        )
        sleep(3)
        account_page = self.manager.driver.find_element_by_xpath(HOMEPAGE["account"])
        self.assertEqual(account_page.get_attribute("clickable"), "true")

    def test_sign_up_page(self):
        self.cs_user.sign_up_page()
        sleep(2)
        sign_up_button = self.cs_user._find_element(SIGNUPPAGE["sign_up"])
        self.assertEqual(sign_up_button.get_attribute("clickable"), "true")

    def test_sign_up(self):
        self.cs_user.sign_up(
            lastname="test10",
            firstname="test",
            email="test10@test.com",
            password="00000000",
            password_confirmed="00000000",
        )
        sleep(10)
        sign_up_finish = self.manager.driver.find_element_by_xpath(
            SIGNUPPAGE["interested_theme_finish"]
        )
        self.assertEqual(sign_up_finish.get_attribute("clickable"), "true")

    def test_sign_in(self):
        self.cs_user.sign_in("test2@test.com", "00000000")
        sleep(2)
        account_page = self.manager.driver.find_element_by_xpath(HOMEPAGE["account"])
        self.assertEqual(account_page.get_attribute("clickable"), "true")


if __name__ == "__main__":
    test_runner = HtmlTestRunner.HTMLTestRunner(
        output="./report",
        open_in_browser=False,
        report_title="CSApp functonal test report",
    )
    unittest.main(testRunner=test_runner)
