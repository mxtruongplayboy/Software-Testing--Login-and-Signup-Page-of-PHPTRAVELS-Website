import pandas as pd
from config.settings import LOGIN_INPUT_FILE, LOGIN_OUTPUT_FILE, URL_LOGIN_PAGE, URL_LOGOUT_PAGE
from utils.excel_handler import read_excel, write_excel
from utils.web_driver import get_driver
from pages.login_page import LoginPage

def run_login_tests():
    data = read_excel(LOGIN_INPUT_FILE)
    results = []

    driver = get_driver()
    login_page = LoginPage(driver)
    login_page.load(URL_LOGIN_PAGE)

    for _, row in data.iterrows():

        username = row['username']
        password = row['password']
        expected = row['expected']

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.submit()
        
        actual_result, exception = login_page.check_login_status()
        result = {
            'time': pd.Timestamp.now(),
            'username': username,
            'password': password,
            'expected': expected,
            'actual': actual_result,
            'status': 'Pass' if (expected == actual_result) else 'Fail',
            'exception': exception
        }
        results.append(result)

        if actual_result == 'Login Success':
            login_page.load(URL_LOGOUT_PAGE)
            login_page.load(URL_LOGIN_PAGE)
        
    driver.quit()
    results_df = pd.DataFrame(results)
    write_excel(LOGIN_OUTPUT_FILE, results_df)
