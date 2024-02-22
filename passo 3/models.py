# Modelos pydantic

# está explicado no passo 1!

from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    username: str
    email: str
    age: int = None
    

