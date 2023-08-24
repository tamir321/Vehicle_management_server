import os
from datetime import datetime, timedelta
from typing import Annotated

import requests
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import random
from visa import Payment

class Car(BaseModel):
    car_number :str
    car_model : str
    price :int

class Crad(BaseModel):
    card_number :str
    customer : str

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "hello word"}


@app.post("/buy_car")
async def run_traansaction(car :Car,card :Crad):
    visa_server = os.getenv("MOSHE")
    visa_port = os.getenv("LIYA")
    visa_url = f'http://{visa_server}:{visa_port}/run_transaction'
    payload = Payment(card_number=card.card_number,castumer = card.customer,amout=car.price)
    payload = {"card_number":card.card_number,"castumer" : card.customer,"amout":car.price}
    res = requests.post(url=visa_url,json=payload)
    if res.status_code<300:
        if res.json().get("approve"):
            print("I was here")
        return res.json()
    else:
        return {"message":"Huston we have"}




if __name__ == "__main__":
    my_port = int(os.getenv("PORT"))
    print("my_port",my_port)
    uvicorn.run(app, host="0.0.0.0", port=my_port)


