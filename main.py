from fastapi import FastAPI
from Routers.denunciaFocoRouter import denunciaF

app = FastAPI()

@app.get("/")
def read_root():
    return{"mesage": "Bienvenido al back"}

app.include_router(denunciaF)