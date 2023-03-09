from fastapi import FastAPI
import uvicorn

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

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True)