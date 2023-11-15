
from peewee import Database


def db_recreate_table_list(table_list: tuple, db: Database) -> None:

    for model in table_list:
        try:
            db.drop_tables([model])
        except Exception:
            print(f'table not remove {model}')

        try:
            db.create_tables([model])
        except Exception:
            print(f'table not create {model}')


def db_tuncate_table_list(table_list: tuple) -> None:

    for table in table_list:
        try:
            table.truncate_table()
            print(f'table clean {table}')
        except Exception:
            print(f'f:db_tuncate_table_list -> table not clean {table}')
    print('')
