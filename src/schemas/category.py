# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from bson import ObjectId
from marshmallow import fields, EXCLUDE, Schema, pre_load

from lib.redis_util import get_user_by_id
from lib.schema.req import ResDatetimeField, ObjectIdField
from random import randint, choice

from src.enums.obj import ObjType
from src.models.stream import StreamModel
from src.schemas.stream import StreamVideo

default_banner = 'https://picsum.photos/400'


class UserView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    username = fields.Str(missing='Unnamed')
    avatar = fields.Str(missing='https://i.pravatar.cc/300')
    _id = ObjectIdField()


class ChannelView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    channel = fields.Str(missing='Unnamed', data_key='username')
    avatar = fields.Str(missing='https://i.pravatar.cc/300')
    followed = fields.Bool(missing=choice([True, False]))
    _id = ObjectIdField()


class VideoView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    _id = ObjectIdField(required=True)
    banner = fields.Str(
        missing=default_banner,
        allow_none=True)
    title = fields.Str(missing='')
    description = fields.Str(missing='')
    public_address = fields.Str(required=True)
    created_time = ResDatetimeField()

    total_view = fields.Int(missing=randint(5000, 60000))
    total_heart = fields.Int(missing=randint(5000, 60000))
    total_comment = fields.Int(missing=randint(15000, 60000))
    total_share = fields.Int(missing=randint(500, 6000))

    user = fields.Nested(UserView(), missing={})
    followed = fields.Bool(missing=choice([True, False]))

    stream = fields.Nested(StreamVideo)

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

    @pre_load
    def load_user(self, in_data, **kwargs):
        in_data['user'] = get_user_by_id(in_data.get('author_id', ''))
        return in_data


map_object = {
    ObjType.VIDEO: VideoView(),
    ObjType.LIVE: VideoView(),
    ObjType.SHORT_VIDEO: VideoView(),
    # ObjType.LIVE: VideoView(),

    ObjType.CHANNEL: ChannelView()
}


class PropsComponent(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    title = fields.Str(missing='')
    description = fields.Str(missing='')
    items = fields.List(fields.Dict(), missing=[])

    @pre_load
    def _load_items(self, in_data, **kwargs):
        if not in_data['obj_type'] in map_object:
            raise Exception
        _schema = map_object[in_data['obj_type']]
        _items = [_schema.load(x) for x in in_data['items']]
        in_data['items'] = _items
        return in_data


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
    item_route = fields.Str()
    more_items = fields.Str()


class ComponentsView(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    components = fields.List(fields.Nested(ComponentView))
