from fastapi import FastAPI

app = FastAPI()


# Sut -system under test
@app.get('/')
def read_root():
    return {'message: ': 'ola mundo'}
