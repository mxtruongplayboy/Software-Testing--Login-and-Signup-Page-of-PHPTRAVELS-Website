import time
from selenium.webdriver.common.by import By
from config.settings import URL_HOME_PAGE
from utils.get_error_message import get_error_message

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)
        time.sleep(2)

    def enter_username(self, username):
        email_field = self.driver.find_element(By.ID, 'email')
        email_field.clear()
        email_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.clear()
        password_field.send_keys(password)

    def submit(self):
        self.driver.find_element(By.ID, 'submitBTN').click()


    def check_login_status(self):
        try:
            time.sleep(2)
            current_url = self.driver.current_url
            if current_url == URL_HOME_PAGE:
                return 'Login Success', ''
            else:
                email_field = self.driver.find_element(By.ID, 'email')
                validation_message = email_field.get_attribute("validationMessage")
                if validation_message:
                    return 'Login Fail', validation_message
                else:
                    error_message = get_error_message(self.driver)
                    return 'Login Fail', error_message
        except Exception as e:
            return 'Login Fail', str(e)

