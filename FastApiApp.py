
from fastapi import FastAPI,requests
from pydantic import BaseModel
import uvicorn
import logging
from MongoDB import DB

class Person(BaseModel):
    name:str
    age:int

db=[]
mDB=DB("test")
app=FastAPI()
@app.post("/add")
def insert(p:Person):
    db.append(p)
    mDB.get_table("test").insert_many([p.__dict__])
    return("Successfully Added user")

@app.get("/get")
def insert():
    data=mDB.get_table("test").find()
    res=[]
    for i in data:res.append([i["name"],i["age"]])
    return res

if(__name__== "__main__"):
    uvicorn.run("FastApiApp:app",host="0.0.0.0",port =5001)


