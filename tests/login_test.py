import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from pages.LoginPage import FirstPage
from pages.HomePage import SecondPage
from utils import utils as envParam
import moment



@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver =self.driver

        driver.get(envParam.URL)

        login =FirstPage(driver)
        login.enter_username(envParam.USERNAME)
        login.enter_password(envParam.PASSWORD)
        login.click_login()


       # driver.find_element(By.NAME,"username").send_keys("Admin")
       # driver.find_element(By.NAME,"password").send_keys("admin123")
       # driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = SecondPage(driver)
            homepage.icon_click()
            homepage.logout_click()
            x = driver.title
            assert x == 'OrangeHRM'

        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currentTime=moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName=envParam.whoami()
            screenshotName=testName+"_"+currentTime
            allure.attach(self.driver.get_screenshot_as_png(),name="screenshotName",attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/USER/PycharmProjects/Automation_Framework_Practice1/screenshots" +screenshotName+".PNG")
            raise

        except:
            print("There was an exception")
            currentTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = envParam.whoami()
            screenshotName = testName + "_" + currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshotName",
                          attachment_type=allure.attachment_type.PNG)
            raise

        else:
            print("No Exceptions occured")

        finally:
            print("I am inside the finally block")



        #driver.find_element(By.CSS_SELECTOR,"p[class='oxd-userdropdown-name']").click()
       # driver.find_element(By.XPATH,"//a[text()='Logout']").click()
        time.sleep(2)


