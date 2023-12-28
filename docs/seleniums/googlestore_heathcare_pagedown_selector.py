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
url = 'https://play.google.com/store/apps/details?id=com.sec.android.app.shealth&hl=ko-KR'
browser.get(url)

# - 정보 획득
from selenium.webdriver.common.by import By
# 평가 및 리뷰 클릭
selector_element = '#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > header > div > div:nth-child(2) > button > i'
browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()

# modal 스크롤 영역 
selector_element = '#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div > div:nth-child(2)'
element_scrollable_div = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)

# JavaScript를 사용하여 해당 div 요소 내부를 맨 아래로 스크롤합니다.
browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', element_scrollable_div)

pass

# 브라우저 종료
browser.quit()