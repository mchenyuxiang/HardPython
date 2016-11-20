#-*-coding:utf-8-*-
import scrapy
import urllib
import re
from urllib import quote_plus

from scarpySpider.spiders import html_downloader
from scarpySpider.spiders import html_parser


class QuotesSpider(scrapy.Spider):
    name = "baidu_rank"

    def __init__(self):
        # self.keyword = keyword_manager.KeywordManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        # self.outputer = html_outputer.HtmlOutputer()

    def start_requests(self):
        # urls = {
        #     'http://quotes.toscrape.com/page/1/',
        #     'http://quotes.toscrape.com/page/2/',
        # }
        root_name = ['长沙消防工程公司', '消防工程安装公司', '长沙安防工程', '长沙智能化弱电工程', '长沙监控安装公司']
        # root_name = ['长沙平江香干']
        # root_name = root_name.encode('utf-8')
        root_user_url = 'www.hndtai.com'
        # root_user_url = 'www.djpjxg.com'
        # root_user_url = 'http://www.seoai.cn/'
        # print root_name
        # root_pn = 0i
        root_url = "http://www.baidu.com/s"
        # for url in urls:
        yield scrapy.Request(url=root_url, meta={'root_name':root_name,'root_name_all':root_name,'root_user_url':root_user_url},callback=self.parse)

    def parse(self, response):
        # print response.body
        # page = response.url.split("/")[-2]
        for root_name_single in response.meta['root_name_all']:
            root_name = quote_plus(root_name_single)
            # 得到:关键词列表
            root_pn = 0
            domain_rank = root_pn / 10 - 1
            for root_pn in range(0, 51, 10):
                html_wd_pn = "?wd=%s&pn=%d" % (root_name, root_pn)
                html_url = response.url + html_wd_pn
                # print html_url
                html_cont = self.downloader.download(html_url)
                # 得出网址
                new_data = self.parser.baidu_paser(html_cont)
                # 得到客户的域名地址
                user_url_data = response.meta['root_user_url'].split(".")
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
                    pattern = re.compile(r'%s' % user_domain)
                    result1 = re.search(pattern, name.get_text())
                    if result1:
                        domain_rank = new_data.index(name) + 1
                        domain_rank = root_pn + domain_rank
                        # print domain_rank
                        break
                        # print name.get_text()
                # print domain_rank
                if domain_rank != -1:
                    break

            if domain_rank != -1:
                rank_message = "关键词：%s\t百度排名为： %d" % (root_name_single, domain_rank)
            else:
                rank_message = "关键词：%s\t百度排名50名之外" % root_name_single

            print rank_message
