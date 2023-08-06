from pydantic import BaseModel
from typing import List, Union
from datetime import date, datetime, time, timedelta

class Vehicle(BaseModel):
    row: Union[int, None] = None # python 3.10   int | None = None
    Plate_id: int
    Manufacture: str
    Model: str
    current_driver : Union[int,None] =None
    current_mileage : int
    service_duration :int
    last_service : int
    Group : str

    class Config:
        schema_extra = {
            "example": {

                "Plate_id": 8,
                "Manufacture": "GM",
                "Model": "LYRIQ",

                "current_mileage" : 1300 ,
                "service_duration" :15000,
                "last_service" : 0,
                "Group" : "A"
            }
        }


async def filter_employees(emp_array, filter):
    result = emp_array
    print(filter.items())
    for key,val in filter.items():
        result = list(filter(lambda x : x[key] == val,result))
    return result