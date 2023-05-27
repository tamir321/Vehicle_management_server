from fastapi import APIRouter ,UploadFile, HTTPException
from typing import List
from fastapi.responses import FileResponse ,HTMLResponse
from models.employee import Employee #,filter_employees
from business_logic import globals
from json2html import *

router = APIRouter()



@router.get("/employee",tags = ["employee"])
async def get_all_employees()-> List[Employee]:
    return globals.employess.json_array

@router.get("/employee/{employee_id}" ,tags = ["employee"])
async def get_employee_by_id(employee_id) -> List[Employee]:
    emp = list(filter(lambda x :x["employee_id"]==employee_id,globals.employess.json_array))
    return emp


@router.post("/employee",tags = ["employee"])
async def add_new_employee(emp :Employee ):
    if len(await get_employee_by_id(emp.employee_id)) == 0:
        res = await globals.employess.append_list(emp)
        return res
    else:
        HTTPException(status_code=404, detail="employee all ready exist")

@router.put("/employee/{employee_id}",tags = ["employee"])
async def update_employee(employee_id:int ,emp: Employee):
    update_emp =await get_employee_by_id(employee_id=employee_id)
    if len(update_emp)<1:
        HTTPException(status_code=404, detail="employee does not exist ")
    res = await globals.employess.update_list({"employee_id":employee_id},dict(emp))
    return res


@router.post("/uploadfile/",tags = ["employee"])
async def create_upload_file(file: UploadFile ):

    return {"filename": file.filename,
            "type":file.content_type}

@router.get("/employees/file/",tags = ["employee"], response_class=FileResponse)
async def read_data():
    response = FileResponse(globals.employess.csv_file_path, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=downloaded_file.csv"
    return response

@router.get("/employees/html",tags = ["employee"], response_class=HTMLResponse)
def get_employee_html():
    return json2html.convert(json=globals.employess.json_array, table_attributes="id=\"info-table\" border=\"1\"")