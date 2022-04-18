# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from src.enums.obj import ObjType, MoreByItem
from src.enums.page import PageCode, BlockCode
from src.enums.route import ItemRoute, PageRoute
from src.models.event import EventModel
from src.models.sitemap import SitemapModel
from src.models.user import UserModel


class MetaService(object):

    @staticmethod
    def get_obj_by_id(obj_id, route):
        if f'/{route}' in [ItemRoute.VIDEO, ItemRoute.NFT, ItemRoute.SHORT, ItemRoute.MUSIC]:
            return EventModel.get_item(obj_id), ObjType.VIDEO
        if f'/{route}' in [ItemRoute.LIVE]:
            return EventModel.get_item(obj_id), ObjType.LIVE
        if f'/{route}' in [ItemRoute.CHANNEL]:
            return UserModel.get_item(obj_id), ObjType.CHANNEL
        return None, None

    @staticmethod
    def get_explore_all(explore):
        if f'/{explore}' in [PageRoute.TOP_NFT, PageRoute.TOP_MUSIC, PageRoute.TOP_VIDEO, PageRoute.TOP_SHORT]:
            return list(EventModel.get_random_items(size=20)), ObjType.VIDEO, ItemRoute.VIDEO
        if f'/{explore}' in [PageRoute.TOP_LIVE]:
            return list(EventModel.get_random_items(size=20)), ObjType.LIVE, ItemRoute.LIVE
        if f'/{explore}' in [PageRoute.CHANNELS]:
            return UserModel.get_random_items(size=20), ObjType.CHANNEL, ItemRoute.CHANNEL
        return list(EventModel.get_random_items(size=20)), ObjType.VIDEO, ItemRoute.VIDEO

    @staticmethod
    def get_more_by_item(obj_id: str, more_type: str, params):
        if more_type == MoreByItem.PLAY_MORE:
            return list(EventModel.get_random_items(size=params.page_size)), ObjType.VIDEO, ItemRoute.VIDEO
        if more_type == MoreByItem.RECOMMEND:
            return list(EventModel.get_random_items(size=params.page_size)), ObjType.VIDEO, ItemRoute.VIDEO
        return [], ObjType.VIDEO, ItemRoute.VIDEO

    @classmethod
    def get_page_explore(cls, page):
        _components = SitemapModel.get_explore(page_explore=page)
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

    @classmethod
    def get_components(cls, page: str = PageCode.HOME_PAGE):
        if page == PageCode.HOME_PAGE:
            _components = SitemapModel.get_mock()
        else:
            _components = SitemapModel.get_explore(page_explore=page)
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
