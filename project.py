from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

inventory = {}
item_id_counter = 1


class Item(BaseModel):
    name: str
    quantity: int
    price: float
    description: Optional[str] = None


@app.get("/")
def root():
    return {"message": "Inventory Manager API"}


@app.get("/items")
def get_all_items():
    return {"items": inventory}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory[item_id]


@app.post("/items")
def create_item(item: Item):
    global item_id_counter
    inventory[item_id_counter] = item.dict()
    item_id = item_id_counter
    item_id_counter += 1
    return {"id": item_id, "item": inventory[item_id]}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    inventory[item_id] = item.dict()
    return {"id": item_id, "item": inventory[item_id]}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = inventory.pop(item_id)
    return {"message": "Item deleted", "item": deleted_item}
