from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=375,812")  # iPhone X dimensions
    # options.add_argument(
    #     "--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) "
    #     "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    
    driver = webdriver.Chrome(options=options)
    return driver
