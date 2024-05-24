from pydantic import BaseModel
from typing import Optional

class denunciaFocoSchema(BaseModel):
    idAutor: str
    descripcion: str
    ubicacion: str
    fechaDenuncia: str
    foto: str