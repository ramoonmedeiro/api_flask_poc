from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional, List
from fastapi.responses import JSONResponse
import uvicorn
from models import Filme


# iniciando app
app = FastAPI(
    title='API de Filmes',
    version='0.0.1',
    description='API de filmes para testes'
    )

filmes = {
    1: {
        'titulo': 'Interstellar',
        'genero': 'sci-fi',
        'ano': 2014
    },

    2:{
        'titulo': 'gladiador',
        'genero': 'ação',
        'ano': 2000
    }
}

# Método GET

@app.get('/filmes')
async def get_filmes():
    return filmes

@app.get('/filmes/{filme_id}')
async def get_filme(filme_id : int):
    try:
        return filmes[filme_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Filme não encontrado')
    
@app.post('/filmes')
#async def post_filme(filme: Optional[Filme] = None):
async def post_filme(filme: Filme):
    if filme.id not in filmes:
        next_id: int = len(filmes) + 1
        filmes[next_id] = filmes
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='ID já existe')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)