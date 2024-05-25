from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from Config.db import engine, metadata

denunciaFocoM = Table(
    "denunciaFoco",metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("idAutor", String, nullable=True),
    Column("descripcion", String(500), nullable=False),
    Column("ubicacion", String(100), nullable=False),
    Column("fechaDenuncia", String(10), nullable=False),
    Column("foto", String(100), nullable=False)
)

metadata.create_all(engine)