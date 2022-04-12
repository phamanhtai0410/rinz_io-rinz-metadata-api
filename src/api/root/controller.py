# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import lib
from lib.http.base import NotFound
from lib.util import is_oid
from src.schemas.category import ComponentsView
from src.services.meta import MetaService


@lib.handle_res(login=False)
def debug():
    return {}


@lib.handle_res(login=False)
def health_check(*args, **kwargs):
    return {}


@lib.handle_res(login=False, res_schema=ComponentsView)
def get_home_page(*args, **kwargs):
    _components = MetaService.get_components("home")
    return {
        'components': _components
    }


@lib.handle_res(login=False)
def get_obj_by_id(route, obj_id, *args, **kwargs):
    if not is_oid(obj_id):
        raise NotFound

    _obj = MetaService.get_obj_by_id(obj_id)
    if _obj:
        _obj['_id'] = obj_id
    return _obj
