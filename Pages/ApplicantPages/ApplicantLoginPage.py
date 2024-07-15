from selenium.webdriver.common.by import By

from Config.Config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """By Locators"""
    Email = (By.NAME, 'email')
    Password = (By.NAME, 'password')
    Login_Button = (By.XPATH, '//button[contains(text(),"Log")]')
    Signup_Link = (By.LINK_TEXT, 'Sign Up')

    """Constructor of the class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_URL)

    """Page Actions"""

    """This is used to get the page title"""

    def get_login_page_title(self, title):
        return self.get_title(title)

    """This is used to check the signup link"""

    def is_signup_link_exist(self):
        return self.is_visible(self.Signup_Link)

    """This is used to do login"""

    def do_login(self, username, password):
        self.do_send_keys(self.Email, username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.Login_Button)
