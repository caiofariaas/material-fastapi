# Modelos pydantic

from pydantic import BaseModel, validator

# o 'validator' é usado para validar alguma informação na hora da criação do seu 'Usuario'
# no exmeplo nós estamos usando ele para validar se a idade do usuario é maior que 0

class Usuario(BaseModel):
    id: int
    username: str
    email: str
    age: int = None
    
# nós passamos como parametro dele o campo que deseja verificar, no caso 'age'
# e criamos uma função de validação logo abaixo
# nós passamos 'cls' para se referir a propria classe em que ela se encontra
# e 'value' para representar o valor inserido no campo 'age' na hora de criar o usuário
    
    @validator('age')
    def idade_positiva(cls, value):
        
        # verificamos o valor e caso o valor for menor ou igual a 0 mostramos um ERRO.
    
        if value <= 0:
            raise ValueError("A Idade deve ser maior que 0")
        
        # se não, retornamos o valor e pronto!
        
        return value

# Faça o teste no Swagger! tente criar um usuário com uma idade igual ou menor a 0 usando o POST que criamos no primeiro passo!