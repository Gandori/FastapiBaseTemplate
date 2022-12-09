from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

api = FastAPI(title='Template-Api', version='1.0.0')

@api.get('/')
async def index(request: Request):
    None

@api.on_event('startup')
def startup():
    None

@api.on_event('shutdown')
def shutdown():
    None

@api.get('/get')
async def get() -> JSONResponse:
    return JSONResponse({'Data': 'Get'})

@api.post('/post')
async def post() -> JSONResponse:
    return JSONResponse({'Data': 'Post'})

@api.put('/put')
async def put() -> JSONResponse:
    return JSONResponse({'Data': 'Put'})

@api.delete('/delete/{id}')
async def delete(id) -> JSONResponse:
    return JSONResponse({'ID': id})