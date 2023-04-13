from fastapi import FastAPI
from routes import filme_router, usuario_router

app = FastAPI()

app.include_router(filme_router.router, tags=['filmes'])
app.include_router(usuario_router.router, tags=['usuários'])

if __name__ == '__main__':
    import uvicorn 
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)