from selenium_custom import ChromeDriverManager, GetElement, ActionElement


if __name__ == "__main__":
    # Chrome起動
    manager = ChromeDriverManager()
    driver = manager.get_driver()
    driver.get("https://www.google.com")

