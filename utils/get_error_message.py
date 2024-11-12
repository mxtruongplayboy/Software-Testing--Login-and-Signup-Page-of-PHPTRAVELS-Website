from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_error_message(driver):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".vt-card.error"))
        )
        error_message = element.find_element(By.CLASS_NAME, 'text-group').find_element(By.TAG_NAME, 'p').text
        return error_message
    except:
        return None
