from typing import List
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import sessionmaker
from Schema.denunciaFocoSchema import denunciaFocoSchema
from Config.db import engine
from fastapi import APIRouter, status, Response
from Models.denunciaFocoModel import denunciaFocoM




denunciaF = APIRouter()

@denunciaF.post("/api/denunciaF", status_code=status.HTTP_201_CREATED)
async def createDenunciaF(dataDenunciaF: denunciaFocoSchema):
    with engine.connect() as conn:
        nuevo = dataDenunciaF.dict()
        conn.execute(denunciaFocoM.insert().values(nuevo))
        conn.commit()
    return Response(status_code=status.HTTP_201_CREATED)

@denunciaF.get("/api/denunciaFoco", response_model=List[denunciaFocoSchema])
async def listarDenunciasF():
    with engine.connect() as conn:
        query = denunciaFocoM.select()
        result = conn.execute(query).fetchall()
        
        #convirtiendo el resultado en una lista de diccionarios
        denunciaFList = [dict(row._asdict()) for row in result]
        return denunciaFList


# Definimos el esquema de respuesta
class DenunciaFocoCountSchema(BaseModel):
    ubicacion: str
    count: int

@denunciaF.get("/api/denunciaFocoUbicacion", response_model=List[DenunciaFocoCountSchema])
async def listarDenunciasUbic():
    with engine.connect() as conn:
        # Realizar la consulta con GROUP BY y COUNT
        query = (
            select(denunciaFocoM.c.ubicacion, func.count(denunciaFocoM.c.ubicacion).label('count'))
            .group_by(denunciaFocoM.c.ubicacion)
        )
        result = conn.execute(query).fetchall()
        
        # Convirtiendo el resultado en una lista de diccionarios
        denunciaFList = [{"ubicacion": row[0], "count": row[1]} for row in result]
        return denunciaFList

