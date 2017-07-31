# coding:utf-8

#from scrapy import cmdline
import os
import MySQLdb

from scarpySpider import settings

# cmdline.execute("scrapy crawl shenma_rank".split())
# cmdline.execute("scrapy crawl baidu_mobile_rank".split())
# cmdline.execute("scrapy crawl baidu_rank".split())
# cmdline.execute("scrapy crawl author".split())
# os.system("scrapy crawl baidu_rank")
# os.system("scrapy crawl baidu_mobile_rank")
# os.system("scrapy crawl sogou_rank")
# os.system("scrapy crawl 360_rank")
# os.system("scrapy crawl 360_mobile_rank")
os.system("scrapy crawl sogou_mobile_rank")
# os.system("scrapy crawl shenma_rank")

# # 更新数据余额
# dbuser = settings.MYSQL_USER
# dbpass = settings.MYSQL_PASSWD
# dbname = settings.MYSQL_DBNAME
# dbhost = settings.MYSQL_HOST
# dbport = settings.MYSQL_PORT
# #
# conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, port=dbport, charset="utf8")
# cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
# #
# cur.execute("call UpdateBalance")
# cur.close()
