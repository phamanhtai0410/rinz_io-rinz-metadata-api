# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import fields, EXCLUDE, Schema, pre_load
from pydash import get

from lib.redis_util import get_user_by_id
from lib.schema.req import ResDatetimeField, ObjectIdField
from random import randint

from src.enums.obj import ObjType

default_banner = 'https://s3-alpha-sig.figma.com/img/402b/7c6c/53824e64a9ae4cbe850f69d339e1d379?Expires=1651449600&Signature=gv5HshfnCMLIeP3BD8d0kMDzBd36MdomUpS2pGNVc8JuvLl9aWdEJsv0WXyIj3gceHArsJsD0j0NEswmh9XiIBxm4~nkPI5cfLNYjGWNu1wuUtsbXFA9mgL7dZMo1NAHC3tzo4OFnOdnX4pNoDp1AT6z7~xDD3N5eJJxFy40fa8iY4LydQis38984mDRs~2oQNo07Fl1xsFgKE25ba0~fzvH3YBxDPcvIvA-H-6CnOYoh8iA9k1tEeMF9Hpz~jnWaXZdanGoTaFNtXVVFep1FiWjTytMxlXYJlwK9TfxdQ9ynXhl~hLXd6K8Sz8xHBNdZ~2JGDTaJVY0WV6kHff7Uw__&Key-Pair-Id=APKAINTVSUGEWH5XD5UA'


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
    user = fields.Nested(UserView(), missing={})

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
