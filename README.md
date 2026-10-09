
# TaskFlow API

API REST para gerenciamento de tarefas, desenvolvida
com Python e FastAPI.

## Tecnologias

- Python
- FastAPI
- Pytest
- HTTPX

## Como executar

1. Crie e ative um ambiente virtual.
2. Instale as dependências:
   pip install -r requirements.txt
3. Execute:
   python -m uvicorn app.main:app --reload

## Documentação

http://127.0.0.1:8000/docs

## Testes

python -m pytest -v

## Funcionalidades atuais

- Rota de boas-vindas
- Health check
- Testes automatizados

## Próximas funcionalidades

- CRUD de tarefas
- Banco de dados PostgreSQL
- Autenticação JWT
