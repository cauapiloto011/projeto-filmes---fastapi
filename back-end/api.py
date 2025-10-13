from fastapi import FastAPI
import funcao


#rodar fastapi:
# python -m uvicorn api:app --reload

#Testar api FastApi
# /docs > Documentação Swagger
# /redoc > Docuentação redoc

#iniciar o fastapi
app = FastAPI(title="Gerenciador de filmes")


#GET = pegar / listar
#POST = Criar / Enviar
#PUT = Atualizar
#DELETE = Deletar

@app.get("/")
def home():
    return {"mensagem": "Quero café prof"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.inserir_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adicionado com sucesso!"}

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filme()
    lista = []
    for linha in filmes:
        lista.append({
            "id:" linha[0],
            "titulo": linha[1],
            "genero": linha[2],
            "ano": [3],
            "avaliacao": linha [4]
            })
    return {"filmes": lista}