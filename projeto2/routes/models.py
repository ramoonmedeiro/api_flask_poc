from typing import Optional
from pydantic import BaseModel

class Filme(BaseModel):

    id: Optional[int] = None
    titulo: str 
    genero: str
    ano: int