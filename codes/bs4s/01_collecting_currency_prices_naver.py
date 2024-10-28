import requests     # url 주소 입력과 해당 html 가져오기

# 브라우저 주소창
response = requests.get('https://finance.daum.net/domestic/exchange')

# print(response.text)      # html contents

# - 환율 변동 가격 수집
# refer : https://finance.naver.com/marketindex/
# <span class="value">149.5400</span>
# span.value
from bs4 import BeautifulSoup   # html 해석기

# Dom 구조화
soup = BeautifulSoup(response.text, 'html.parser')


currency_prices = soup.select('td.pR > span.num')
type(currency_prices)

for currency in currency_prices:
    print(f'Tag : {currency}, Currency Price : {currency.text}')
    pass

pass