from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from Config.db import engine, metadata

denunciaPersonaM = Table(
    "denunciaPersona",metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("idAutor", String(10), nullable=True),
    Column("nombrePersonaContagiada", String(100), nullable=False),
    Column("apellidoPersonaContagiada", String(100), nullable=False),
    Column("sintomasPersonaContagiada", String(500), nullable=False),
    Column("ubicacionPersonaContagiada", String(100), nullable=False),
    Column("fechaDenuncia", String(10), nullable=False)
)

metadata.create_all(engine)