
from datetime import datetime
import sys
from peewee import PostgresqlDatabase, SqliteDatabase
from pathlib import Path


ABS_PATH = Path(__file__).parent.resolve()
APP_NAME = 'sqlalchemy cheatsheet'


# =====================================
# load config

try:

    if sys.version_info.major == 3 and sys.version_info.minor >= 11:

        import tomllib

        with open(f"{ABS_PATH}/config.toml", "rb") as f:
            config = tomllib.load(f)
    else:

        import toml

        with open(f"{ABS_PATH}/config.toml", "r") as f:
            config = toml.load(f)

    IND = config['utils']['console_indent']

    # sqlite
    DB = SqliteDatabase(f"{ABS_PATH}/{config['db_sqlite']['db_dir']}/{config['db_sqlite']['db_file']}")

    # psotgresql
    # DB = PostgresqlDatabase(
    #     config['db']['db_name'],
    #     user=config['db']['db_user'],
    #     password=config['db']['db_password'],
    #     host=config['db']['host'],
    #     port=int(config['db']['port']),
    #     autorollback=True
    # )

    print(f'{datetime.now()} start app: {APP_NAME}')
    # print(f'{IND} python {sys.version_info.major}.{sys.version_info.minor}')
    # print(f'{IND} config loaded: OK')

except Exception as e:
    raise Exception(f'config load -> error: {e}')
