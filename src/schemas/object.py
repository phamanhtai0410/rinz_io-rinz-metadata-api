# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from random import randint, choice

from bson import ObjectId
from marshmallow import Schema, EXCLUDE, fields, pre_load
from pydash import get

from lib.redis_util import get_user_by_id
from lib.schema.req import ObjectIdField, ResDatetimeField
from src.enums.obj import ObjType
from src.enums.video import VideoType
from src.models.stream import StreamModel
from src.schemas.category import UserView, ChannelView, default_banner
from src.schemas.stream import StreamVideo


class VideoSchema(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    _id = ObjectIdField()
    banner = fields.Str(missing=default_banner, allow_none=True)
    title = fields.Str(missing='')
    description = fields.Str(missing='')
    stream = fields.Nested(StreamVideo)

    public_address = fields.Str(required=True)

    created_time = ResDatetimeField()
    user = fields.Nested(UserView(), missing={})
    followed = fields.Bool(missing=choice([True, False]))

    total_view = fields.Int(missing=randint(5000, 60000))
    total_heart = fields.Int(missing=randint(5000, 60000))
    total_comment = fields.Int(missing=randint(15000, 60000))
    total_share = fields.Int(missing=randint(500, 6000))

    @pre_load
    def load_user(self, in_data, **kwargs):
        in_data['user'] = get_user_by_id(in_data.get('author_id', ''))
        return in_data

    @pre_load
    def _load_stream(self, in_data, **kwargs):
        _ref_id = in_data['_id']
        if isinstance(_ref_id, str):
            _ref_id = ObjectId(_ref_id)

        stream = StreamModel.db().find_one(
            {
                'live_event_id': _ref_id
            }
        )
        if stream:
            in_data['stream'] = stream.get('streams')
        else:
            in_data['stream'] = {}
        return in_data


map_object = {
    ObjType.VIDEO: VideoSchema(),
    ObjType.LIVE: VideoSchema(),
    ObjType.CHANNEL: ChannelView(),
    ObjType.SHORT_VIDEO: VideoSchema()
}


class ObjectDetail(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    object = fields.Dict()
    object_type = fields.Str(required=True)

    @pre_load
    def _load_object(self, in_data, **kwargs):
        if not in_data['object_type'] in map_object:
            raise Exception

        _obj = map_object[in_data['object_type']].load(in_data['object'])
        in_data['object'] = _obj
        return in_data


class FormLoadMore(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    page = fields.Int(missing=1, allow_none=True)
    page_size = fields.Int(missing=20, allow_none=True)


class ExploreAll(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    items = fields.List(fields.Dict(), missing=[])
    object_type = fields.Str(required=True)
    item_route = fields.Str()

    @pre_load
    def _load_object(self, in_data, **kwargs):
        if not in_data['object_type'] in map_object:
            raise Exception
        _schema = map_object[in_data['object_type']]
        _items = [_schema.load(x) for x in in_data['items']]
        in_data['items'] = _items
        return in_data
