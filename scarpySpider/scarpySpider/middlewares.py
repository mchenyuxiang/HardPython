#!/usr/bin/python
# -*-coding:utf-8-*-

import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            print ua, '-----------------yyyyyyyyyyyyyyyyyyyyyyyyy'
            request.headers.setdefault('User-Agent', ua)

            # the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape

class ProxyMiddleware(object):

    def process_request(self,request,spider):
        request.meta['proxy'] = 'http://221.216.94.77:808'