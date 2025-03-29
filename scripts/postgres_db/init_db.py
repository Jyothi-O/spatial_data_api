from scripts.postgres_db.db_models import Base, engine

def initialize_db():
    """Creates all database tables if they don’t exist."""
    print("✅ Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database and tables are ready!")