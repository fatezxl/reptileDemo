#coding:utf-8
import re
import urlparse
from bs4 import  BeautifulSoup

class HtmlParser(object):
    '''
    HTML解析器
    '''
    def parser(self,root_url,page_url,html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url: 下载页面的URL
        :param html_cont: 下载的网页内容
        :return: 返回URL和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser')#加上from_encoding='utf-8'会弹出警告
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(root_url,page_url,soup)
        print '***' * 30 + '当前页面：'
        print page_url
        print '--'*30 + 'url集合'
        print new_urls
        print '--' * 30 + 'data数据'
        print new_data
        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):
        '''
        抽取新的URL集合
        :param page_url: 下载页面的URL
        :param soup: soup
        :return: 返回新的URL集合
        '''
        new_urls = set()
        #抽取符合要求的a标记
        # 注意：此处规则很重要，关乎爬取的内容,此处举例：/fengjing/,/bizhi/7171_88712_2.html
        links = soup.find_all('a',href=re.compile(r'/\w+/'))
        links_2 = soup.find_all('a', href=re.compile(r'/bizhi/\d+/.html'))
        for link in links:
            #提取href属性
            new_url = link['href']
            #拼接成完整网址
            new_full_url = urlparse.urljoin(page_url,new_url).encode('utf-8')
            new_urls.add(new_full_url)
        for link2 in links_2:
            # 提取href属性
            new_url2 = link2['href']
            # 拼接成完整网址
            new_full_url2 = urlparse.urljoin(page_url, new_url2).encode('utf-8')
            new_urls.add(new_full_url2)
        return new_urls

    def _get_new_data(self,root_url,page_url,soup):
        '''
        抽取有效数据
        :param root_url:根地址
        :param page_url: 下载页面的URL
        :param soup:
        :return: 返回有效数据
        '''
        data = {
            'title' : '',
            'page_url' : '',
            'imgurl_1366_768' : '',
            'imgurl_1680_1050' : ''

        }
        #请求页面的地址
        data['page_url'] = page_url

        #图片标题
        #TODO 筛选存在问题
        test = soup.find(id='titleName')
        print 'title'
        print test
        # print test.string
        if test != None:
            print '不是none'
            print test.string

            title = soup.find(id='titleName').string
            print '编码之后：'
            print title
            data['title'] = title

            # 图片的地址
            # 1366x768
            if soup.find(id='1366x768')!=None:
                imgurl_136_768 = soup.find(id='1366x768')['href']
                new_full_url_1366_768 = urlparse.urljoin(root_url, imgurl_136_768)
                data['imgurl_1366_768'] = new_full_url_1366_768.encode('utf-8')
            #1680_1050
            if soup.find(id='1680x1050') != None:
                imgurl_1680_1050 = soup.find( id='1680x1050')['href']
                new_full_url_1680_1050 = urlparse.urljoin(root_url, imgurl_1680_1050)
                data['imgurl_1680_1050'] = new_full_url_1680_1050.encode('utf-8')


        # 参考案例
        # title = soup.find('i',class_='business-icon').find('img')['alt']
        # data['title'] = title.get_text()
        # summary = soup.find('div',class_='lemma-summary')
        # #获取tag中包含的所有文本内容，包括子孙tag中的内容，并将结果作为Unicode字符串返回
        # data['summary'] = summary.get_text()
        return data
