import requests

def main():
    # 자료 요청
    uri = f'http://openapi.seoul.go.kr:8088/76706545646f74743534576e594c47/json/bikeList/1/5/'
    response = requests.get(url=uri)

    if response.status_code == 200:
        print(f'{response.text}') 
        import json
        data_dict = json.loads(response.text)
        data_dict
        # {'rentBikeStatus': {'list_total_count': 5, 'RESULT': {...}, 'row': [...]}}
        type(data_dict)
        # <class 'dict'>
        # data = {
        #     'name': ["Choi", "Choi", "Choi", "Kim", "Park"], 
        #     'year': [2013, 2014, 2015, 2016, 2017], 
        #     'points': [1.5, 1.7, 3.6, 2.4, 2.9]
        #     } 
        data_bikes = {"stationName":[]
                , "parkingBikeTotCnt":[]}
        for row in data_dict['rentBikeStatus']['row']:
            print(f'stationName : {row["stationName"]}, parkingBikeTotCnt : {row["parkingBikeTotCnt"]}')
            data_bikes['stationName'].append(row["stationName"])
            pass
        pass
    else :
        pass    # 에러 메세지 출력
    return 

if __name__ == '__main__':
    main()
    pass