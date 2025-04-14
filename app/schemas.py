from pydantic import BaseModel ,EmailStr

class User(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr