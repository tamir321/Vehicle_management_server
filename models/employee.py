from pydantic import BaseModel
from typing import List, Union
from datetime import date, datetime, time, timedelta

class Employee(BaseModel):
    row: Union[int, None] = None # python 3.10   int | None = None
    employee_id: int
    first_name: str
    last_name: str
    license_expiration : date
    license_group : str

    class Config:
        schema_extra = {
            "example": {

                "employee_id": 8 ,
                "first_name": "first",
                "last_name": "last",
                "license_expiration": "2008-09-15",
                "license_group": "A",
            }
        }


async def filter_employees(emp_array, filter):
    result = emp_array
    print(filter.items())
    for key,val in filter.items():
        result = list(filter(lambda x : x[key] == val,result))
    return result