from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from logger import logger 

# ---------------- ChromeDriverManager ----------------
class ChromeDriverManager:
    """Chromeブラウザを起動してdriverを取得するクラス（Selenium Managerを利用）"""

    def __init__(self) -> None:
        pass  # 今は遅延起動（あとで chrome_process() を呼ぶ）

    def chrome_option(self) -> Options:
        """起動オプションを設定（今回はウィンドウサイズのみ）"""
        options = Options()
        options.add_argument("--window-size=1280,800")
        return options

    def chrome_process(self) -> WebDriver:
        """webdriver.Chrome() で driver を生成"""
        options = self.chrome_option()
        driver: WebDriver = webdriver.Chrome(options=options)  # Selenium Manager が自動でdriverを準備
        return driver

# ---------------- GetElement ----------------
class GetElement:
    """ページ上の要素を取得するクラス"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    def get_id_element(self) -> WebElement:
        username_field: WebElement = self.driver.find_element(By.ID, "username")
        return username_field

    def get_pass_element(self) -> WebElement:
        password_field: WebElement = self.driver.find_element(By.NAME, "password")
        return password_field

    def get_check_box_element(self) -> WebElement:
        checkbox: WebElement = self.driver.find_element(By.XPATH, "//input[@type='checkbox']")
        return checkbox
    
    def get_login_btn_element(self) -> WebElement:
        login_button: WebElement = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        return login_button


# ---------------- ActionElement ----------------
class ActionElement:
    """要素に対するアクションを行うクラス"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    def input_element(self, element: WebElement, text: str) -> None:
        try:
            element.clear()
            element.send_keys(text)
            logger.info(f"要素に入力しました: {text}")
        except Exception as e:
            logger.error(f"入力処理に失敗: {e}")
            raise

    def click_element(self, element: WebElement) -> None:
        try:
            element.click()
            logger.info("要素をクリックしました")
        except Exception as e:
            logger.error(f"クリック処理に失敗: {e}")
            raise
