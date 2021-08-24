from urls import HOMEPAGE_URLS, ACCOUNTPAGE_URLS, REGISTER_URLS
import time


class CSApp:
    def __init__(self, manager):
        self.manager = manager
        time.sleep(3)

    def adventure_page(self):
        account_button = self.manager.driver.find_element_by_xpath(
            HOMEPAGE_URLS["adventure"]
        )
        account_button.click()

    def search_page(self):
        account_button = self.manager.driver.find_element_by_xpath(
            HOMEPAGE_URLS["search"]
        )
        account_button.click()

    def favorite_page(self):
        account_button = self.manager.driver.find_element_by_xpath(
            HOMEPAGE_URLS["favorite"]
        )
        account_button.click()

    def account_page(self):
        account_button = self.manager.driver.find_element_by_xpath(
            HOMEPAGE_URLS["account"]
        )
        account_button.click()

    def register(self, lastname, firstname, email, password, password_confirmed):
        self.account_page()
        time.sleep(1)
        register_button = self.manager.driver.find_element_by_xpath(
            ACCOUNTPAGE_URLS["register_page"]
        )
        register_button.click()
        time.sleep(1)
        lastname = self.manager.driver.find_element_by_xpath(
            REGISTER_URLS["last_name"]
        ).send_keys(lastname)
        time.sleep(1)
        firstname = self.manager.driver.find_element_by_xpath(
            REGISTER_URLS["first_name"]
        ).send_keys(firstname)
        time.sleep(1)
        email = self.manager.driver.find_element_by_xpath(
            REGISTER_URLS["email"]
        ).send_keys(email)
        time.sleep(1)
        password = self.manager.driver.find_element_by_xpath(
            REGISTER_URLS["password"]
        ).send_keys(password)
        time.sleep(1)
        password_confirmed = self.manager.driver.find_element_by_xpath(
            REGISTER_URLS["password_confirmed"]
        ).send_keys(password_confirmed)
        time.sleep(1)
        self.manager.driver.find_element_by_xpath(REGISTER_URLS["resigter"]).click()
