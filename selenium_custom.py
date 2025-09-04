import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ---------------- ログ設定 ----------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# ---------------- ChromeDriverManager ----------------
class ChromeDriverManager:
    """Chromeブラウザを起動するクラス"""

    def __init__(self):
        try:
            options = self.chrome_option()             # 起動オプション設定
            self.driver = self.chrome_process(options) # driver生成
            logger.info("Chromeを起動しました！")
        except Exception as e:
            logger.error(f"Chromeの起動に失敗しました: {e}")
            raise

    def chrome_option(self):
        """ウィンドウサイズを設定"""
        options = Options()
        options.add_argument("--window-size=1280,800")
        return options

    def chrome_process(self, options):
        """webdriver.Chrome() で driver を生成"""
        return webdriver.Chrome(options=options)

    def get_driver(self):
        """driverを外部に返す"""
        return self.driver

# ---------------- GetElement ----------------
class GetElement:
    """ページ上の要素を取得するクラス"""

    def __init__(self, driver):
        self.driver = driver

    def get_id_element(self):
        return self.driver.find_element(By.ID, "username")  # 仮のID

    def get_pass_element(self):
        return self.driver.find_element(By.NAME, "password")  # 仮のNAME

    def get_check_box_element(self):
        return self.driver.find_element(By.XPATH, "//input[@type='checkbox']")

    def get_login_btn_element(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")

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
