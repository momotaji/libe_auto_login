from selenium_custom import ChromeDriverManager, GetElement, ActionElement
from selenium.webdriver.remote.webdriver import WebDriver  # 型を使うために import

if __name__ == "__main__":
    # Chrome起動
    manager: ChromeDriverManager = ChromeDriverManager()
    driver: WebDriver = manager.chrome_process()  # get_driver() が WebDriver を返す想定
    driver.get("https://www.google.com")
