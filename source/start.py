#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
"""
模块用途描述

Authors: zhangzhenhu(zhangzhenhu@iwaimai.baidu.com)
Date:    2016/12/25 17:29
"""
import json
import locale
import os.path
import sys

import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

# locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF8')
# sys.path.append('../')

__TASK_NAME = "webapp"
__version__ = 1.0

define("port", default=8088, help="run on the given port", type=int)


# 定义监听的端口，随便挑个喜欢的数字吧

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/(.+)", tornado.web.StaticFileHandler, {"path": "./"}),
            (r"/$", tornado.web.RedirectHandler, {'url': '/index.html'}),
            # (r"/(.*)", StaticHandler),
        ]
        # script_path = os.path.dirname(os.path.relpath(__file__))
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            # static_path="./",
            # static_url_prefix="/",
            debug=True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
