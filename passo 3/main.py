#Passo 3!

# Esta Parte é a mesma presente no passo 1,
# seguimos com o passo 3 a partir da linha 24!

from fastapi import FastAPI, HTTPException
from models import Usuario

app = FastAPI()

database = {}


@app.post("/usuarios/")
async def criar_usuario(usuario: Usuario):
        
    if usuario.id in database:
        raise HTTPException(status_code=400, detail="O ID de usuário já existe")
    
    database[usuario.id] = usuario
    return {"message": "Usuário criado com sucesso", "usuario": usuario}


# Passo 3!

# Métodos GET 

# Aqui nós vamos fazer um método GET que será responsável 
# por nos retornar todas as informações salvas na nossa base de dados!

# @app.get indica que nós queremos fazer uma requisição GET

# no caso, como estamos trabalhando apenas com um dicionário,
# só precisamos retorna-lo!

@app.get("/usuarios/")
async def ver_usuarios():
    return database

# Agora iremos fazer um método GET novamente, porém, agora iremos fazer uma busca por ID!

# perceba que ao passar a rota, nós passamos tambem {usuario_id} como 'parametro'
# sendo ele o mesmo que passamos para a função!
# neste campo é onde nós iremos colocar o ID do usuário que desejamos encontrar

@app.get("/usuarios/{usuario_id}")
async def buscar_usuario(usuario_id: int):
    
    # Aqui nós basicamente verificamos se esse id existe na nossa base de dados
    # caso não exita nós retornamos um erro 404, e como detalhe 'Usuario não encontrado'
    
    if usuario_id not in database:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    # caso o id exista, nós retornamos este usuário!
    
    return database[usuario_id]
