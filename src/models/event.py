# -*- coding: utf-8 -*-
"""
   Description: 
        -
        -
"""
from lib.model import BaseMG
from pymodm import fields


class EventModel(BaseMG):
    class Meta:
        collection_name = 'event'
        final = True
        ignore_unknown_fields = True

    _id = fields.ObjectIdField(primary_key=True)
    public_address = fields.CharField(default='', blank=True)
    status = fields.CharField()
    description = fields.CharField()
    title = fields.CharField()
    banner = fields.CharField()
    created_time = fields.DateTimeField()
    author_id = fields.CharField(default='', blank=True)