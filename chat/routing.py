from django.urls import re_path
from . import consumers
# routing.py：websocket路由文件，相当于django的urls.py。
# 它根据websocket请求的url地址触发consumers.py里定义的方法。
# 它的作用是将发送至ws/chat/<room_name>/的websocket请求转由ChatConsumer处理。
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]