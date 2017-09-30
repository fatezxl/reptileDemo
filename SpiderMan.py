#coding:utf-8

#导入之前的所有文件
from DataOutput import DataOutput
from HtmlParser import HtmlParser
from HtmlDownloader import HtmlDownloader
from URLManager import UrlManager

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self,root_url):
        #添加入口URL
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url，同时判断抓取了多少个url,抓取数据数量限定在0——100之间
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                #从URL管理器获取新的url
                new_url = self.manager.get_new_url()
                #HTML下载器下载页面
                html = self.downloader.download(new_url)
                #HTML解析器抽取网页数据
                new_urls,data = self.parser.parser(root_url,new_url,html)
                #将抽取的url添加到URL管理器中
                self.manager.add_new_urls(new_urls)

                print '有待爬取的url数量：%d' % self.manager.new_url_size()

                #数据存储器存储文件
                self.output.store_data(data)
                print "已经抓取%s个链接"%self.manager.old_url_size()
            except Exception as e:
                print "crawl failed"
                print e.message
            #数据存储器将文件输出成指定格式
        self.output.output_html()

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("http://desk.zol.com.cn/")