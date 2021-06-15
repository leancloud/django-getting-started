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


APP_ID = os.environ['LC_APP_ID']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])

leancloud.init(APP_ID, master_key=MASTER_KEY)

application = engine

if __name__ == '__main__':
    log = 'default' if os.environ['LEANCLOUD_APP_ENV'] == 'development' else None
    server = WSGIServer(('', PORT), application, log=log, handler_class=WebSocketHandler)
    server.serve_forever()
