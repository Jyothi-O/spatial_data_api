import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry

DB_NAME = "Testing"
DB_USER = "Test"
DB_PASSWORD = "test12345"
DB_HOST = "192.168.0.205"

def ensure_postgis():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    conn.autocommit = True
    cursor = conn.cursor()

    # Enable PostGIS extension
    cursor.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    cursor.close()
    conn.close()
    print("PostGIS extension enabled successfully!")

ensure_postgis()
# Define DATABASE_URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

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

print("Database and tables are ready!")
