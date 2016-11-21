# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import scrapy

dbuser = 'root'
dbpass = 'hndct888'
dbname = 'spider'
dbhost = '564222ff17911.sh.cdb.myqcloud.com'
dbport = 6922

class RankPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser,passwd=dbpass,db=dbname,host=dbhost,port=dbport,charset="utf8")
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            print item['rank']
            print item['keyword'].encode('utf-8')
            self.cursor.execute("""INSERT INTO tb_rank (companyId,rank, keyword, platformId,createTime)
                                       VALUES (%s,%s, %s, %s, now())""",
                                (
                                    item['companyId'],
                                    item['rank'],
                                    item['keyword'].encode('utf-8'),
                                    item['platformId'],
                                )
                                )
            print '-------------------test--------------------'
            self.conn.commit()


        except MySQLdb.Error,e:
            print "Error %d:%s" % (e.args[0],e.args[1])
        return item
