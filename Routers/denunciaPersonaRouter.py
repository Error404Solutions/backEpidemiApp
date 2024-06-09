from typing import List
from pydantic import BaseModel
from sqlalchemy import func, select
from Schema.denunciaPersonaSchema import denunciaPersonaSchema
from Config.db import engine
from fastapi import APIRouter, HTTPException, status, Response
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
    
    
# Definimos el esquema de respuesta para el conteo de casos potenciales por ubicacion
class DenunciaPotencialCountSchema(BaseModel):
    ubicacion: str
    count: int

@denunciaP.get("/api/denunciaPotencialUbicacion", response_model=List[DenunciaPotencialCountSchema])
async def listarDenunciasPoUbic():
    with engine.connect() as conn:
        # Realizar la consulta con GROUP BY y COUNT
        query = (
            select(denunciaPersonaM.c.ubicacionPersonaContagiada, func.count(denunciaPersonaM.c.ubicacionPersonaContagiada).label('count'))
            .group_by(denunciaPersonaM.c.ubicacionPersonaContagiada)
        )
        result = conn.execute(query).fetchall()
        
        # Convirtiendo el resultado en una lista de diccionarios
        denunciaFList = [{"ubicacion": row[0], "count": row[1]} for row in result]
        return denunciaFList
    
    
#hallar las denuncias que tiene una ubicacion 
@denunciaP.get("/api/denunciaPersona/{ubicacion_name}", response_model=List[denunciaPersonaSchema])
async def obtenerDenunciaPersonasUbicacion(ubicacion_name: str):
    with engine.connect() as conn:
        query = select(denunciaPersonaM).where(denunciaPersonaM.c.ubicacionPersonaContagiada == ubicacion_name)
        result = conn.execute(query).fetchall()
        if not result:
            raise HTTPException(status_code=404, detail="Ubicacion no encontrada")
        
        # Convertir el resultado en una lista de diccionarios
        ubicList = [dict(row._mapping) for row in result]
        return ubicList