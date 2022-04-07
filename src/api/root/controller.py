# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import lib
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
