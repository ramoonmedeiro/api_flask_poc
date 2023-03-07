from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return {'msg': 'Minha primeira API'}