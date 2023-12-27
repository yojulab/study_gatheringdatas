# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=1
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=2
# ...
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=10

# * 웹 크롤링 동작
# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time
# ChromeDriver 실행

from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
# Chrome 옵션 설정
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# WebDriver 생성
webdriver_manager_dricetory = ChromeDriverManager().install()

driver = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)         # - chrome browser 열기

from selenium.webdriver.common.by import By          # - 정보 획득
url = "https://www.coupang.com/np/campaigns/348".format()
from selenium.common.exceptions import NoSuchElementException

# 페이지로 이동
driver.get(url)  # 실제 페이지 URL로 변경

def click_page_number(page_number):
    """해당 페이지 번호를 클릭합니다."""
    try:
        page_link = driver.find_element(By.CSS_SELECTOR, f"a[data-page='{page_number}']")
        # page_link.click()
        driver.execute_script("arguments[0].click();", page_link)
    except NoSuchElementException:
        print(f"페이지 {page_number}를 찾을 수 없습니다.")

def click_next_page():
    """다음 페이지 버튼을 클릭합니다."""
    next_page_button = driver.find_element(By.CSS_SELECTOR, ".next-page")
    next_page_button.click()

def click_previous_page():
    """이전 페이지 버튼을 클릭합니다."""
    previous_page_button = driver.find_element(By.CSS_SELECTOR, ".prev-page-dimmed")
    previous_page_button.click()

# 예시:
click_page_number(5)  # 5페이지 이동
click_next_page()  # 다음 페이지로 이동
click_previous_page()  # 이전 페이지로 이동

# 브라우저 닫기
driver.quit()
