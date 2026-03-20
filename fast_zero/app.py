from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from sqlalchemy import select

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import (
    Message,
    UserDatabase,
    Userlist,
    Userpublic,
    Userschema,
)

app = FastAPI()


database = []


# Sut -system under test
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'ola mundo'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=Userpublic)
def create_user(user: Userschema):
    session = get_session()
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )
    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                HTTPStatus.CONFLICT, detail='Nome de usuário já existe'
            )
        elif db_user.email == user.email:
            raise HTTPException(
                HTTPStatus.CONFLICT, detail='Email já cadastrado'
            )
    db_user = User(
        username=user.username, email=user.email, password=user.password
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', status_code=HTTPStatus.OK, response_model=Userlist)
def read_users():
    return {'users': database}


@app.get('/users/{user_id}', response_model=Userpublic)
def read_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario não encontrado'
        )
    else:
        return database[user_id - 1]


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=Userpublic
)
def update_user(user_id: int, user: Userschema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario não encontrado'
        )
    else:
        user_with_id = UserDatabase(**user.model_dump(), id=user_id)
        database[user_id - 1] = user_with_id
        return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=Message
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario não encontrado'
        )
    else:
        database.pop(user_id - 1)
        return 'usuário deletado'
