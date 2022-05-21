# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from lib.model import BaseMG
from pymodm import fields

from src.enums.obj import ObjType
from src.enums.page import PageCode, ComponentCode, BlockCode
from src.enums.route import PageRoute, ItemRoute

mockup_home = [
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
        "item_route": ItemRoute.NFT,
        'obj_type': ObjType.VIDEO
    },
    # {
    #     "page": PageCode.HOME_PAGE,
    #     "code": BlockCode.TOP_MUSIC,
    #     "order": 2,
    #     "props": {
    #         "title": "Top Music",
    #         "description": ""
    #     },
    #     "type": ComponentCode.VIDEO_SHORT,
    #     "route": PageRoute.TOP_MUSIC,
    #     "item_route": ItemRoute.MUSIC,
    #     'obj_type': ObjType.VIDEO
    # },
    {
        "page": PageCode.HOME_PAGE,
        "code": BlockCode.TOP_LIVE,
        "order": 3,
        "props": {"title": "Top Live",
                  "description": ""},
        "type": ComponentCode.VIDEO_BANNER,
        "route": PageRoute.TOP_LIVE,
        "item_route": ItemRoute.LIVE,
        'obj_type': ObjType.VIDEO
    },
    {
        "page": PageCode.HOME_PAGE,
        "code": BlockCode.TOP_VIDEO,
        "order": 4,
        "props": {"title": "Top Videos",
                  "description": ""},
        "type": ComponentCode.VIDEO_SLIDER,
        "route": PageRoute.TOP_VIDEO,
        "item_route": ItemRoute.VIDEO,
        'obj_type': ObjType.VIDEO
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
        "item_route": ItemRoute.SHORT,
        'obj_type': ObjType.VIDEO
    },
    {
        "page": PageCode.HOME_PAGE,
        "code": BlockCode.POPULAR_CHANNEL,
        "order": 6,
        "props": {
            "title": "Popular Channel",
            "description": ""
        },
        "type": ComponentCode.CHANNELS,
        "route": PageRoute.CHANNELS,
        "item_route": ItemRoute.CHANNEL,
        'obj_type': ObjType.CHANNEL
    }
]

mockup_explore_live = [
    {
        "page": PageCode.EXPLORE_LIVE,
        "code": BlockCode.LIVE_PAGE_BANNER_VIDEOS,
        "order": 1,
        "props": {
            "title": "",
            "description": ""
        },
        "type": ComponentCode.VIDEO_BANNER,
        "item_route": ItemRoute.LIVE,
        'obj_type': ObjType.LIVE,
        'route': PageRoute.LIVE
    },
    {
        "page": PageCode.EXPLORE_LIVE,
        "code": BlockCode.LIVE_PAGE_SHORT_VIDEOS,
        "order": 2,
        "props": {
            "title": "Title",
            "description": ""
        },
        "type": ComponentCode.VIDEO_SHORT,
        'route': PageRoute.LIVE,
        "item_route": ItemRoute.SHORT,
        'obj_type': ObjType.VIDEO
    },
    {
        "page": PageCode.EXPLORE_LIVE,
        "code": BlockCode.LIVE_PAGE_SLIDER_VIDEOS,
        "order": 3,
        "props": {"title": "Title",
                  "description": ""},
        "type": ComponentCode.VIDEO_SLIDER,
        'route': PageRoute.LIVE,
        "item_route": ItemRoute.VIDEO,
        'obj_type': ObjType.VIDEO
    },
    {
        "page": PageCode.EXPLORE_LIVE,
        "code": BlockCode.LIVE_PAGE_USER_SHORT_VIDEOS,
        "order": 4,
        "props": {"title": "Category for you",
                  "description": ""},
        "type": ComponentCode.VIDEO_SHORT,
        'route': PageRoute.LIVE,
        "item_route": ItemRoute.SHORT,
        'obj_type': ObjType.VIDEO
    },
    {
        "page": PageCode.EXPLORE_LIVE,
        "code": BlockCode.LIVE_PAGE_POPULAR_CHANNELS_WITH_FOLLOW,
        "order": 5,
        "props": {
            "title": "Popular channels",
            "description": ""
        },
        "type": ComponentCode.CHANNELS_WITH_FOLLOW,
        'route': PageRoute.LIVE,
        "item_route": ItemRoute.CHANNEL,
        'obj_type': ObjType.CHANNEL
    },
    {
        "page": PageCode.EXPLORE_LIVE,
        "code": BlockCode.LIVE_PAGE_RECOMMEND_SLIDER_VIDEOS,
        "order": 6,
        "props": {
            "title": "Recommend for you",
            "description": ""
        },
        "type": ComponentCode.VIDEO_SLIDER,
        'route': PageRoute.LIVE,
        "item_route": ItemRoute.VIDEO,
        'obj_type': ObjType.VIDEO
    }
]

