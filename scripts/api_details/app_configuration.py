import configparser

__config = configparser.ConfigParser(interpolation=None)
__config.read("conf/application.conf")

LOG_BASE_PATH = __config.get("LOG", 'base_path')
LOG_LEVEL = __config.get("LOG", 'level')
FILE_BACKUP_COUNT = __config.get("LOG", 'file_backup_count')
FILE_NAME = __config.get("LOG", 'file_name')
FILE_BACKUP_SIZE = __config.get("LOG", 'file_size_mb')
LOG_HANDLERS = __config.get("LOG", 'handlers')
enable_traceback = __config.get("LOG", 'enable_traceback')

postgres_host = __config.get("Database", 'postgres_host')
postgres_port = __config.get("Database", 'postgres_port')
database_name = __config.get("Database", 'database_name')
database_user = __config.get("Database", 'database_user')
db_password = __config.get("Database", 'db_password')


