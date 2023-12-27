# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력(https://www.w3schools.com/)
url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
browser.get(url)

# - 정보 획득
from selenium.webdriver.common.by import By
# 상품회사 리스트 : 
# element_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a > span.best")
# for index in range(len(element_companies)) :
for index in range(4) :
    element_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a > span.best")
    element_companies[index].click()
    time.sleep(1)       # 화면 완성 term
    # 제품 상세 제목 : div > h1
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="div > h1.title")
    print("App company Name : {}".format(element_title.text))
    
    browser.back()      # 제품 리스트로 이동
    time.sleep(1)       # 화면 완성 term
    pass
pass

# 브라우저 종료
browser.quit()