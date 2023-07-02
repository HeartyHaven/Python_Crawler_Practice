#1.如何提取单个页面的数据
#2.上线程池，多个页面同时抓取
import requests
# from lxml import etree
import re
import csv
from concurrent.futures import ThreadPoolExecutor
ans=[]
f=open("data.csv",mode='w',encoding='utf-8')
csvwriter=csv.writer(f)
csvwriter.writerow(('产地','产品','类别','单位','低价','高价','均价','发行时间'))
def download_single_page(url,dat):
    obj=r'"prodName":"(?P<pname>.*?)".*?"prodCat":"(?P<prodcat>.*?)"' \
        r'.*?"lowPrice":"(?P<lp>.*?)".*?"highPrice":"(?P<hp>.*?)".*?' \
        r'"avgPrice":"(?P<avgprice>.*?)".*?"place":"(?P<place>.*?)".*?' \
        r'"unitInfo":"(?P<unitinfo>.*?)".*?"pubDate":"(?P<pubdate>.*?)"'
    resp=requests.get(url,params=dat)
    resp.encoding='utf-8'
    resp=resp.text
    fiter=re.finditer(obj,resp)
    for f in fiter:
        txt=('nan'if f.group('place')=='' else f.group('place'),f.group('pname'),f.group('prodcat'),f.group('unitinfo'),f.group('lp'),
             f.group('hp'),f.group('avgprice'),f.group('pubdate'))
        csvwriter.writerow(txt)
    print("第",dat["current"],"页已经爬完！")
    pass
if __name__=='__main__':
    with ThreadPoolExecutor(100) as t:

        for i in range(1,200):
            dat={
                "current":str(i),
                "limit": '20',
                "count": '491510'
            }
            t.submit(download_single_page,url='http://www.xinfadi.com.cn/getPriceData.html',dat=dat)

    print('全部爬完！')
    f.close()