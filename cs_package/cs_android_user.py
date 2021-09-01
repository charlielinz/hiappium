from cs_package.xpath import HOMEPAGE, ACCOUNTPAGE, FACEBOOK_SIGNIN, LINE_SIGNIN, SIGNUPPAGE, SIGNINPAGE
from time import sleep


class CSUser:
    def __init__(self, manager):
        self.manager = manager
        sleep(1)

    def _find_element(self, xpath):
        return self.manager.driver.find_element_by_xpath(xpath)

    def _find_element_and_click(self, xpath):
        self.manager.driver.find_element_by_xpath(xpath).click()
        sleep(1)

    def _find_element_and_send_keys(self, xpath, key):
        self.manager.driver.find_element_by_xpath(xpath).send_keys(key)

    def adventure_page(self):
        self._find_element_and_click(HOMEPAGE["adventure"])

    def search_page(self):
        self._find_element_and_click(HOMEPAGE["search"])

    def favorite_page(self):
        self._find_element_and_click(HOMEPAGE["favorite"])

    def account_page(self):
        self._find_element_and_click(HOMEPAGE["account"])

    def sign_up_page(self):
        self.account_page()
        self._find_element_and_click(ACCOUNTPAGE["sign_up_page"])

    def sign_in_page(self):
        self.account_page()
        self._find_element_and_click(ACCOUNTPAGE["sign_in_normal"])

    def sign_up(self, lastname, firstname, email, password, password_confirmed):
        self.sign_up_page()
        self._find_element_and_send_keys(SIGNUPPAGE["last_name"], lastname)
        self._find_element_and_send_keys(SIGNUPPAGE["first_name"], firstname)
        self._find_element_and_send_keys(SIGNUPPAGE["email"], email)
        self._find_element_and_send_keys(SIGNUPPAGE["password"], password)
        self._find_element_and_send_keys(SIGNUPPAGE["password_confirmed"], password_confirmed)
        self._find_element_and_click(SIGNUPPAGE["sign_up"])

    def sign_in(self, email, password):
        self.sign_in_page()
        self._find_element_and_send_keys(SIGNINPAGE["email"], email)
        self._find_element_and_send_keys(SIGNINPAGE["password"], password)
        self._find_element_and_click(SIGNINPAGE["sign_in"])

    def facebook_sign_in(self, accountname, password):
        self.account_page()
        self._find_element_and_click(ACCOUNTPAGE["sign_in_facebook"])
        sleep(2)
        try:
            element = self._find_element(FACEBOOK_SIGNIN["account_name"])
            if element.is_displayed():
                self._find_element_and_send_keys(FACEBOOK_SIGNIN["account_name"], accountname)
                self._find_element_and_send_keys(FACEBOOK_SIGNIN["password"], password)
                self._find_element_and_click(FACEBOOK_SIGNIN["enter"])
        except Exception:
            self._find_element_and_click(FACEBOOK_SIGNIN["continue"])
    
    def line_sign_in(self, email, password):
        self.account_page()
        self._find_element_and_click(ACCOUNTPAGE["sign_in_line"])
        self._find_element_and_send_keys(LINE_SIGNIN["email"], email)
        self._find_element_and_send_keys(LINE_SIGNIN["password"], password)
        self._find_element_and_click(LINE_SIGNIN["enter"])
        sleep(1)
        self._find_element_and_click(LINE_SIGNIN["allow_access"])
