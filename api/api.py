from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

api = FastAPI(title='Template-Api', version='1.0.0')

@api.on_event('startup')
def startup():
    None

@api.on_event('shutdown')
def shutdown():
    None

@api.get('/get')
async def get():
    return JSONResponse(content='GET')

@api.post('/post')
async def post():
    return JSONResponse(content='POST')

@api.put('/put')
async def put():
    return JSONResponse(content='PUT')

@api.delete('/delete/{id}')
async def delete(id: int):
    return JSONResponse(content=id)