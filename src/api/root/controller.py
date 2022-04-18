# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import lib
from lib.http.base import NotFound
from lib.redis_util import get_user_by_id
from lib.util import is_oid
from src.enums.obj import ObjType
from src.schemas.category import ComponentsView
from src.schemas.object import ObjectDetail, ExploreAll
from src.services.meta import MetaService


@lib.handle_res(login=False)
def debug():
    return {}


@lib.handle_res(login=False)
def health_check(*args, **kwargs):
    return {}


@lib.handle_res(login=False, res_schema=ComponentsView)
def get_page(explore='home', *args, **kwargs):
    _components = MetaService.get_components(explore)
    return {
        'components': _components
    }


@lib.handle_res(login=False, res_schema=ObjectDetail)
def get_obj_by_id(route, obj_id, *args, **kwargs):
    if not is_oid(obj_id):
        raise NotFound
    _result = {

    }
    _obj, _object_type = MetaService.get_obj_by_id(obj_id, route)
    if not _obj:
        raise NotFound
    _obj['_id'] = obj_id
    _obj['user'] = get_user_by_id(obj_id=_obj.get('author_id', ''))
    _result['object_type'] = _object_type
    _result['object'] = _obj
    return _result


@lib.handle_res(login=False, res_schema=ExploreAll)
def get_more_of_items(obj_id, more_type, params, *args, **kwargs):

    _items, _object_type, _item_route = MetaService.get_more_by_item(
        obj_id,
        more_type
    )

    return {
        'items': _items,
        'object_type': _object_type,
        'item_route': _item_route
    }
