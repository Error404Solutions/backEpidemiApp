from typing import List
from Schema.denunciaPersonaSchema import denunciaPersonaSchema
from Config.db import engine
from fastapi import APIRouter, status, Response
from Models.denunciaPersonaModel import denunciaPersonaM

denunciaP = APIRouter()

@denunciaP.post("/api/denunciaP", status_code=status.HTTP_201_CREATED)
async def createDenunciaP(dataDenunciaP: denunciaPersonaSchema):
    with engine.connect() as conn:
        nuevo = dataDenunciaP.dict()
        conn.execute(denunciaPersonaM.insert().values(nuevo))
        conn.commit()
    return Response(status_code=status.HTTP_201_CREATED)

@denunciaP.get("/api/denunciaPersona", response_model=List[denunciaPersonaSchema])
async def listarDenunciasP():
    with engine.connect() as conn:
        query = denunciaPersonaM.select()
        result = conn.execute(query).fetchall()
        
        #convirtiendo el resultado en una lista de diccionarios
        denunciaPList = [dict(row._asdict()) for row in result]
        return denunciaPList