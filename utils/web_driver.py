from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Chạy ẩn trình duyệt nếu cần
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options)
    return driver

