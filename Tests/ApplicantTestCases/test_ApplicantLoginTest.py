import pytest

from Config.Config import TestData
from Pages.ApplicantPages.ApplicantLoginPage import LoginPage
from Tests.BaseTest import BaseTest


class TestApplicantLoginPage(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(TestData.ApplicantLoginPage_Title)
        assert title == TestData.ApplicantLoginPage_Title

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.User_Name, TestData.Password)
