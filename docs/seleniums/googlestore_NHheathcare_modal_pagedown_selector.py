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
url = 'https://play.google.com/store/apps/details?id=com.nhlife.customer.healthcare&hl=ko-KR'
browser.get(url)

# - 정보 획득
from selenium.webdriver.common.by import By
# 평가 및 리뷰 클릭
selector_element = '#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > header > div > div:nth-child(2) > button > i'
browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()

# modal 스크롤 영역 
# document.querySelector('div.fysCi').style.overflow
selector_element = 'div.fysCi'
element_scrollable_div = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)

# 댓글 모두 표시까지 페이지를 다운합니다.
# within javascript in browser
# var scrollableDiv = document.querySelector('div.fysCi');
# scrollableDiv.scrollTo(0, scrollableDiv.scrollHeight);
previous_scrollHeight = 0

# pagedown 전 댓글 갯수 확인 : div.RHo1pe
elements_comment = browser.find_elements(by=By.CSS_SELECTOR, value='div.RHo1pe')
print('count comment before done scroll : {}'.format(len(elements_comment)))
while True:
    browser.execute_script('arguments[0].scrollTo(arguments[1], arguments[0].scrollHeight);'
                           , element_scrollable_div, previous_scrollHeight)

    current_scrollHeight = browser.execute_script("return arguments[0].scrollHeight"
                                                  , element_scrollable_div)
    if previous_scrollHeight >= current_scrollHeight:
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass

# pagedown 전 댓글 갯수 확인 : div.RHo1pe
elements_comment = browser.find_elements(by=By.CSS_SELECTOR, value='div.RHo1pe')
print('count comment after done scroll : {}'.format(len(elements_comment)))

pass

# 브라우저 종료
browser.quit()