from pydantic import BaseModel, validator

class Usuario(BaseModel):
    id: int
    username: str
    email: str
    age: int = None
    
    @validator('age')
    def idade_positiva(cls, value):
        if value <= 0:
            raise ValueError("A Idade deve ser maior que 0")
        
        return value
