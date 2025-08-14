from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": f"Item {item_id} updated to {item.name} with price {item.price}"}
