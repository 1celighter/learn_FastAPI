from fastapi import FastAPI
from pydantic import ConfigDict, Field, BaseModel, EmailStr
import uvicorn 

app = FastAPI()

Items = []

class ItemSchema(BaseModel):
    title: str = Field(min_length=4,max_length=20)
    price: int = Field(ge=0, le=50)
    category: str = Field(min_length=4, max_length=15) 
    email: EmailStr    

    model_config = ConfigDict(extra="forbid")

@app.post("/Create_Item",
          tags=["Items"],
          summary="Create items here")
def CreateItem(CreateItem:ItemSchema) -> dict:
    Items.append({
        "Title": CreateItem.title,
        "Price": CreateItem.price,
        "Category": CreateItem.category,
        "Email": CreateItem.email
    })
    return {
        "Message": "Your item has been added!",
        "Item": CreateItem
    }

@app.get("/Get_Items",
         tags=["Items"],
         summary="Get all items if we have it")
def GetItems():
    return {
        "Message": "There all items",
        "Items": Items
    }


if __name__ == "__main__":
    uvicorn.run("first:app", reload=True) 