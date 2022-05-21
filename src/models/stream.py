# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from pymodm import fields

from lib.model import BaseMG


class StreamModel(BaseMG):
    class Meta:
        collection_name = 'stream'
        final = True
        ignore_unknown_fields = True

    # _id = fields.ObjectIdField(primary_key=True)
    streams = fields.DictField(default={})
    live_event_id = fields.ObjectIdField()
