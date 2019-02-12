import requests
import json

addr="서울시 종로구 혜화로 42"
url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
headers = {"Authorization": "KakaoAK 1305118b2161261e4dcf82d17364d87c"}
res=requests.get(url,headers=headers).text
result= json.loads(str(res))
match_first = result['documents'][0]['address']
print(match_first['x'])
print(match_first['y'])


def getLatLng(addr):
  url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
  headers = {"Authorization": "KakaoAK 1305118b2161261e4dcf82d17364d87c"}
  result = json.loads(str(requests.get(url,headers=headers).text))
  match_first = result['documents'][0]['address']

  return float(match_first['y']), float(match_first['x'])

addr="서울시 종로구 혜화로 42"
ans=getLatLng(addr)
print(ans)
