from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class Userschema(BaseModel):
    username: str
    email: EmailStr
    password: str


class Userpublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserDatabase(Userschema):
    id: int


class Userlist(BaseModel):
    users: list[Userpublic]
