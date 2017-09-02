# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
import scrapy

from twisted.enterprise import adbapi
from scarpySpider import settings



class RankPipeline(object):
    def __init__(self):
        dbuser = settings.MYSQL_USER
        dbpass = settings.MYSQL_PASSWD
        dbname = settings.MYSQL_DBNAME
        dbhost = settings.MYSQL_HOST
        dbport = settings.MYSQL_PORT
        self.conn = MySQLdb.connect(user=dbuser,passwd=dbpass,db=dbname,host=dbhost,port=dbport,charset="utf8")
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            print item['rank']
            print item['keyword'].encode('utf-8')
            #INSERT
            #INTO
            #zzcms_seo_costdetail(platformid, keywordid, webid, userid, createtime, rank, priceone, pricetwo)
            #VALUES()
            if int(item['rank']) <= 10:
                print item['rank']
                priceone = item['priceone']
                pricetwo = 0
            # elif int(item['rank']) <=20:
            #     print item['rank']
            #     priceone = 0
            #     pricetwo = item['pricetwo']
            else:
                priceone = 0
                pricetwo = 0
            #   DATE_SUB(NOW(),INTERVAL 1 DAY)
            self.cursor.execute("""INSERT INTO zzcms_seo_costdetail(platformid,keywordid,webid,userid,createTime,rank,priceone,pricetwo,keywordname)
                                       VALUES (%s,%s, %s, %s, now(),%s,%s,%s,%s)""",
                                (
                                    item['platformId'],
                                    item['keywordId'],
                                    item['webId'],
                                    item['userId'],
                                    item['rank'],
                                    priceone,
                                    pricetwo,
                                    item['keyword'].encode('utf-8')
                                )
                                )
            print '-------------------test--------------------'
            self.conn.commit()


        except MySQLdb.Error,e:
            print "Error %d:%s" % (e.args[0],e.args[1])
        return item

class MysqlTwistedPipeline(object):
    def __init__(self):
        # self.dbpool = dbpool
        dbparms = dict(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            cursorclass=MySQLdb.cursors.DictCursor,
            charset="utf8",
            use_unicode=True,
            port=settings.MYSQL_PORT,
            cp_reconnect = True
        )
        self.dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

    # @classmethod
    # def from_setting(cls,settings):
    #     dbparms = dict(
    #         host = settings['MYSQL_HOST'],
    #         db = settings['MYSQL_DBNAME'],
    #         user = settings['MYSQL_USER'],
    #         passwd = settings['MYSQL_PASSWD'],
    #         charset = "uft8",
    #         cursorclass = MySQLdb.cursors.DictCursor,
    #     )
    #     dbpool = adbapi.ConnectionPool("MySQLdb",**dbparms)
    #
    #     return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twised将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error)

    def handle_error(self,failure):
        print failure

    def do_insert(self, cursor, item):
        ## 执行具体插入
        try:
            print item['rank']
            print item['keyword'].encode('utf-8')
            # INSERT
            # INTO
            # zzcms_seo_costdetail(platformid, keywordid, webid, userid, createtime, rank, priceone, pricetwo)
            # VALUES()
            if int(item['rank']) <= 10:
                print item['rank']
                priceone = item['priceone']
                pricetwo = 0
            # elif int(item['rank']) <=20:
            #     print item['rank']
            #     priceone = 0
            #     pricetwo = item['pricetwo']
            else:
                priceone = 0
                pricetwo = 0
            cursor.execute("""INSERT INTO zzcms_seo_costdetail(platformid,keywordid,webid,userid,createTime,rank,priceone,pricetwo,keywordname)
                                             VALUES (%s,%s, %s, %s, now(),%s,%s,%s,%s)""",
                                (
                                    item['platformId'],
                                    item['keywordId'],
                                    item['webId'],
                                    item['userId'],
                                    item['rank'],
                                    priceone,
                                    pricetwo,
                                    item['keyword'].encode('utf-8')
                                )
                                )
            print '-------------------test--------------------'


        except MySQLdb.Error, e:
            print "Error %d:%s" % (e.args[0], e.args[1])