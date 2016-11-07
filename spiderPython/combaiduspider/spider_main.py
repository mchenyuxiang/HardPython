# -*-coding:utf-8-*-
import urllib

from combaiduspider import html_downloader
from combaiduspider import html_parser

class SpiderMain(object):
    def __init__(self):
        # self.keyword = keyword_manager.KeywordManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        # self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        # 得到:关键词列表
        # new_keyword = self.keyword.get_new_keyword()
        html_cont = self.downloader.download(root_url)
        # 得出网址
        new_data = self.parser.paser(html_cont)
        # self.url.add_new_url(new_urls)
        # self.outputer.collect_data(new_data)
        # self.output.output_html()
        for name in new_data:
            print name.get_text()


if __name__ == '__main__':
    root_name = u"畜牧蚊香"
    root_name = root_name.encode('utf-8')
    root_name = urllib.quote(root_name)
    root_pd = 20
    root_url = "http://www.baidu.com/s?wd=%r&pn=%d" % (root_name,root_pd)
    print root_url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)