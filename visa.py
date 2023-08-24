import os
from datetime import datetime, timedelta
from typing import Annotated
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import random
import logging

class Payment(BaseModel):
    card_number :str
    castumer : str
    amout :int

app = FastAPI()
i,j = 0 ,0
fail_transction = []
good_transaction = []


@app.get("/")
async def root():
    return {"message": "hello word"}


@app.post("/run_transaction")
async def run_traansaction(pay :Payment):
    fail_pass= random.choice([False,True,True,True,True])
    global i ,j
    if fail_pass:
        i +=1
        transaction = {i:pay}
        good_transaction.append(transaction)
        return {"approve":{"transaction_id":i}}
    else:
        j +=1
        fail_transction.append({j:pay})
        return {"failed":{"transaction_id":j}}



@app.get("/good")
def good():
    return good_transaction





if __name__ == "__main__":
    my_port = int(os.getenv("PORT"))
    print("my_port",my_port)
    uvicorn.run(app, host="0.0.0.0", port=my_port)


