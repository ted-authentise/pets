from fastapi import FastAPI  
import sqlite3
from pydantic import BaseModel
app = FastAPI()   
    
connection = sqlite3.connect("pets.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS pets
               (name text, breed text, type text, ranking real, image text)''')

@app.get("/pets") 
async def get_by_type(type: str):     
  return {"search": type}

class Pet(BaseModel):
    name: str
    breed: str
    type: str
    image: str
    ranking: int

@app.put("/pets")
async def add_pet(pet: Pet):
  return pet

@app.delete("/pets")
async def delete_by_type(type: str):
  return {"type": type}

@app.delete("/pets/{name}")
async def delete_by_name(name):
  return {"name": name}
