from pydantic import BaseModel
from typing import Optional

class notificationSchema(BaseModel):
    id: Optional[int]
    titulo: Optional[str]
    mensaje: str
    tipo: str