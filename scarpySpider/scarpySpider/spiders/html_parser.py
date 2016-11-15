#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import re
import urllib

class HtmlParser(object):

    def _baidu_get_urls(self,soup):
        new_urls = set()
        links = soup.find_all(['a','span'],class_='c-showurl')
        return links

    # 百度列表网页解析
    def baidu_paser(self,html_cont):
        if html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._baidu_get_urls(soup)
        return new_urls