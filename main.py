import uvicorn
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello_world():
    return {'Hello': 'world'}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f'blog with id {id}'}


if __name__ == "__main__":
    uvicorn.run('main:app', host="localhost", port=8000, log_level='info', reload=True)
