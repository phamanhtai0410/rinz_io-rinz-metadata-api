import pydash as py_
from pymodm import fields

from lib.model import BaseMG
from lib.util import dt_utcnow


class UserModel(BaseMG):
    class Meta:
        collection_name = 'users'
        final = True
        ignore_unknown_fields = True

    public_address = fields.CharField(required=True)
    last_login = fields.DateTimeField(default=dt_utcnow)
    username = fields.CharField(blank=True, default='Unnamed')
    avatar = fields.CharField(blank=True, default='')
    language = fields.CharField(blank=True, default='')

