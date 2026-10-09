from fastapi import FastAPI

app = FastAPI(
    title = "taskflow API",
    description = "API REST para gerenciamento de tarefas",
    version = "0.1.0"
)

@app.get("/")
def home():
    return {"message": "Bem-vindo ao taskflow API!"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

