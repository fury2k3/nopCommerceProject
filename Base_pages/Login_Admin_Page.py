from selenium.webdriver.common.by import By

#hethya just page bech nhot feha locators mte3i akahaw
#ndeclari melowl class w baad li declarithom nestaamelhom lota fi chakl fonctionet

class Login_Admin_Page:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    btn_loginXpath= "//button[normalize-space()='Log in']"
    logout_Xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
            self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
    def click_btn(self):
        self.driver.find_element(By.XPATH,self.btn_loginXpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_Xpath).click()


