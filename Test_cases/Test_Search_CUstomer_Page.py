import pytest
import time
from selenium import webdriver

from Base_pages.Search_Customer_Page import search_customer_page
from Base_pages.Login_Admin_Page import Login_Admin_Page
from Base_pages.Add_Customer_Page import Add_Customer_Page
from Utilities.read_properties import read_config
from Utilities.custom_logger import Log_maker



class Test_004_search_customer_By_Email:
    BaseUrl = read_config.get_url()
    username = read_config.get_username()
    password = read_config.get_password()
    logger = Log_maker.log_gen()

    @pytest.fixture
    def setup_driver(self):
        driver = webdriver.Chrome()  # or any other WebDriver
        yield driver
        driver.quit()

    def test_search_by_email(self,setup_driver):
        self.logger.info("***************Test search customer by email started**************")
        self.driver = setup_driver
        self.driver.get(self.BaseUrl)
        self.driver.maximize_window()
        #login
        self.lp = Login_Admin_Page(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_btn()
        self.logger.info("*******************Login Successful**************")

        self.logger.info("*******************starting search customer by email ")
        self.addcustomer = Add_Customer_Page(self.driver)
        self.addcustomer.click_customers()
        self.addcustomer.click_customers_options()
        self.logger.info("*******************search customer by email id ***************")

        self.searchcust = search_customer_page(self.driver)
        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchcust.setSearch()
        time.sleep(5)
        status = self.searchcust.search_customer_by_email("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("***************search customer by email id finished **************")





