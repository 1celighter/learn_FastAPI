from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

products = [
    {
        "id": 1,
        "name of product": "gilled",
        "type of product": "meat", 
    },
    {
        "id": 2, 
        "name of product": "banana split",
        "type of product": "organic",
    }
]

@app.get("/product",
    tags=["Магазин"],
    summary="Тип продуктов и их название"
)
def get_name():
    return products

@app.get("/products/{product_id}",
    tags=["Магазин"],
    summary="Получить конкретный товар в магазине"
)
def get_product(product_id: int):
    for product_item in products:
        if product_item["id"] == product_id:
            return {f"Вот ваш продукт {product_item}"}
    raise HTTPException(status_code=404, detail="этого продукта не наблюдается в этом магазине")
    
class NewProduct(BaseModel):
    name_of_product: str
    type_of_product: str

@app.post("/New_product",
        tags=["Магазин"],
        summary="Создать заявку на продукт")
def get_new_product(n_product:NewProduct):
    products.append({
        "id": len(products) + 1, 
        "name of product": n_product.name_of_product,
        "type of product": n_product.type_of_product
    })
    return{f"Ваша заявка на продукт под названием {n_product.name_of_product} успешно создан"}

if __name__ == "__main__":
    uvicorn.run("first:app", reload=True)