# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# %%
# url in address window
browser.get('https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033')

# %%
# element_path = '#swiper-wrapper-01f169110cf10240e3 > li.mnemitem_grid_item.swiper-slide.swiper-slide-active > div > div > div.mnemitem_detailbx > div.mnemitem_tx_thmb > a > div.mnemitem_tit > span.mnemitem_goods_tit'
# element = browser.find_element(by=By.CSS_SELECTOR, value=element_path)  # 단수 찾기
# type(element) # <span class="mnemitem_goods_tit">몰리스 쉬야응가 1회용 패드 L 50매</span>

# # %%
# element.text

# # %%
# element.get_attribute('class')

# %% [markdown]
# ### 여러개 element 가져오기

# %%
element_title_path = '.mnemitem_goods_tit'
elements = browser.find_elements(by=By.CSS_SELECTOR, value=element_title_path)
# type(elements), type(elements[0])

# %%
for webelement in elements:
    try :
        print(webelement.text)
    except :
        pass

# %% [markdown]
# ### paginations
# - page 2 tag : #area_itemlist > div.paginate > div > a:nth-child(2)
# - page 7 tag : #area_itemlist > div.paginate > div > a:nth-child(7)

# %%
# element_path = '#area_itemlist > div.paginate > div > strong'
# pagination = browser.find_element(by=By.CSS_SELECTOR, value=element_path)
# pagination.click()

import time

pagination_links = browser.find_elements(By.CSS_SELECTOR, 'div.paginate > strong, div.paginate > div > a')
for page_number in range(len(pagination_links))[9:]:  # 첫 페이지는 tag 달라짐
    # Refresh pagination_links to avoid stale element issues
    pagination_links = browser.find_elements(By.CSS_SELECTOR, 'div.paginate > strong, div.paginate > div > a')

    # element_path = 'div.paginate > div > a:nth-of-type({})'.format(page_number)
    element_path = pagination_links[page_number].get_attribute('outerHTML')
    try :
        # pagination = browser.find_element(by=By.CSS_SELECTOR, value=element_path)
        pagination_links[page_number].click()    
        print('성공 : {}'.format(element_path))
        
        time.sleep(3)
        element_title_path = '.mnemitem_goods_tit'
        webelements = browser.find_elements(by=By.CSS_SELECTOR, value=element_title_path)
        
        for webelement in webelements:
            try :
                print(webelement.text)
            except :
                pass
        
    except :
        print('실패 : {}'.format(element_path))
        pass



# %%
browser.quit()

