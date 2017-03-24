# coding:utf-8

from scrapy import cmdline
import os
import MySQLdb

# cmdline.execute("scrapy crawl shenma_rank".split())
# cmdline.execute("scrapy crawl baidu_mobile_rank".split())
# cmdline.execute("scrapy crawl baidu_rank".split())
# cmdline.execute("scrapy crawl author".split())
#os.system("scrapy crawl baidu_rank")
#os.system("scrapy crawl baidu_mobile_rank")
#os.system("scrapy crawl sogou_rank")
#os.system("scrapy crawl 360_rank")
#os.system("scrapy crawl 360_mobile_rank")
#os.system("scrapy crawl sogou_mobile_rank")
#os.system("scrapy crawl shenma_rank")

# 更新数据余额
# dbuser = 'root'
# dbpass = 'hndct888'
# dbname = 'zzcms_test'
# dbhost = '564222ff17911.sh.cdb.myqcloud.com'
# dbport = 6922
#
# conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, port=dbport, charset="utf8")
# cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
#
# cur.execute("call UpdateBalance")
# cur.close()
