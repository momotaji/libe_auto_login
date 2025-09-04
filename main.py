from selenium_custom import ChromeDriverManager, GetElement, ActionElement


if __name__ == "__main__":
    # Chrome起動
    manager = ChromeDriverManager()
    driver = manager.get_driver()

    # サンプルページを開く（仮）
    driver.get("https://www.google.com")

    # ここから GetElement や ActionElement を使って要素操作していける


