
from config import DB
from models import ObjectDb


def insert_object() -> None:
    with DB:
        object_1 = ObjectDb()
        object_1.name = "object_1"
        object_1.save()

        ObjectDb.create(
            name='object_1',
        )
