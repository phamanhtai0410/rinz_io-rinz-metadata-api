# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from random import randint

from bson import ObjectId
from marshmallow import Schema, EXCLUDE, fields, pre_load
from pydash import get

from lib.redis_util import get_user_by_id
from lib.schema.req import ObjectIdField, ResDatetimeField
from src.enums.obj import ObjType
from src.enums.video import VideoType
from src.models.stream import StreamModel
from src.schemas.category import UserView, ChannelView, default_banner


class StreamVideo(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    video_id = fields.Str()
    playback_uri = fields.Str()
    duration = fields.Str()
    resolution = fields.Int()
    type = fields.Str(missing=VideoType.VOD)


class VideoSchema(Schema):
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
    user = fields.Nested(UserView(), missing={})
    stream = fields.Nested(StreamVideo)

    @pre_load
    def load_user(self, in_data, **kwargs):
        in_data['user'] = get_user_by_id(in_data.get('author_id', ''))
        return in_data

    @pre_load
    def _load_stream(self, in_data, **kwargs):
        _ref_id = in_data['_id']
        if 'banners' in in_data and in_data['banners'] and len(in_data['banners']) > 0:
            in_data['banner'] = get(in_data, 'banners[0].url', default=default_banner)  # in_data['banner'][0]['url']
        else:
            in_data[
                'banner'] = default_banner
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
    ObjType.CHANNEL: ChannelView()
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
