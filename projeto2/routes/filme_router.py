from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/filmes')
async def get_filmes():
    return {"info": "Retorna todos os filmes"}