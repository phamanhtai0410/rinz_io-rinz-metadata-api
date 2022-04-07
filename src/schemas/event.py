# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import fields, EXCLUDE, Schema

from lib.schema.req import ResDatetimeField, ObjectIdField


class EventView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    _id = ObjectIdField(required=True)
    banner = fields.Str(missing='')
    title = fields.Str(missing='')
    description = fields.Str(missing='')
    public_address = fields.Str(required=True)
    created_time = ResDatetimeField()
