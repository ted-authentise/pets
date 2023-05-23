from fastapi import FastAPI, HTTPException
import sqlite3
from pydantic import BaseModel

app = FastAPI()

connection = sqlite3.connect("pets.db", check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS pets
       (name text, breed text, type text, ranking real, image text);"""
)
cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_pet_name ON pets (name);""")


@app.get("/pets")
async def get_by_type(type: str):
    cursor.execute(
        "SELECT name, breed, type, image, ranking FROM pets WHERE type LIKE ? ORDER BY ranking DESC",
        [type],
    )
    rows = cursor.fetchall()
    return {"pets": rows}


@app.get("/pets/{name}")
async def get_by_name(name: str):
    cursor.execute(
        "SELECT name, breed, type, image, ranking FROM pets WHERE name LIKE ?"
    , [name])
    pet = cursor.fetchone()
    if pet is None:
      raise HTTPException(status_code=404, detail="Pet not found")
    return pet


class Pet(BaseModel):
    name: str
    breed: str
    type: str
    image: str
    ranking: int


@app.put("/pets", status_code=201)
async def add_pet(pet: Pet):
    values = (pet.name, pet.breed, pet.type, pet.image, pet.ranking)
    try:
        cursor.execute(
            "INSERT INTO pets (name, breed, type, image, ranking) VALUES(?, ?, ?, ?, ?);",
            values,
        )
        connection.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Pet with this name already exists")
    return pet


@app.delete("/pets", status_code=200)
async def delete_by_type(type: str):
    cursor.execute("DELETE FROM pets WHERE type LIKE ?", [type])
    connection.commit()
    rows = cursor.rowcount
    return {"rows_affected": rows}


@app.delete("/pets/{name}", status_code=204)
async def delete_by_name(name):
    cursor.execute("DELETE FROM pets WHERE name LIKE ?", [name])

    connection.commit()

