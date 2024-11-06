import requests
import json

def main():
    uri = f'https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize'
    headers = {
        'X-NCP-APIGW-API-KEY-ID':'r4sjp0a0uc'
        , 'X-NCP-APIGW-API-KEY':'di7f7MT89o6xnqE2nkPvg1yoVLv1TdCa1EqtD08U'
        , 'Content-Type':'application/json'
    }
    bodys = {
            "document": {
                "title": "'금투세 폐지'…국내증시 날개 달까",
                "content": "동학개미(국내 개인투자자)들의 숙원이었던 금융투자소득세(금투세)가 마침내 폐지로 가닥이 잡혔다. 야당이 장고 끝에 금투세 폐지에 '동의'하면서, 금투세는 유예 기간 종료를 2개월 앞두고 4년 만에 사라지게 됐다. 투자자들은 너무 늦었다는 반응과 함께 이제라도 폐지된다는 점에서 대부분 긍정적인 평가가 나온다. 5일 한국거래소에 따르면 코스피는 전 거래일(2582.96)보다 46.61포인트(1.83%) 오른 2588.97에 장을 마쳤다. 특히 코스닥 지수는 3.43% 급등하며, 금투세 폐지에 대한 기대감이 더 크게 반영됐다. 이날 코스닥 시가총액 상위 종목인 알테오젠(9.26%), 에코프로비엠(7.25%), 에코프로(7.37%), HLB(4.86%), 리가켐바이오(8.96%), 엔켐(6.62%), 휴젤(7.48%), 삼천당제약(4.90%), 클래시스(4.15%) 등은 일제히 초강세를 나타냈다."
            },
            "option": {
                "language": "ko",
                "model": "news",
                "tone": 3,
                "summaryCount": 1
            }
        }
    response = requests.post(url=uri, headers=headers, data=json.dumps(bodys))
    contents = json.loads(response.text)
    return 

if __name__ == '__main__':
    main()
    pass