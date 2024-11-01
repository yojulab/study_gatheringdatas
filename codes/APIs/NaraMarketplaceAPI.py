import requests

# ?&&&&&
url = 'https://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'
params ={'serviceKey' : 'ow0djIIbtYKcXjahX81pjlVfuA8kUj6DBQkALWCEeCXNuir3R0%2BLMOTTuhmW9Ms7R%2FAVfqb7cGIAazhHFttnPw=='
         , 'pageNo' : '1'
         , 'numOfRows' : '10'
         , 'type' : 'json'
         , 'bidNtceBgnDt' : '201712010000'
         , 'bidNtceEndDt' : '201712312359' }

response = requests.get(url, params=params)
print(response.content)