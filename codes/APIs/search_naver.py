import requests
import json

def main():
    uri = f'https://openapi.naver.com/v1/search/blog'
    params = {'query':'진​주'}
    headers = {
        'X-Naver-Client-Id':'WrU0qvrbTY5rxbKsl3gM'
        , 'X-Naver-Client-Secret':'FzTuyQGlGV'
    }
    response = requests.get(url=uri, params=params, headers=headers)  # like postman
    if response.status_code == 200:     # 200 == 200
        contents = json.loads(response.text)    # python에서 다루기 편하게 format 수정
        pass
    return 

if __name__ == '__main__':
    main()
    pass