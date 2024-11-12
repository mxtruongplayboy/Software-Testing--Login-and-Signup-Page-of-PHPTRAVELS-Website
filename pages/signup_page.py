import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from config.settings import URL_SIGNUP_SUCCESS_PAGE
from utils.get_error_message import get_error_message

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)
        time.sleep(2)

    def enter_firstname(self, firstname):
        email_field = self.driver.find_element(By.ID, 'firstname')
        email_field.clear()
        email_field.send_keys(firstname)
    
    def enter_lastname(self, lastname):
        email_field = self.driver.find_element(By.ID, 'last_name')
        email_field.clear()
        email_field.send_keys(lastname)
    
    def enter_country(self, country):
        dropdown_button = self.driver.find_element(By.CSS_SELECTOR, ".btn.dropdown-toggle.btn-light")
        dropdown_button.click()
        search_field = self.driver.find_element(By.CLASS_NAME, "bs-searchbox").find_element(By.TAG_NAME, "input")
        search_field.send_keys(country)
        search_field.send_keys(Keys.ENTER)

    def enter_phone(self, phone):
        password_field = self.driver.find_element(By.ID, 'phone')
        password_field.clear()
        password_field.send_keys(phone)
    
    def enter_email(self, email):
        password_field = self.driver.find_element(By.ID, 'user_email')
        password_field.clear()
        password_field.send_keys(email)
    
    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.clear()
        password_field.send_keys(password)

    def submit(self):
        submit_button = self.driver.find_element(By.ID, 'submitBTN') 
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", submit_button)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def check_signup_status(self):
        try:
            time.sleep(2)
            current_url = self.driver.current_url
            if current_url == URL_SIGNUP_SUCCESS_PAGE:
                return 'Signup Success', ''
            else:
                submit_button = self.driver.find_element(By.ID, 'submitBTN')
                disabled_status = submit_button.get_attribute("disabled")
                if disabled_status:
                    error_message = get_error_message(self.driver)
                    return 'Signup Fail', error_message
                else:
                    fields_to_check = ['firstname', 'last_name', 'phone', 'user_email', 'password']
                    for field_id in fields_to_check:
                        try:
                            field = self.driver.find_element(By.ID, field_id)
                            validation_message = field.get_attribute("validationMessage")
                            if validation_message:
                                return 'Signup Fail', f"{field_id}: {validation_message}"
                        except:
                            continue
                    search_field = self.driver.find_element(By.CLASS_NAME, "selectpicker")
                    validation_message = search_field.get_attribute("validationMessage")
                    if validation_message:
                        return 'Signup Fail', f"country: {validation_message}"
                    error_message = get_error_message(self.driver)
                    return 'Signup Fail', error_message
        except Exception as e:
            # Trường hợp gặp lỗi trong quá trình kiểm tra
            return 'Login Fail', str(e)

