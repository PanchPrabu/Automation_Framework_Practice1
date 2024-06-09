from selenium.webdriver.common.by import By


class SecondPage():

    def __init__(self, driver):

        self.driver = driver
        self.icon_button_css = "p[class='oxd-userdropdown-name']"
        self.logout_button_xpath = "//a[text()='Logout']"


    def icon_click(self):
        self.driver.find_element(By.CSS_SELECTOR,self.icon_button_css).click()


    def logout_click(self):
        self.driver.find_element(By.XPATH,self.logout_button_xpath).click()

