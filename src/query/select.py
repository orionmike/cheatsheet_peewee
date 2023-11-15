from datetime import datetime
from config import DB
from models import ObjectDb


def get_object() -> None:
    object = ObjectDb.get_or_none(ObjectDb.id == 1)
    object = ObjectDb.get(ObjectDb.id == 1)
    object = ObjectDb.get_by_id(ObjectDb.id == 1)
    object = ObjectDb.select().where(ObjectDb.id == 2).first()


def get_object_list() -> None:
    object_list = ObjectDb.select()
    object_list = ObjectDb.select().dicts()
    object_list = ObjectDb.select().where(ObjectDb.id > 1, ObjectDb.is_active == True)
    object_list = ObjectDb.select().where(ObjectDb.updated_at < datetime.utcnow())

    object_list = ObjectDb.select().where(
        (ObjectDb.id > 10) | (ObjectDb.is_active == True))
