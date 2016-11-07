#-*-coding:utf-8-*-
import urllib
import urllib2

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        response1 = urllib.urlopen(url)

        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
        response = urllib2.urlopen(request)

        if response1.getcode() != 200:
            return None

        return  response.read()