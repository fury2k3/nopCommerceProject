from traceback import print_tb

import pytest
from selenium.webdriver.common.bidi.cdp import logger
import random
import string

from selenium.webdriver.common.by import By

from Utilities.read_properties import read_config
from Base_pages.Login_Admin_Page import Login_Admin_Page
from Utilities.custom_logger import Log_maker
from Base_pages.Add_Customer_Page import Add_Customer_Page


class Test_003_AddCustomer:
    login_url = read_config.get_url()
    username = read_config.get_username()
    password = read_config.get_password()
    logger = Log_maker.log_gen()



    @pytest.mark.sanity
    def test_Add_customer(self,setup_driver):
        self.logger.info("***************Test_003_AddCustomer************") #dima nekhdhou esm lcclass
        self.driver = setup_driver # nibou el setup mte3na
        self.driver.get(self.login_url) # njibou URL kilada
        self.driver.maximize_window()
        self.lp = Login_Admin_Page(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_btn()
        self.logger.info("***************Login_successfully***************")
        self.logger.info("***************Starting add customer Test************")
        self.add_cust = Add_Customer_Page(self.driver)
        # self.add_cust.search("Customers")
        self.add_cust.click_customers()
        self.add_cust.click_customers_options()
        self.add_cust.click_add_new()
        self.logger.info("***************Providing Customer Info*************")

        self.email = random_generator() + "@gmail.com" #hethi email genrator dima haka
        self.add_cust.enter_email(self.email)
        self.add_cust.enter_password("aziz123")
        self.add_cust.enter_first_name("aziz")
        self.add_cust.enter_last_name("issaoui")
        self.add_cust.select_gender("Male")
        self.add_cust.date_of_birth("12/03/2000")
        self.add_cust.enter_company_name("startup")
        self.add_cust.enter_tax_exempt()
        self.add_cust.select_newsletter("Your store name")
        self.add_cust.select_customer_role("Vendors")
        self.add_cust.select_manager_of_vendor("Vendor 1")
        self.add_cust.enter_admin_comments("hello this is aziz")
        self.add_cust.save()
        self.logger("**************Saving Customer Info**************")
        self.msg= self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("***************Customer Added Successfully*************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "Customer_Add.png")
            self.logger.error("************** Test failed****************")
            assert True == False
        self.logger.info("************** Test Ended ******************")











def random_generator(size=8, chars=string.ascii_lowercase + string.digits): # hethi tgeneratilna eemail bech kol mara manog3douch nestaamlou fard email
    return ''.join(random.choice(chars) for _ in range(size))




