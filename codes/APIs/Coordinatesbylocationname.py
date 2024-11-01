import requests

# ?&
url = 'http://api.openweathermap.org/geo/1.0/direct'
params ={'q':'seoul'
         , 'appid':'cbdbbb3a98df1289f73ac00a15f1cd46'}

response = requests.get(url, params=params)
# print(response.content)
import json
content = json.loads(response.content)

# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["study_finance"]
# collection 작업
collection = database['coordinatesbylocationonname']

result = collection.insert_many(content)