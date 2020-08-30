from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main(numb):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome('C:\chromedriver', options=options)
    driver.get("http://www.naver.com")
    for i in range(numb):
        elem = driver.find_element_by_name("query")
        elem.send_keys("**** ***")
        elem.submit()
        elem2 = driver.find_element_by_partial_link_text("**** ***")
        elem2.click()
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.get("http://www.naver.com")

main(10000)