mockup_explore_short = [
    {
        "page": PageCode.EXPLORE_SHORT,
        "code": BlockCode.LIVE_PAGE_BANNER_VIDEOS,
        "order": 1,
        "props": {
            "title": "",
            "description": "",
            "items": []  # init items
        },
        "type": ComponentCode.SHORT_VERTICAL,
        "item_route": ItemRoute.SHORT,
        'obj_type': ObjType.SHORT_VIDEO,
        "route": PageRoute.SHORTS  # for load more items with page and page size
    }
]
mockup_explore_music = [
    {
        "page": PageCode.EXPLORE_MUSIC,
        "code": BlockCode.MUSIC_PAGE_BEST,
        "order": 1,
        "props": {
            "title": "Best New Songs",
            "description": "",
            "items": []  # init items
        },
        "type": ComponentCode.VIDEO_SHORT,
        "item_route": ItemRoute.SHORT,
        'obj_type': ObjType.SHORT_VIDEO,
        "route": PageRoute.SHORTS  # for load more items with page and page size
    },
    {
        "page": PageCode.EXPLORE_MUSIC,
        "code": BlockCode.MUSIC_PAGE_BEST,
        "order": 2,
        "props": {
            "title": "TOP TRENDING",
            "description": "",
            "items": []  # init items
        },
        "type": ComponentCode.VIDEO_SHORT,
        "item_route": ItemRoute.SHORT,
        'obj_type': ObjType.SHORT_VIDEO,
        "route": PageRoute.SHORTS  # for load more items with page and page size
    },
    {
        "page": PageCode.EXPLORE_MUSIC,
        "code": BlockCode.POPULAR_CHANNEL,
        "order": 3,
        "props": {
            "title": "Vietnam",
            "description": ""
        },
        "type": ComponentCode.CHANNELS,
        "route": PageRoute.CHANNELS,
        "item_route": ItemRoute.CHANNEL,
        'obj_type': ObjType.CHANNEL
    },
    {
        "page": PageCode.EXPLORE_MUSIC,
        "code": BlockCode.POPULAR_CHANNEL,
        "order": 4,
        "props": {
            "title": "US/UK",
            "description": ""
        },
        "type": ComponentCode.CHANNELS,
        "route": PageRoute.CHANNELS,
        "item_route": ItemRoute.CHANNEL,
        'obj_type': ObjType.CHANNEL
    },
    {
        "page": PageCode.EXPLORE_MUSIC,
        "code": BlockCode.POPULAR_CHANNEL,
        "order": 5,
        "props": {
            "title": "Top Artists",
            "description": ""
        },
        "type": ComponentCode.CHANNELS,
        "route": PageRoute.CHANNELS,
        "item_route": ItemRoute.CHANNEL,
        'obj_type': ObjType.CHANNEL
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
        return mockup_home

    @staticmethod
    def get_explore(page_explore):
        if f'/{page_explore}' == PageRoute.LIVE:
            return mockup_explore_live
        if f'/{page_explore}' in [PageRoute.MUSIC, PageRoute.TOP_MUSIC]:
            return mockup_explore_music
        if f'/{page_explore}' in [PageRoute.SHORTS, PageRoute.TOP_SHORT]:
            return mockup_explore_short
