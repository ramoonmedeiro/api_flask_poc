from fastapi import FastAPI, HTTPException, status
import uvicorn
from models import Filme


# iniciando app
app = FastAPI()

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

# Criando rota=filmes
@app.get('/filmes')
async def get_filmes():
    return filmes

# Dando get para consumir o endpoint de um filme
@app.get('/filmes/{filme_id}')
async def get_filme(filme_id: int):
    try:    
        filme = filmes[filme_id]
        return filme
    except:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail='Filme não encontrado'
                )
    

@app.post('/filmes', status_code=status.HTTP_201_CREATED)
async def post_filme(filme: Filme):
    next_id: int = len(filmes) + 1
    filmes[next_id] = filme
    del filme.id
    return filme



if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)