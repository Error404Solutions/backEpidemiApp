from fastapi import FastAPI
from Routers.denunciaFocoRouter import denunciaF
from Routers.denunciaPersonaRouter import denunciaP

app = FastAPI()

@app.get("/")
def read_root():
    return{"mesage": "Bienvenido al back"}

app.include_router(denunciaF)
app.include_router(denunciaP)