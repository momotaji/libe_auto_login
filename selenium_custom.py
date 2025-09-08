from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from logger import logger 

# ---------------- ChromeDriverManager ----------------
class ChromeDriverManager:
    """Chromeブラウザを起動してdriverを取得するクラス（Selenium Managerを利用）"""

    def __init__(self):
        try:
            options = self.chrome_option()             # 起動オプションを作成
            self.driver = self.chrome_process(options) # driverを生成
            logger.info("Chromeを起動しました！")
        except Exception as e:
            logger.error(f"Chromeの起動に失敗しました: {e}")
            raise  # エラーをそのまま投げて処理を停止

    def chrome_option(self):
        """起動オプションを設定（今回はウィンドウサイズのみ）"""
        options = Options()
        options.add_argument("--window-size=1280,800")
        return options

    def chrome_process(self, options):
        """webdriver.Chrome() で driver を生成"""
        return webdriver.Chrome(options=options)  # Selenium Manager が自動でdriverを準備

    def get_driver(self):
        """driverを返す"""
        return self.driver

# ---------------- GetElement ----------------
class GetElement:
    """ページ上の要素を取得するクラス"""

    def __init__(self, driver):
        self.driver = driver

    def get_id_element(self):
        username_field = self.driver.find_element(By.ID, "username")
        return username_field

    def get_pass_element(self):
        password_field = self.driver.find_element(By.NAME, "password")
        return password_field

    def get_check_box_element(self):
        checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox']")
        return checkbox
    
    def get_login_btn_element(self):
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        return login_button


# ---------------- ActionElement ----------------
class ActionElement:
    """要素に対するアクションを行うクラス"""

    def __init__(self, driver):
        self.driver = driver

    def input_element(self, element, text: str):
        try:
            element.clear()
            element.send_keys(text)
            logger.info(f"要素に入力しました: {text}")
        except Exception as e:
            logger.error(f"入力処理に失敗: {e}")
            raise

    def click_element(self, element):
        try:
            element.click()
            logger.info("要素をクリックしました")
        except Exception as e:
            logger.error(f"クリック処理に失敗: {e}")
            raise
