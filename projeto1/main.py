from fastapi import FastAPI, HTTPException, status, Path
from fastapi.responses import JSONResponse
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

# Método GET
@app.get('/filmes')
async def get_filmes():
    return filmes

# Dando get para consumir o endpoint de um filme
@app.get('/filmes/{filme_id}')
async def get_filme(
    filme_id: int = Path(
    default=None, 
    title='ID do filme',
    description='Dever ser entre 1 e 2',
    gt = 0, lt = 3 )
    ):

    try:    
        filme = filmes[filme_id]
        return filme
    except:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail='Filme não encontrado'
                )
    
# Método POST
@app.post('/filmes', status_code=status.HTTP_201_CREATED)
async def post_filme(filme: Filme):
    next_id: int = len(filmes) + 1
    filmes[next_id] = filme
    del filme.id
    return filme

# Método PUT
@app.put('/filmes/{filme_id}')
async def put_filme(filme_id: int, filme: Filme):
    if filme_id in filmes:
        filmes[filme_id] = filme

        return filme
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Não exite um filme com id={filme_id}'
                )

# Método DELETE
@app.delete('/filmes/{filme_id}')
async def delete_filme(filme_id: int):
    if filme_id in filmes:
        del filmes[filme_id]
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Não exite um filme com id={filme_id}'
        )



if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)