# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import fields, EXCLUDE, Schema

from lib.schema.req import ResDatetimeField, ObjectIdField
from random import randint


class BlockView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    _id = ObjectIdField(required=True)
    banner = fields.Str(missing='')
    title = fields.Str(missing='')
    description = fields.Str(missing='')
    public_address = fields.Str(required=True)
    created_time = ResDatetimeField()
    total_view = fields.Int(missing=randint(5000, 60000))


class CategoryView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    _id = ObjectIdField()
    page = fields.Str(missing='/')
    code = fields.Str(missing='')
    title = fields.Str(missing='')
    description = fields.Str(missing='')
    type = fields.Str(missing='')
    route = fields.Str()
    order = fields.Int()
    items = fields.List(fields.Nested(BlockView), missing=[])


class Categories(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    categories = fields.List(fields.Nested(CategoryView))
