from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()
Attack_Items = [
    {
        "Attack_Item_ID": 1,
        "Weapon_Name": "Butterfly",
        "Weapon_Damage": 30
    },
    {
        "Attack_Item_ID": 2,
        "Weapon_Name": "Bloodthorn",
        "Weapon_Damage": 65
    }
]
@app.get("/get_item",
         tags=["Attack Items"],
         summary="There all attack items")
def get_items():
    return{
        "message": "There all Attack Items",
        "items": Attack_Items}

@app.get("/get_item/{Atk_Item}",
         tags=["Attack Items"],
         summary="The way to get a Atk Item as u wish")
def get_Atk_item(Item_id: int):
    for Atk_Item in Attack_Items:
        if Atk_Item["Attack_Item_ID"] == Item_id:
            return{
                "message": "This is ur req Attack item",
                "Item": Atk_Item
            }
    raise HTTPException(status_code=404, detail="That item for ur ID was deleted or not found")

class NewItem(BaseModel):
    Weapon_name: str
    Weapon_Damage: int

@app.post("/New_Item",
          tags=["Attack Items"],
          summary="Get ticket here to create your own item!")
def Create_Atk_Item(nAtk_Item: NewItem):
    Attack_Items.append({
        "Attack_Item_ID": len(Attack_Items) + 1,
        "Weapon_name": nAtk_Item.Weapon_name,
        "Weapon_Damage": nAtk_Item.Weapon_Damage 
    })
    return{
        "message": "There are your new attack item",
        "items": nAtk_Item
    }

if __name__ == "__main__":
    uvicorn.run("items:app", reload=True)