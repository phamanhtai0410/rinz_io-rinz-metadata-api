# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from lib.model import BaseMG
from pymodm import fields

from src.enums.page import PageCode, ComponentCode, BlockCode
from src.enums.route import PageRoute, ItemRoute

mockup = [
    {
        "page": PageCode.HOME_PAGE,
        "code": BlockCode.TOP_NFT,
        "order": 1,
        "props": {
            "title": "",
            "description": ""
        },
        "type": ComponentCode.VIDEO_BANNER,
        "route": PageRoute.TOP_NFT,
        "item_route": ItemRoute.NFT
    },
    {
        "page": PageCode.HOME_PAGE,
        "code": BlockCode.TOP_MUSIC,
        "order": 2,
        "props": {
            "title": "Top Music",
            "description": ""
        },
        "type": ComponentCode.VIDEO_SHORT,
        "route": PageRoute.TOP_MUSIC,
        "item_route": ItemRoute.MUSIC
    },
    {
        "page": PageCode.HOME_PAGE,
        "code": BlockCode.TOP_LIVE,
        "order": 3,
        "props": {"title": "Top Live",
                  "description": ""},
        "type": ComponentCode.VIDEO_BANNER,
        "route": PageRoute.TOP_LIVE,
        "item_route": ItemRoute.LIVE
    },
    {
        "page": PageCode.HOME_PAGE,
        "code": BlockCode.TOP_VIDEO,
        "order": 4,
        "props": {"title": "Top Videos",
                  "description": ""},
        "type": ComponentCode.VIDEO_SLIDER,
        "route": PageRoute.TOP_VIDEO,
        "item_route": ItemRoute.VIDEO
    },
    {
        "page": PageCode.HOME_PAGE,
        "code": BlockCode.TOP_SHORT,
        "order": 5,
        "props": {
            "title": "Top Shorts",
            "description": ""
        },
        "type": ComponentCode.VIDEO_SHORT,
        "route": PageRoute.TOP_SHORT,
        "item_route": ItemRoute.SHORT
    }
]


class SitemapModel(BaseMG):
    class Meta:
        collection_name = 'sitemaps'
        final = True
        ignore_unknown_fields = True

    # _id = fields.ObjectIdField(primary_key=True)
    page = fields.CharField(default='')
    code = fields.CharField(default='')
    title = fields.CharField(default='')
    description = fields.CharField(default='')
    type = fields.CharField(default='')
    route = fields.CharField()
    order = fields.IntegerField()

    @staticmethod
    def get_mock():
        return mockup
