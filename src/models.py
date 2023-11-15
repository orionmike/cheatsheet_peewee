

from datetime import datetime
from peewee import (
    Model,
    IntegerField,
    CharField,
    BooleanField,
    PrimaryKeyField,
    ForeignKeyField,
    DateTimeField
)

from config import DB


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    created_at = DateTimeField(default=datetime.utcnow())
    updated_at = DateTimeField(default=datetime.utcnow())

    class Meta:
        database = DB
        order_by = 'id'


class CategoryObjectDb(BaseModel):

    id_object = IntegerField(null=True)
    name = CharField(null=True)
    is_active = BooleanField(null=True, default=True)

    class Meta:
        db_table = 'category'


class TagObjectDb(BaseModel):

    id_object = IntegerField(null=True)
    name = CharField(null=True)
    is_active = BooleanField(null=True, default=True)

    class Meta:
        db_table = 'tag'


class ObjectDb(BaseModel):
    name = CharField(null=True)
    is_active = BooleanField(null=True, default=True)

    category = ForeignKeyField(CategoryObjectDb, backref='object', null=True)
    tags = ForeignKeyField(TagObjectDb, backref='object', null=True)

    class Meta:
        db_table = 'object'
