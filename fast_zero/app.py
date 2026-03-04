from http import HTTPStatus

import fastapi

from fast_zero.schemas import (
    Message,
    UserDatabase,
    Userlist,
    Userpublic,
    Userschema,
)

app = fastapi.FastAPI()


database = []


# Sut -system under test
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'ola mundo'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=Userpublic)
def create_user(user: Userschema):
    user_with_id = UserDatabase(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=Userlist)
def read_users():
    return {'users': database}
