# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import lib


@lib.handle_res(login=False)
def get_more_by_item(obj_type: str, *args, **kwargs):
    return {
        'object_type': '',
        'items': [],
        'item_route': ''
    }
