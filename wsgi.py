# coding: utf-8

from gevent import monkey
monkey.patch_all()

import os
# Django configuration
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import leancloud
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from cloud import engine


APP_ID = os.environ['LEANCLOUD_APP_ID']
MASTER_KEY = os.environ['LEANCLOUD_APP_MASTER_KEY']
PORT = int(os.environ['LEANCLOUD_APP_PORT'])

leancloud.init(APP_ID, master_key=MASTER_KEY)

application = engine

if __name__ == '__main__':
    if os.environ['LEANCLOUD_APP_ENV'] == 'development':
        server = WSGIServer(('localhost', PORT), application, handler_class=WebSocketHandler)
    else:
        server = WSGIServer(('0.0.0.0', PORT), application, log=None, handler_class=WebSocketHandler)
    server.serve_forever()
