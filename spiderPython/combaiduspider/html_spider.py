# -*-coding:utf-8-*-
import urllib
import re

import html_downloader
import html_parser
from urllib import quote_plus

class SpiderMain(object):
    def __init__(self):
        # self.keyword = keyword_manager.KeywordManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        # self.outputer = html_outputer.HtmlOutputer()

    # 百度排名查询
    def baidu_rank_craw(self,root_url,root_user_url,root_name_all):
        for root_name_single in root_name_all:
            root_name = quote_plus(root_name_single)
            # 得到:关键词列表
            root_pn = 0
            domain_rank = root_pn / 10 - 1
            for root_pn in range(0, 51 ,10):
                html_wd_pn = "wd=%s&pn=%d" % (root_name,root_pn)
                html_url = root_url+html_wd_pn
                # print html_url
                html_cont = self.downloader.download(html_url)
                # 得出网址
                new_data = self.parser.baidu_paser(html_cont)
                # 得到客户的域名地址
                user_url_data = root_user_url.split(".")
                leng_url = len(user_url_data)
                if leng_url == 1:
                    user_domain = user_url_data
                elif leng_url > 1:
                    user_domain = user_url_data[1]
                else:
                    user_domain = '请输入域名'
                # print type(user_url_data)
                # print user_domain
                # 查询用户网址是否在当前页面，如果不在则翻页，最多查询5页内容
                for name in new_data:
                    pattern = re.compile(r'%s'%user_domain)
                    result1 = re.search(pattern, name.get_text())
                    if result1:
                        domain_rank = new_data.index(name)+1
                        domain_rank = root_pn + domain_rank
                        # print domain_rank
                        break
                    # print name.get_text()
                # print domain_rank
                if domain_rank != -1:
                    break

            if domain_rank != -1:
                rank_message =  "关键词：%s\t百度排名为： %d" % (root_name_single,domain_rank)
            else:
                rank_message =  "关键词：%s\t百度排名50名之外" % root_name_single

            print rank_message
