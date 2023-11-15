

# from database import Base, recreate_table_list, sync_engine
from config import DB
from database import db_recreate_table_list
from models import ObjectDb, TagObjectDb, CategoryObjectDb

if __name__ == '__main__':
    db_recreate_table_list((ObjectDb, TagObjectDb, CategoryObjectDb), DB)
