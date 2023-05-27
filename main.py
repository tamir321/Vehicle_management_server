"""
# install fastapi
pip install fastapi

# install uvicorn -Uvicorn is an ASGI web server implementation for Python.
pip install uvicorn

run the code - uvicorn main:app --reload
"""
from fastapi import FastAPI
import uvicorn
from business_logic.csv_convertor import CsvConvertor
from business_logic import globals
from routs import employees

globals.init()


globals.employess = CsvConvertor(globals.employee_file)

app = FastAPI()

app.include_router(employees.router)

@app.get("/" ,tags = ["web-server"])
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)