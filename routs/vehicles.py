from fastapi import APIRouter
from business_logic import globals
from models.vehicle import Vehicle
from typing import List

router = APIRouter()

@router.get("/vehicles",tags=["vehicle"])
async def get_all_vehicles() ->List[Vehicle]:
    return list(globals.vehicles.values())



@router.post("/vehicle",tags=["vehicle"])
async def add_new_vehicle(_vehicle : Vehicle):
    globals.vehicles[ _vehicle.Plate_id ]= _vehicle
    return {"message": " a new vehicle was added"}



