import pandas as pd
from config.settings import SIGNUP_INPUT_FILE, SIGNUP_OUTPUT_FILE, URL_SIGNUP_PAGE
from utils.excel_handler import read_excel, write_excel
from utils.web_driver import get_driver
from pages.signup_page import SignUpPage

def run_signup_tests():
    # Đọc dữ liệu từ file input
    data = read_excel(SIGNUP_INPUT_FILE)
    results = []

    driver = get_driver()
    signup_page = SignUpPage(driver)

    for _, row in data.iterrows():
        signup_page.load(URL_SIGNUP_PAGE)
        
        firstname = row['firstname']
        lastname = row['lastname']
        country = row['country']
        phone = row['phone']
        email = row['email']
        password = row['password']
        expected = row['expected']

        # Thực hiện đăng nhập và kiểm tra kết quả
        signup_page.enter_firstname(firstname)
        signup_page.enter_lastname(lastname)
        signup_page.enter_country(country)
        signup_page.enter_phone(phone)
        signup_page.enter_email(email)
        signup_page.enter_password(password)
        signup_page.submit()
        
        # Kiểm tra kết quả đăng nhập
        actual_result, exception = signup_page.check_signup_status()
        result = {
            'time': pd.Timestamp.now(),
            'firstname': firstname,
            'lastname': lastname,
            'country': country,
            'phone': phone,
            'email': email,
            'password': password,
            'expected': expected,
            'actual': actual_result,
            'status': 'Pass' if (expected == actual_result) else 'Fail',
            'exception': exception
        }
        results.append(result)

        if actual_result == 'Signup Success':
            signup_page.load(URL_SIGNUP_PAGE)
        
    driver.quit()
    # Ghi kết quả vào file output sau khi hoàn thành tất cả trường hợp
    results_df = pd.DataFrame(results)
    write_excel(SIGNUP_OUTPUT_FILE, results_df)

