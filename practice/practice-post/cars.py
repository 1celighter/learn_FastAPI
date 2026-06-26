from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

cars = [
    {
        "Car-ID": 1,
        "Name": "Corvet",
        "Max speed": 200
    },
    {
        "Car-ID": 2,
        "Name": "Nissan",
        "Max speed": 240
    }
]
@app.get("/cars",
         tags=["Cars"],
         summary="get all cars in list")
def get_all_cars():
    return{
        "Message": "There a list with all our carts",
        "List": cars
    }

@app.get("/cars/{car_id}",
         tags=["Cars"],
         summary="Choice a one car")
def get_one_car(car_id: int):
    for car in cars:
        if car["Car-ID"] == car_id:
            return {
                "message": "there are ur car u was choiced by car-id",
                "Your car": car
            }
    raise HTTPException(status_code=404, detail="This car has not found maybe u did mistake with choising")
    
class NewCar(BaseModel):
    CarName: str
    CarMaxSpeed: int

@app.post("/CreateCar",
          tags=["Cars"],
          summary="There u can create your own car if u want!")
def CreateNewCar(NCar: NewCar):
    cars.append({
        "Car-ID": len(cars) + 1,
        "Name": NCar.CarName,
        "Max speed": NCar.CarMaxSpeed
    })
    return {
        "Message": "There ur new created car also here all car specs",
        "car": NCar
    }

if __name__ == "__main__":
    uvicorn.run("cars:app", reload=True)
