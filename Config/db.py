from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+mysqlconnector://admin:12345@localhost:3306/EPIDEMIAPP")

metadata = MetaData()