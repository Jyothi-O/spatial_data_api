
import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry
from scripts.logging.log_module import logger as log
from scripts.api_details import app_configuration

DB_NAME = app_configuration.database_name
DB_USER = app_configuration.database_user
DB_PASSWORD = app_configuration.db_password
DB_HOST = app_configuration.postgres_host
DB_PORT = app_configuration.postgres_port


def ensure_postgis():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    conn.autocommit = True
    cursor = conn.cursor()

    # Enable PostGIS extension
    cursor.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    cursor.close()
    conn.close()
    log("PostGIS extension enabled successfully!")


ensure_postgis()
# Define DATABASE_URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create Engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Define Tables
class Point(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(Geometry("POINT"))


class Polygon(Base):
    __tablename__ = "polygons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    geometry = Column(Geometry("POLYGON"))


# Create Tables in the Database
Base.metadata.create_all(bind=engine)
log.info("Database and tables are ready!")
