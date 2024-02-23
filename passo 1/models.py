# Passo 1 -  Criação dos Modelos/Models!

# Pydantic é uma biblioteca Python que fornece funcionalidades para validar dados de forma simples e eficiente,
# além de serialização e desserialização de dados em objetos Python.

# O objetivo principal do Pydantic é facilitar a validação e manipulação de dados em aplicativos Python,
# especialmente em aplicativos da web, onde a entrada de dados pode vir de diferentes fontes, 
# como solicitações HTTP, arquivos JSON, bancos de dados, etc.

# Utilizamos muito essa biblioteca juntamente com o FastAPI!

# A Classe 'BaseModel' que importamos de pydantic é usada como uma classe base para a criação de modelos de dados
# Ela tambem fornece funcionalidades  para validações de dados, serialização e desserialização

# No exemplo criaremos um Modelo de dados chamado 'Usuario'

from pydantic import BaseModel

# Aqui estamos criando o modelo 'Usuario' e definindo seus atributos, juntamente com o tipo de dado esperado!
# Especificamente no campo 'age' nós temos um tratamento opcional, onde se mostra que o tipo esperado é int
# e se caso nenhum valor for fornecido aquele usuario ficará com a idade 'None', basicamente um campo Opcional!

class Usuario(BaseModel):
    id: int
    username: str
    email: str
    age: int = None
    
# Siga para o arquivo 'main.py'!
