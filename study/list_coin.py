import requests
import csv

url = "https://api.upbit.com/v1/market/all?isDetails=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()
print(data)
with open('response.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data[0].keys())
    for item in data:
        writer.writerow(item.values())

print("Data saved as response.csv")