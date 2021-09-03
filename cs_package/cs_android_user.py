from cs_package.xpath import (
    HOMEPAGE,
    ACCOUNTPAGE,
    FACEBOOK_SIGNIN,
    LINE_SIGNIN,
    SIGNUPPAGE,
    SIGNINPAGE,
    ANDROID_SETTING,
)
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class CSUser:
    def __init__(self, manager):
        self.manager = manager
        sleep(1)

    def _find_element_by_xpath(self, xpath):
        return self.manager.driver.find_element_by_xpath(xpath)

    def _find_element_by_id(self, id_):
        return self.manager.driver.find_element_by_id(id_)

    def _find_element_by_id_and_click(self, id_):
        self.manager.driver.find_element_by_id(id_).click()
        sleep(1)

    def _find_element_by_xpath_and_click(self, xpath):
        self.manager.driver.find_element_by_xpath(xpath).click()
        sleep(1)

    def _find_element_by_xpath_and_send_keys(self, xpath, key):
        self.manager.driver.find_element_by_xpath(xpath).send_keys(key)

    def _clear_storage_step(self, app_id):
        self._find_element_by_id_and_click(app_id)
        self._find_element_by_xpath_and_click(ANDROID_SETTING["Storage & Cache"])
        self._find_element_by_xpath_and_click(ANDROID_SETTING["Clear Storage"])
        try:
            self._find_element_by_xpath_and_click(ANDROID_SETTING["cs app OK"])
            self._find_element_by_xpath_and_click(ANDROID_SETTING["back"])
            self._find_element_by_xpath_and_click(ANDROID_SETTING["back"])
            return
        except NoSuchElementException:
            pass
        try:  
            self._find_element_by_xpath_and_click(ANDROID_SETTING["Google Chrome Clear All Data"])
            self._find_element_by_xpath_and_click(ANDROID_SETTING["Google Chrome OK"])
            self._find_element_by_xpath_and_click(ANDROID_SETTING["back"])
            self._find_element_by_xpath_and_click(ANDROID_SETTING["back"])
            return
        except NoSuchElementException:
            pass
        try:
            self._find_element_by_xpath_and_click(ANDROID_SETTING["Google Search Clear All Data"])
            self._find_element_by_xpath_and_click(ANDROID_SETTING["Google Search OK"])
            self._find_element_by_xpath_and_click(ANDROID_SETTING["back"])
            self._find_element_by_xpath_and_click(ANDROID_SETTING["back"])
        except NoSuchElementException:
            pass

    def adventure_page(self):
        self._find_element_by_xpath_and_click(HOMEPAGE["adventure"])

    def search_page(self):
        self._find_element_by_xpath_and_click(HOMEPAGE["search"])

    def favorite_page(self):
        self._find_element_by_xpath_and_click(HOMEPAGE["favorite"])

    def account_page(self):
        self._find_element_by_xpath_and_click(HOMEPAGE["account"])

    def sign_up_page(self):
        self.account_page()
        self._find_element_by_xpath_and_click(ACCOUNTPAGE["sign_up_page"])

    def sign_in_page(self):
        self.account_page()
        self._find_element_by_xpath_and_click(ACCOUNTPAGE["sign_in_normal"])

    def sign_up(self, lastname, firstname, email, password, password_confirmed):
        self.sign_up_page()
        self._find_element_by_xpath_and_send_keys(SIGNUPPAGE["last_name"], lastname)
        self._find_element_by_xpath_and_send_keys(SIGNUPPAGE["first_name"], firstname)
        self._find_element_by_xpath_and_send_keys(SIGNUPPAGE["email"], email)
        self._find_element_by_xpath_and_send_keys(SIGNUPPAGE["password"], password)
        self._find_element_by_xpath_and_send_keys(
            SIGNUPPAGE["password_confirmed"], password_confirmed
        )
        self._find_element_by_xpath_and_click(SIGNUPPAGE["sign_up"])

    def sign_in(self, email, password):
        self.sign_in_page()
        self._find_element_by_xpath_and_send_keys(SIGNINPAGE["email"], email)
        self._find_element_by_xpath_and_send_keys(SIGNINPAGE["password"], password)
        self._find_element_by_xpath_and_click(SIGNINPAGE["sign_in"])

    def clear_storage(self):
        self._find_element_by_xpath_and_click(ANDROID_SETTING["app & notifications"])
        num = ("1", "2", "3")
        for nums in num:
            app_id = "com.android.settings:id/app" + nums + "_view"
            self._clear_storage_step(app_id)

    def facebook_sign_in(self, accountname, password):
        self.account_page()
        self._find_element_by_xpath_and_click(ACCOUNTPAGE["sign_in_facebook"])
        sleep(2)
        try:
            self._find_element_by_id_and_click("com.android.chrome:id/terms_accept")
            self._find_element_by_id_and_click("com.android.chrome:id/negative_button")
        except NoSuchElementException:
            pass
        try:
            self._find_element_by_xpath_and_send_keys(
                FACEBOOK_SIGNIN["account_name"], accountname
            )
        except NoSuchElementException:
            self._find_element_by_xpath_and_click(FACEBOOK_SIGNIN["continue"])
            return
        self._find_element_by_xpath_and_send_keys(FACEBOOK_SIGNIN["password"], password)
        self._find_element_by_xpath_and_click(FACEBOOK_SIGNIN["enter"])
        sleep(2)
        try:
            self._find_element_by_xpath(HOMEPAGE["account"])
        except NoSuchElementException:
            self._find_element_by_xpath_and_click(FACEBOOK_SIGNIN["continue"])

    def line_sign_in(self, email, password):
        self.account_page()
        self._find_element_by_xpath_and_click(ACCOUNTPAGE["sign_in_line"])
        self._find_element_by_xpath_and_send_keys(LINE_SIGNIN["email"], email)
        self._find_element_by_xpath_and_send_keys(LINE_SIGNIN["password"], password)
        self._find_element_by_xpath_and_click(LINE_SIGNIN["enter"])
        sleep(1)
        self._find_element_by_xpath_and_click(LINE_SIGNIN["allow_access"])
