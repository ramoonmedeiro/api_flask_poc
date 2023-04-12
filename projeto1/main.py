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

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)