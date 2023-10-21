import requests

response = requests.request('GET', 'https://api.upbit.com/v1/candles/minutes/1?market=KRW-BTC&count=10')
print(response.text)