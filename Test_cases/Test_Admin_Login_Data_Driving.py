import time

import pytest

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest
from Base_pages.Login_Admin_Page import Login_Admin_Page
from Utilities.read_properties import read_config
from Utilities.custom_logger import Log_maker
from Utilities import excel_utils


class Test02_Admin_Login_Data_Driving:
    login_url = read_config.get_url()
    file = ".//Test_Data//admin_login_data.xlsx"
    status_List = []
    Logger = Log_maker.log_gen()



    # @pytest.mark.regression
    def test_03_data_driving_AdminLogin(self, setup_driver):
        self.Logger.info("*********test_login_validation*******")
        self.driver = setup_driver
        self.driver.implicitly_wait(10)
        self.driver.get(self.login_url)
        self.admin_login_page = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.file, "Admin")
        print("number of rows", self.rows)

        for r in range(2, self.rows + 1):
            self.username = excel_utils.read_data(self.file, "Admin", r, 1)
            self.password = excel_utils.read_data(self.file, "Admin", r, 2)
            self.expected_login = excel_utils.read_data(self.file, "Admin", r, 3)
            self.admin_login_page.enter_username(self.username)
            self.admin_login_page.enter_password(self.password)
            self.admin_login_page.click_btn()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected_login == "Yes":
                    self.Logger.info("test data is passed")
                    self.admin_login_page.click_logout()
                    self.status_List.append("Pass")

                elif self.expected_login == "No":
                    self.Logger.info("test data is NOT passed")
                    self.admin_login_page.click_logout()
                    self.status_List.append("Fail")

            elif act_title != exp_title:
                if self.expected_login == "Yes":
                    self.Logger.info("test data is NOT passed")
                    self.status_List.append("Fail")
                elif self.expected_login == "No":
                    self.Logger.info("test is passed")
                    self.status_List.append("Pass")

        print("status list is :", self.status_List)
        if "fail" in self.status_List:
            self.Logger.info("Test Data Driving Is Not Passed")
            assert False
        else:
            self.Logger.info("Test Data Driving Is Passed")
            assert True
