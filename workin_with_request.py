import json

import  requests

my_pet = {
  "id": 10,
  "category": {
    "id": 1,
    "name": "dogs"
  },
  "name": "doggie_1"

}
header = { 'accept': 'application/xml'}
url= "https://petstore.swagger.io/v2/pet"
res = requests.post(url=url,json=my_pet,headers=header)

print(res)

session = requests.session()
