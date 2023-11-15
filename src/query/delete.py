from config import DB
from models import ObjectDb


def delete_object() -> None:

    obj = ObjectDb.get_or_none(ObjectDb.id == 1)
    obj.delete_instance()

    obj_list = ObjectDb.delete().where(ObjectDb.id > 20)
    obj_list.execute()
