import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Add_Customer_Page:
    # Set up the locators
    link_customers_menu_Xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_option_Xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_new_Xpath = "//a[normalize-space()='Add new']"
    input_email_Xpath = "//input[@id='Email']"
    input_password_Xpath = "//input[@id='Password']"
    input_first_names_Xpath = "//input[@id='FirstName']"
    input_lastname_Xpath = "//input[@id='LastName']"
    input_gender_male_Xpath = "//input[@id='Gender_Male']"
    input_gender_female_Xpath = "//input[@id='Gender_Female']"
    text_date_of_birth_ID = "DateOfBirth"
    input_company_name_Xpath = "//input[@id='Company']"
    input_tex_exempt_Xpath = "//input[@id='IsTaxExempt']"
    choose_newsletter_customer_Xpath = "//span[@aria-expanded='true']//input[@role='searchbox']"
    newsletter_your_store_name_Xpath = "//li[@title='Your store name']"
    newsletter_test_store2_Xpath = "//li[@title='Test store 2']"
    customer_role_registered_Xpath = "//li[@title='Registered']"
    customer_role_Administrators_Xpath = "//li[@title='Administrators']"
    customer_role_forum_moderator_Xpath = "//li[@title='Forum Moderators']"
    customer_role_guests_Xpath = "//li[@title='Guests']"
    customer_role_vendor_Xpath = "//li[@title='Vendors']"
    input_admin_comment_Xpath = "//textarea[@id='AdminComment']"
    link_save_Xpath = "//textarea[@id='AdminComment']"
    drop_down_vendor_Xpath = "//select[@id='VendorId']"

    def __init__(self, driver):
        self.driver = driver

    def click_customers(self):
        # Wait until the customers menu is visible and clickable
        customers_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.link_customers_menu_Xpath))
        )

        # Use ActionChains to hover over the customers menu
        actions = ActionChains(self.driver)
        actions.move_to_element(customers_menu).perform()  # Hover over the menu item

        # Wait for the submenu to appear and be clickable
        customers_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_customers_option_Xpath))
        )

        # Click the customers menu
        customers_option.click()

    def click_customers_options(self):
        # Wait until the customers option is visible and clickable
        customers_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.link_customers_option_Xpath))
        )

        # Hover over the customer options and ensure it's clickable
        actions = ActionChains(self.driver)
        actions.move_to_element(customers_option).perform()  # Hover over the submenu item

        # Wait for the element to be clickable before clicking
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_customers_option_Xpath))
        )

        # Click on the customers option
        customers_option.click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.add_new_Xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.input_email_Xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.input_password_Xpath).send_keys(password)

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.input_first_names_Xpath).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.input_lastname_Xpath).send_keys(last_name)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.input_gender_male_Xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.input_gender_female_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.input_gender_female_Xpath).click()

    def date_of_birth(self, date_of_birth):
        self.driver.find_element(By.XPATH, self.text_date_of_birth_ID).send_keys(date_of_birth)

    def enter_company_name(self, company_name):
        self.driver.find_element(By.XPATH, self.input_company_name_Xpath).send_keys(company_name)

    def enter_tax_exempt(self):
        self.driver.find_element(By.XPATH, self.input_tex_exempt_Xpath).click()
        time.sleep(3)

    def select_newsletter(self, value):
        elements = self.driver.find_elements(By.XPATH, self.choose_newsletter_customer_Xpath)
        newsletter_field = elements[0]
        newsletter_field.click()
        time.sleep(3)
        if value == "Your store name":
            self.driver.find_element(By.XPATH, self.newsletter_your_store_name_Xpath).click()
        elif value == "Test store 2":
            self.driver.find_element(By.XPATH, self.newsletter_test_store2_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.newsletter_your_store_name_Xpath).click()

    def select_customer_role(self, role):
        elements = self.driver.find_elements(By.XPATH, self.choose_newsletter_customer_Xpath)
        customer_role = elements[1]
        customer_role.click()
        time.sleep(3)
        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.customer_role_Administrators_Xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.customer_role_forum_moderator_Xpath)
        elif role == "Registered":
            pass
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.customer_role_vendor_Xpath).click()
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul/li[1]/span").click()

            self.listitem = self.driver.find_element(By.XPATH, self.customer_role_guests_Xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click()", self.listitem)

    def select_manager_of_vendor(self, value):
        drp_down = Select(self.driver.find_element(By.XPATH, self.drop_down_vendor_Xpath))
        drp_down.select_by_visible_text(value)

    def enter_admin_comments(self, admin_comments):
        self.driver.find_element(By.XPATH, self.input_admin_comment_Xpath).send_keys(admin_comments)

    def save(self):
        self.driver.find_element(By.XPATH, self.link_save_Xpath).click()
