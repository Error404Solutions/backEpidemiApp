from typing import List
from Schema.notificationSchema import notificationSchema
from Config.db import engine
from fastapi import APIRouter, HTTPException, status, Response
from Models.notificationModel import notificacionM

notificacion = APIRouter()

@notificacion.post("/api/notificacion", status_code=status.HTTP_201_CREATED)
async def createNotificacion(dataNotificacion: notificationSchema):
    with engine.connect() as conn:
        nuevo = dataNotificacion.dict()
        conn.execute(notificacionM.insert().values(nuevo))
        conn.commit()
    return Response(status_code=status.HTTP_201_CREATED)

@notificacion.get("/api/notificacion", response_model=List[notificationSchema])
async def listarNotificaciones():
    with engine.connect() as conn:
        query = notificacionM.select()
        result = conn.execute(query).fetchall()
        #Listar las notificaciones
        notificacionList = [dict(row._asdict()) for row in result]
        return notificacionList
    
@notificacion.get("/api/notificacion/{notificacion_id}", response_model=notificationSchema)
async def obtenerNotificacion(notificacion_id: int):
    with engine.connect() as conn:
        query = notificacionM.select().where(notificacionM.c.id == notificacion_id)
        result = conn.execute(query).fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="Notificación no encontrada")
        return dict(result._asdict())