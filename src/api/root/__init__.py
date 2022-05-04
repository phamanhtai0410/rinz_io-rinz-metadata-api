# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask import Blueprint

from .controller import health_check, get_page, get_obj_by_id, get_more_of_items, get_more_items

rest_root = Blueprint('rest_root', __name__, url_prefix='')
rest_root.add_url_rule('/common/health_check', view_func=health_check)
rest_root.add_url_rule('/<explore>', view_func=get_page)
rest_root.add_url_rule('', view_func=get_page)
rest_root.add_url_rule('/<route>/items', view_func=get_more_items)
rest_root.add_url_rule('/<route>/<obj_id>', view_func=get_obj_by_id)
rest_root.add_url_rule('/<route>/<obj_id>/<more_type>', view_func=get_more_of_items)

# rest_root.add_url_rule('', view_func=get_explore)
