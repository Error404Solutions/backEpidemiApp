from fastapi import FastAPI
from Routers.denunciaFocoRouter import denunciaF
from Routers.denunciaPersonaRouter import denunciaP
from Routers.notificationRouter import notificacion
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return{"mesage": "Bienvenido al back"}

app.include_router(denunciaF)
app.include_router(denunciaP)
app.include_router(notificacion)