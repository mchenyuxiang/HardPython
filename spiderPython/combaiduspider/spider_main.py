# -*-coding:utf-8-*-

import html_spider

if __name__ == '__main__':
    # root_name = ['长沙消防工程公司','消防工程安装公司','长沙安防工程','长沙智能化弱电工程','长沙监控安装公司']
    # root_name = ['现货返佣网','原油返佣网','白银返佣网','返佣网']
    # root_name = ['真空手套箱','罐磨球磨机']
    root_name = ['智优营家']
    # root_name = root_name.encode('utf-8')
    # root_user_url = 'www.hndtai.com'
    # root_user_url = 'www.deco-mill.com'
    # root_user_url = 'www.deco-mill.com'
    root_user_url = 'www.zhiuseo.com'
    # root_user_url = 'http://www.seoai.cn/'
    # print root_name
    # root_pn = 0i
    # root_url = "http://www.baidu.com/s?"
    root_url = "https://www.so.com/s?"
    # print root_url
    obj_spider = html_spider.SpiderMain()
    # obj_spider.baidu_rank_craw(root_url,root_user_url,root_name)
    # obj_spider.sougou_rank_craw(root_url,root_user_url,root_name)
    obj_spider.sou_360_rank_craw(root_url,root_user_url,root_name)
