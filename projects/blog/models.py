import mongoengine as me
from datetime import datetime

class Posts(me.Document):
    title: str = me.StringField(required=True, max_length=200)
    contents: str = me.StringField(required=True)
    created_on = me.DateTimeField(default=datetime.now())

