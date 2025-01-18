from selenium.webdriver.common.by import By


class search_customer_page:

    email_XPATH = "//input[@id='SearchEmail']"
    first_name_XPATH = "//input[@id='SearchFirstName']"
    last_name_XPATH = "//input[@id='SearchLastName']"
    searchbtn_XPATH = "//button[@id='search-customers']"
    tblsearchresult_XPATH = "//div[@class='row']//div[@class='col-md-12']"
    table_XPATH= "//*[@id='customers-grid']"
    tablerow_XPATH = "//*[@id='customers-grid']//tbody/tr"
    tablecolumns_XPATH = "//*[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.email_XPATH).clear()
        self.driver.find_element(By.XPATH,self.email_XPATH).send_keys(email)
    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH,self.first_name_XPATH).clear()
        self.driver.find_element(By.XPATH,self.first_name_XPATH).send_keys(firstname)
    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH,self.last_name_XPATH).clear()
        self.driver.find_element(By.XPATH,self.last_name_XPATH).send_keys(lastname)
    def setSearch(self):
        self.driver.find_element(By.XPATH,self.searchbtn_XPATH).click()

    def getNumberRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tablerow_XPATH))
    def getNumberColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tablecolumns_XPATH))

    def search_customer_by_email(self, email):
        flag = False
        for r in range(1,self.getNumberRows()+1):
            self.driver.find_element(By.XPATH,self.table_XPATH)
            emailid = self.driver.find_element(By.XPATH,"//*[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if email == emailid:
                flag = True
                break
                return flag
    def search_customer_by_name(self, name):
        flag =False
        for r in range (1,self.getNumberRows()+1):
            self.driver.find_element(By.XPATH,self.table_XPATH)
            namee = self.driver.find_element(By.XPATH,"//*[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == namee:
                flag = True
                break
                return flag












