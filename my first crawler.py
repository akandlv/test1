'''
Created on 2014-4-28

@author: zt
'''
import urllib2,HTMLParser


req=urllib2.Request('http://www.baidu.com')
html=urllib2.urlopen(req)

result=html.read()
html.close()

class MyParser(HTMLParser.HTMLParser):
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
    i=0
    urls=[]
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        if tag=='a':
            for name,value in attrs:
                if name=='href' and value.startswith('http')and not(value in MyParser.urls):
                    MyParser.i+=1
                    MyParser.urls.append(value)
                    print value,'~~~~~~~~~~~~~~~i=',MyParser.i
                    try:
                        req=urllib2.Request(value,headers=MyParser.headers)
                        html=urllib2.urlopen(req)
                        data=html.read()
                        html.close()
                        my=MyParser()
                        my.feed(data)
                    except Exception as e:
                        print e
                else:
                    pass
        else:
            pass
        
my=MyParser()
my.feed(result)
