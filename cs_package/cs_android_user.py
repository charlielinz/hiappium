from xpath import HOMEPAGE_XPATH, ACCOUNTPAGE_XPATH, SIGNUPPAGE_XPATH, SIGNINPAGE_XPATH
from time import sleep


class CSUser:
    def __init__(self, manager):
        self.manager = manager
        sleep(1)

    def _find_element(self, xpath):
        self.manager.driver.find_element_by_xpath(xpath)

    def _find_element_and_click(self, xpath):
        self.manager.driver.find_element_by_xpath(xpath).click()
        sleep(1)

    def _find_element_and_send_keys(self, xpath, key):
        self.manager.driver.find_element_by_xpath(xpath).send_keys(key)

    def adventure_page(self):
        self._find_element_and_click(HOMEPAGE_XPATH["adventure"])

    def search_page(self):
        self._find_element_and_click(HOMEPAGE_XPATH["search"])

    def favorite_page(self):
        self._find_element_and_click(HOMEPAGE_XPATH["favorite"])

    def account_page(self):
        self._find_element_and_click(HOMEPAGE_XPATH["account"])

    def sign_up_page(self):
        self.account_page()
        self._find_element_and_click(ACCOUNTPAGE_XPATH["sign_up_page"])

    def sign_in_page(self):
        self.account_page()
        self._find_element_and_click(ACCOUNTPAGE_XPATH["sign_in_normal"])

    def sign_up(self, lastname, firstname, email, password, password_confirmed):
        self.account_page()
        self._find_element_and_click(ACCOUNTPAGE_XPATH["sign_up_page"])
        self._find_element_and_send_keys(SIGNUPPAGE_XPATH["last_name"], lastname)
        self._find_element_and_send_keys(SIGNUPPAGE_XPATH["first_name"], firstname)
        self._find_element_and_send_keys(SIGNUPPAGE_XPATH["email"], email)
        self._find_element_and_send_keys(SIGNUPPAGE_XPATH["password"], password)
        self._find_element_and_send_keys(SIGNUPPAGE_XPATH["password_confirmed"], password_confirmed)
        self._find_element_and_click(SIGNUPPAGE_XPATH["sign_up"])

    def sign_in(self, email, password):
        self.account_page()
        self._find_element_and_click(ACCOUNTPAGE_XPATH["sign_in_normal"])
        self._find_element_and_send_keys(SIGNINPAGE_XPATH["email"], email)
        self._find_element_and_send_keys(SIGNINPAGE_XPATH["password"], password)
        self._find_element_and_click(SIGNINPAGE_XPATH["sign_in"])
