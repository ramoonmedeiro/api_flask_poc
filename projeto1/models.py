from typing import Optional
from pydantic import BaseModel

class Filmes(BaseModel):

    id: Optional[int] = None
    titulo: str 
    genero: str
    ano: int

