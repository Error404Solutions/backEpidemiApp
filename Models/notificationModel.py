from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from Config.db import engine, metadata

notificacionM = Table(
    "notificacion", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("titulo", String, nullable=True),
    Column("mensaje", String(300), nullable=False),
    Column("tipo", String(30), nullable=False)
)

metadata.create_all(engine)