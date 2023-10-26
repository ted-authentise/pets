from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import sqlite3
from pydantic import BaseModel
import uvicorn

app = FastAPI()

connection = sqlite3.connect("pets.db", check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS pets
       (name text, breed text, type text, ranking real, image text);"""
)
cursor.execute("""CREATE UNIQUE INDEX IF NOT EXISTS idx_pet_name ON pets (name);""")

@app.get("/")
def get_root():
    html_content = """
    <html>
        <head>
            <title>Pets API</title>
        </head>
        <body>
            <h1> Pets API </h1>

            <h2> API Endpoints </h2>

            <h3>Create a Pet</h3>

            <code>
            PUT /pets
            </code>

            <p>Body<p>

            <code>
            {
            "name": string,
            "breed": string,
            "type": string,
            "image": string,
            "ranking": number,
            }
            </code>

            <h3>Get all pets of a type</h3>

            <code>
            GET /pets?type={type}
            </code>

            <h3>Get a pet by name </h3>

            <code>
            GET /pets/{name}
            </code>

            <h3> Delete a pet by name </h3>

            <code>
            DELETE /pets/{name}
            </code>

            <h3> Delete all pets of a type </h3>

            <code>
            DELETE /pets?type={type}
            </code>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

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
        "SELECT name, breed, type, image, ranking FROM pets WHERE name LIKE ?", [name]
    )
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
async def delete_by_name(name: str):
    cursor.execute("DELETE FROM pets WHERE name LIKE ?", [name])

    connection.commit()


def start():
    # pyright: ignore[reportUnknownMemberType]
    uvicorn.run(  # pyright: ignore[reportUnknownMemberType]
        "pets_api.main:app", host="0.0.0.0", port=8000, reload=True
    )
