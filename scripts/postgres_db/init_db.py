from scripts.postgres_db.db_models import Base, engine
from scripts.logging.log_module import logger as log


def initialize_db():
    """Creates all database tables if they don’t exist."""
    log.info("Initializing database...")
    Base.metadata.create_all(bind=engine)
    log.infp("Database and tables are ready!")
