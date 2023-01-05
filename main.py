from pydantic import BaseModel
from fastapi import FastAPI

class User(BaseModel):
    name: str
    age: int
    email: str
    
    
Users = []

app = FastAPI(title="Sample RESTful API by FastAPI")

@app.post("/user")
def create_user(user: User):
    Users.append(user)
    return user


@app.get("/users")
def read_users():
    return Users

