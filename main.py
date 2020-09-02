from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main(numb):
    print("검색어 입력: ")
    query1 = input()
    print("클릭할 기사에 포함될 제목 입력: ")
    query2 = input()
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome('C:\chromedriver', options=options)
    driver.get("http://www.naver.com")
    for i in range(numb):
        elem = driver.find_element_by_name("query")
        elem.send_keys(query1)
        elem.submit()
        elem2 = driver.find_element_by_partial_link_text(query2)
        elem2.click()
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.get("http://www.naver.com")
main(10000)
