#Passo 4!

# Esta Parte é a mesma presente no passo 1,
# seguimos com o passo 4 a partir da linha 40!

from fastapi import FastAPI, HTTPException
from models import Usuario

app = FastAPI()

database = {}

#POST

@app.post("/usuarios/")
async def criar_usuario(usuario: Usuario):
        
    if usuario.id in database:
        raise HTTPException(status_code=400, detail="O ID de usuário já existe")
    
    database[usuario.id] = usuario
    return {"message": "Usuário criado com sucesso", "usuario": usuario}

# GET

@app.get("/usuarios/")
async def ver_usuarios():
    return database

# GET BY ID

@app.get("/usuarios/{usuario_id}")
async def buscar_usuario(usuario_id: int):
    
    if usuario_id not in database:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return database[usuario_id]


# Passo 4!

# Aqui nós estamos criando um método DELETE, responsável por deletar algum item de nossa base de dados
# Assim como no 'GET BY ID' precisamos passar um id na nossa busca, isso especifica qual usuário queremos excluir!

@app.delete("/usuarios/{usuario_id}")
async def excluir_usuario(usuario_id: int):
    
    # Aqui nós verificamos se o usuário existe na nossa base de dados, caso não exista nós mostramos um erro, e caso exista deletamos o mesmo
    
    if usuario_id not in database:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    # Deletando da base de dados
    
    del database[usuario_id]
    
    return {"message": "Usuário excluído com sucesso"}


# Método UPDATE(put)

# Para fazer o update, nós também passamos um parametro na URL do método, sendo ele o id do usuário que desejamos atualizar
# porem, note que nos parametros da função, nós passamos um id e tambem um usuário completo

# este usuário completo que passamos é aonde estará os dados atualizados do nosso usuário

@app.put("/usuarios/{usuario_id}")
async def atualizar_usuario(usuario_id: int, usuario: Usuario):
    
    # Faz a verificação se caso o usuário existe, e se sim ele apenas substitui as informações antigas pelas novas!
    
    if usuario_id not in database:
        
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    database[usuario_id] = usuario
    
    return {"message": "Usuário atualizado com sucesso", "usuario": usuario}

# E agora sua API está pronta!!
