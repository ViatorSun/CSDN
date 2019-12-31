#  !/usr/bin/env  python
#  -*- coding:utf-8 -*-
# @Time   :  2019.12
# @Author :  绿色羽毛
# @Email  :  lvseyumao@foxmail.com
# @Blog   :  https://blog.csdn.net/ViatorSun
# @Note   :  刷新博客访问量



from crawBase import *
import webbrowser as web


'''  访问csdn   '''
class AccessCsdn(CrawBase):

    # 解析所有博客链接
    def getArticals(self, url):
        c = self.get(url)
        html = etree.HTML(c)
        link = html.xpath('//div[@class="article-list"]//a/@href')
        return link

    def geAllArticals(self, urlBase):
        i = 1
        urls = []
        url = urlBase
        while True:
            # print('sfs  '+url)
            url = urlBase + '/article/list/%s' % i
            t = self.getArticals(url)
            urls += t
            if len(t) == 0:
                break
            i += 1
        return urls

    def run(self, url, sec):
        urls = self.geAllArticals(url)   # 解析所有博客链接
        urls = list(set(urls))
        print(len(urls))
        while True:
            for url in urls:
                # print(url)
                web.open(url )
                print(url)
            print("Waiting for the next time...... ")
            time.sleep(sec)


if __name__ == '__main__':
    url = "https://blog.csdn.net/viatorsun"
    access_csdn = AccessCsdn()
    access_csdn.run(url, 200)

