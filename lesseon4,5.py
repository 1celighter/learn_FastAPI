# pydantic with FastAPI

from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI
import uvicorn 

app = FastAPI()

data = {
    "email": "gkjrifm@gmail.com",
    "bio": "Something here",
    "age": 20
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=20)

    model_config = ConfigDict(extra="forbid")

users = []  

@app.post("/users",
          tags=["Users"],
          summary="there to create user")
def create_user(user:UserSchema):
    users.append(user)
    return {
        "Okay": True,
        "msg": "User has been added"
        }

@app.get("/users",
         tags=["Users"],
         summary="get all the users")
def get_users() -> list[UserSchema]: # я написал list[userschema] для более лучшего вида в документации мы этим передаем как должен в конечном итоге выглядить ответ красиво
    return users

if __name__ == "__main__":
    uvicorn.run("lesseon4,5:app", reload=True)
    