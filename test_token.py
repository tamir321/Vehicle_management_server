import requests


url_add_car = "http://localhost:9000/add_car/2"

payload_add_car = {
              "car_name": "string",
              "car_model": "string",
              "car_id": 0
            }


res = requests.post(url=url_add_car,json=payload_add_car)

print(res)

token_url= 'http://localhost:9000/token1'
#username=tamir&password=password
payload = {"username":"tamir","password":"password"}


res = requests.post(url=token_url,json=payload)
print(res)

token = res.json()['access_token']

header = {'Authorization':f'Bearer {token}'}

session = requests.session()
session.headers.update(header)

res2 = session.post(url=url_add_car,json=payload_add_car)
print(res2)
