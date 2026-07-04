from fastapi import FastAPI, HTTPException
from pydantic import ConfigDict, Field, BaseModel, EmailStr
import uvicorn 

app = FastAPI()

Items = []

class ItemSchema(BaseModel):
    Item_Id: int = Field(ge=0)
    title: str = Field(min_length=4,max_length=20)
    price: int = Field(ge=1, le=50)
    category: str = Field(min_length=4, max_length=15) 
    email: EmailStr    

    model_config = ConfigDict(extra="forbid")

@app.post("/Create_Item",
          tags=["Items"],
          summary="Create items here")
def CreateItem(CreateItem:ItemSchema) -> dict:
    Items.append({
        "Item_Id": len(Items) + 1,
        "Title": CreateItem.title,
        "Price": CreateItem.price,
        "Category": CreateItem.category,
        "Email": CreateItem.email
    })
    return {
        "Message": "Your item has been added!",
        "Item": CreateItem
    }

@app.get("/Items",
         tags=["Items"],
         summary="Get all items if we have it")
def GetItems():
    return {
        "Message": "There all items",
        "Items": Items
    }

@app.get("/Items/{Item_Id}",
         tags=["Items"],
         summary="Get any item by Item-Id")
def GetItemById(ItemById: int) -> dict:
    for item in Items:
        if item["Item-Id"] == ItemById:
            return {
                "Message": "There ur item by id",
                "Item": item
            }
    raise HTTPException(status_code=404, detail=f"We cant found this item by this {ItemById} Item-Id")

@app.delete("/Delete_Items/{Item_Id}",
            tags=["Items"],
            summary="Delete items from store by Item-Id")
def DeleteItem(Item_Id: int) -> dict:
    Delete_Item = Items.pop(Item_Id - 1)
    return {
        "Message": f"Item with {Item_Id} id has been deleted",
        "Deleted content": Delete_Item
    }
@app.put("/Update_Item/{Item_Id}",
         tags=["Items"],
         summary="Update some data by id")
def UpdateItem(Item_Id: int, New_Item: ItemSchema) -> dict:
    index = Item_Id - 1 
    item_dict = New_Item.model_dump()
    item_dict["Item_Id"] = Item_Id
    Items[index] = item_dict    
    return {
        "Message": f"Item with {Item_Id} id has been updated",
        "Updated Content": Items[index]
    }


if __name__ == "__main__":
    uvicorn.run("first:app", reload=True) 