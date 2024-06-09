from typing import List
from pydantic import BaseModel
from sqlalchemy import func, select
from Schema.denunciaFocoSchema import denunciaFocoSchema
from Config.db import engine
from fastapi import APIRouter, HTTPException, status, Response
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


# Definimos el esquema de respuesta para el conteo de focos por ubicacion
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

#hallar las denuncias que tiene una ubicacion 
@denunciaF.get("/api/denunciaF/{ubicacion_name}", response_model=List[denunciaFocoSchema])
async def obtenerFocosUbicacion(ubicacion_name: str):
    with engine.connect() as conn:
        query = select(denunciaFocoM).where(denunciaFocoM.c.ubicacion == ubicacion_name)
        result = conn.execute(query).fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="Ubicacion no encontrada")
        
        # Convertir el resultado en una lista de diccionarios
        ubicList = [dict(row._mapping) for row in result]
        return ubicList
        