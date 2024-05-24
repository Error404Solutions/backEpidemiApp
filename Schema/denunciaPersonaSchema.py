from pydantic import BaseModel
from typing import Optional

class denunciaPersonaSchema(BaseModel):
    idAutor: Optional[str]
    nombrePersonaContagiada: str
    apellidoPersonaContagiada: str
    sintomasPersonaContagiada: str
    ubicacionPersonaContagiada: str
    fechaDenuncia: str