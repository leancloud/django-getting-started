# coding: utf-8

from gevent import monkey
monkey.patch_all()

import os
# Django configuration
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import leancloud
from gevent.pywsgi import WSGIServer

from cloud import engine


APP_ID = os.environ['LC_APP_ID']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])

leancloud.init(APP_ID, master_key=MASTER_KEY)

application = engine

# The code below will only be executed locally (`lean up`),
# and will not be executed on the cloud.
if __name__ == '__main__':
    server = WSGIServer(('localhost', PORT), application)
    server.serve_forever()
