from pydantic import BaseModel
from typing import Optional

class denunciaFocoSchema(BaseModel):
    idAutor: Optional[str]
    descripcion: str
    ubicacion: str
    fechaDenuncia: str
    foto: str