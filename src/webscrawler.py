from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

PATH_TO_CHROME_DRIVER = "C:\Webdriver\\bin\chromedriver.exe"

if __name__ == '__main__':
    with webdriver.Chrome(PATH_TO_CHROME_DRIVER) as driver:
        driver.get("https://www.doordash.com/")
        wait = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, "input"))
        )
        address_search_box = driver.find_element_by_tag_name("input")
        address_search_box.click()
        address_search_box.send_keys("6063 Iona Dr., Vancouver")
        address_search_box.send_keys(Keys.ENTER)
        address_search_box.submit()

        while True:
            continue
