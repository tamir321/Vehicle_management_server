from routs.vehicles import  Vehicle

import json


with open("cars.json","r") as f:
    my_cars = json.load(f)


print(my_cars)

jnk = {}
for key ,val  in my_cars.items():
    jnk[key] = Vehicle(**val)

print(jnk)

my_new_json ={}

for key , val in jnk.items():
    my_new_json[key]=val.json()

print(my_new_json)


with open("my_new_car","w") as f:
    json.dump(my_new_json,f,indent=4)


def my_sum(a,b,c):
    pass

y ={"a":3,"b":7,"c":9}

my_sum(**y)