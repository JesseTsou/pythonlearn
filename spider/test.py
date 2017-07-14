#coding=utf-8
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    html = html.decode('utf8')
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


#html = getHtml("http://tieba.baidu.com/p/2460150866")
html = getHtml("http://fuliba.net/gay-bar.html")
print(html)
print(getImg(html))