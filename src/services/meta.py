# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from src.enums.page import PageCode, BlockCode
from src.models.event import EventModel
from src.models.sitemap import SitemapModel


class MetaService(object):

    @classmethod
    def get_categories(cls, page: str = PageCode.HOME_PAGE):
        _categories = SitemapModel.get_mock()
        return [
            {
                **x,
                "items": cls.get_top(x['code'])
            } for x in _categories
        ]

    @staticmethod
    def get_top(block):
        # if block in [BlockCode.TOP_NFT, BlockCode.TOP_VIDEO]:
        return list(EventModel.get_random_items(size=6))

        # return {
        #
        # }
