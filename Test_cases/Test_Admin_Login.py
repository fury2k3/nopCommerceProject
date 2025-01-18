from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from Base_pages.Login_Admin_Page import Login_Admin_Page
from Utilities.read_properties import read_config
from Utilities.custom_logger import Log_maker


class Test_Admin_Login:
    login_url= read_config.get_url()
    username=read_config.get_username()
    password=read_config.get_password()
    invalid_username=read_config.invalid_username()
    Logger =Log_maker.log_gen()


    @pytest.mark.regression
    def test_title_verification(self,setup_driver):
        self.Logger.info("*********test_Admin_Login*******")
        self.Logger.info("*********test_title_verification*******")
        self.driver = setup_driver
        self.driver.get(self.login_url)
        actual_title = self.driver.title
        expected_title = "Your store. Login"
        if expected_title == actual_title:
            assert True
            self.driver.close()
            self.Logger.info("*********test_title_Match*******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_title_verification.png")
            self.driver.close()
            self.Logger.info("*********test_title_Not_Match*******")
            assert False


    @pytest.mark.sanity
    def test_login_validation(self,setup_driver):
        self.Logger.info("*********test_login_validation*******")
        self.driver = setup_driver
        self.driver.get(self.login_url)
        self.admin_login_page = Login_Admin_Page(self.driver)
        self.admin_login_page.enter_username(self.username)
        self.admin_login_page.enter_password(self.password)
        self.admin_login_page.click_btn()
        Actual_dashboard_name = self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if Actual_dashboard_name == "Dashboard":
            self.Logger.info("*********dashboard_Match*******")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login_validation.png")
            self.driver.close()
            assert False


    @pytest.mark.sanity #because its a main test lezmna naatouh sanity wel be9i regression
    @pytest.mark.regression
    def test_login_failed_validation(self,setup_driver):
        self.Logger.info("*********test_login_failed_validation*******")
        self.driver=setup_driver
        self.driver.get(self.login_url)
        self.admin_login_page = Login_Admin_Page(self.driver)
        self.admin_login_page.enter_username(self.invalid_username)
        self.admin_login_page.enter_password(self.password)
        self.admin_login_page.click_btn()
        error_message = self.driver.find_element(By.XPATH,"//li[normalize-space()='No customer account found']").text
        if error_message == "No customer account found":
            self.Logger.info("*********test_error_matching*******")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login_failed_validation.png")
            self.driver.close()
            assert False
