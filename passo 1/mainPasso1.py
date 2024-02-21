# Aqui daremos continuidade á nossa API
# Lembrando que uma boa prática em FastAPI fazer a divisão dos arquivos, por exemplo
# criar um arquivo para os métodos/requisiçoes, um para os modelos e um para a sua base de dados por exemplo!

# FastAPI permite que você crie uma instancia de uma aplicação FastApi
# HTTPException é usado especificamente em FastAPI para  retornar respostas HTTP com códigos de status personalizados e mensagens de erro!

from fastapi import FastAPI, HTTPException
from passo1 import Usuario

# Esta instancia representa a nossa aplicação FastAPI, através dela que podemos criar todos os métodos e requisições!

app = FastAPI()

# Criamos um dicionário para ser utilizado como nosso Banco de Dados por enquanto!

database = {}

# Vamos iniciar a criação das requisições!
# @app.post indica que estamos criando um método POST
# Estamos recebendo como parametro uma variável 'usuario' do tipo "Usuario" que é o model que criamos!

@app.post("/usuarios/")
async def criar_usuario(usuario: Usuario):
    
    # Verifica se o ID já existe no dicionário
    
    if usuario.id in database:
        
            # Aqui caso esse usuário ja exista nós usamos o HTTPException para enviar uma mensagem de erro com o
            # Codigo 404 e no detalhe apenas mostramos essa informação

        raise HTTPException(status_code=400, detail="O ID de usuário já existe")
    
    # Adiciona o usuário à base de dados e retorna uma mensagem de sucesso!
    
    database[usuario.id] = usuario
    
    return {"message": "Usuário criado com sucesso", "usuario": usuario}

# Neste momento ja podemos executar o nosso código e ver como ele está rodando
# execute o codigo : 'uvicorn main:app --reload'

# * Caso a sua 'main' não esteja em um arquivo nomeado como 'main.py' altere o comando com o nome de seu arquivo!

# Siga para o passo 2!!