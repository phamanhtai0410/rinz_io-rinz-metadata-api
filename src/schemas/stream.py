# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import Schema, EXCLUDE, fields

from src.enums.video import VideoType


class StreamVideo(Schema):
    class Meta:
        ordered = True
        unknown = EXCLUDE

    video_id = fields.Str()
    playback_uri = fields.Str()
    duration = fields.Str()
    resolution = fields.Int()
    type = fields.Str(missing=VideoType.VOD)
