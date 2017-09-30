#coding:utf-8
import codecs
class DataOutput(object):
    '''
    数据存储器
    '''
    def __init__(self):
        self.datas = []

    def store_data(self,data):
        '''
        将解析出来的数据存储在内存中
        :param data:
        :return:
        '''
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        '''
        将存储的数据输出为指定的文件格式
        :return:
        '''
        fout = codecs.open('baike.html','w',encoding='utf-8')
        fout.write('<html>')
        fout.write("<head><meta charset='utf-8'/></head>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr><th>this page</th><th>title</th><th>1366_768</th><th>1680_1050</th></tr>")

        print '数组长度：%d' % self.datas.__len__()
        print '@#' * 30
        for data in self.datas:
            fout.write("<tr>")
            if data['page_url'] != None:
                fout.write("<td><a href='%s'>this_page</a></td>" % data['page_url'])
                print data['page_url']
            if data['title'] != '':
                fout.write("<td>%s</td>" % data['title'])
                print data['title']
            if data['imgurl_1366_768'] != '':
                fout.write("<td><a href='%s'>1366HD</a></td>" % data['imgurl_1366_768'])
                print data['imgurl_1366_768']
            if data['imgurl_1680_1050'] != '':
                fout.write("<td><a href=' %s '>1080BD</a></td>" % data['imgurl_1680_1050'])
                print data['imgurl_1680_1050']
            fout.write("</tr>")
            self.datas.remove(data)
        fout.write("</table>")
        fout.write("</body>")
        fout.write('</html>')
        fout.close()
