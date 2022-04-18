# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from src.enums.obj import ObjType
from src.enums.page import PageCode, BlockCode
from src.models.event import EventModel
from src.models.sitemap import SitemapModel
from src.models.user import UserModel


class MetaService(object):

    @staticmethod
    def get_obj_by_id(obj_id):
        return EventModel.get_item(obj_id)

    @classmethod
    def get_components(cls, page: str = PageCode.HOME_PAGE):
        _components = SitemapModel.get_mock()
        return [
            {
                **x,
                "props": {
                    **x["props"],
                    "items": cls.get_top(x['code']) if x['obj_type'] != ObjType.CHANNEL
                    else cls.get_channels(x['code']),
                    "obj_type": x.get('obj_type')
                }
            } for x in _components
        ]

    @staticmethod
    def get_top(block):
        # if block in [BlockCode.TOP_NFT, BlockCode.TOP_VIDEO]:
        return list(EventModel.get_random_items(size=6))

        # return {
        #
        # }

    @staticmethod
    def get_channels(block):
        return list(UserModel.get_random_items(size=6))
