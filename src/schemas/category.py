# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import fields, EXCLUDE, Schema

from lib.schema.req import ResDatetimeField, ObjectIdField
from random import randint


class UserView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    username = fields.Str(missing='Unnamed')
    avatar = fields.Str(missing='https://i.pravatar.cc/300')


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
    user = fields.Nested(UserView(), missing={
        "username": "Unnamed",
        "avatar": 'https://i.pravatar.cc/300'
    })


class PropsComponent(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    title = fields.Str(missing='')
    description = fields.Str(missing='')
    items = fields.List(fields.Nested(BlockView), missing=[])


class ComponentView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    _id = ObjectIdField()
    page = fields.Str(missing='/')
    code = fields.Str(missing='')
    type = fields.Str(missing='')
    order = fields.Int()
    route = fields.Str()
    props = fields.Nested(PropsComponent())


class ComponentsView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    components = fields.List(fields.Nested(ComponentView))
