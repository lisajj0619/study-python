#r6iLh2G2_9fkvZebz6eC
#f0xBf6Hqhw
#https://openapi.naver.com/v1/papago/n2mt
import urllib.request
import json

client_id = "r6iLh2G2_9fkvZebz6eC"
client_secret = "f0xBf6Hqhw"
encoding_text = urllib.parse.quote("집에 가고싶어")
data = f"source=ko&target=en&text={encoding_text}"
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)

#-H
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response = json.loads(response.read().decode("utf-8"))
    print(response['message']['result']['translatedText'])

    