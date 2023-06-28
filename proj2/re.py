import re
import requests
import csv


headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
}#直接获取什么也得不到可能是反扒机制导致的，所以需要伪造一个请求头
f=open("data.csv",mode="w",encoding="utf-8")
csvwriter=csv.writer(f)
for p in range (0,250,25):
    url=f"https://movie.douban.com/top250?start={p}"
    print(url)
    resp=requests.get(url,headers=headers)
    # print(resp.text)
    page_content=resp.text
    #解析数据
    obj=re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<p.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<ratings>.*?)</span>.*?<span>(?P<comments>.*?)人评价</span>',re.S)
    res=obj.finditer(page_content)
    for it in res:
        # print(it)
        dic=it.groupdict()
        # print(dic.values())
        dic["year"]=dic["year"].strip()
        csvwriter.writerow(dic.values())
f.close
print("done!")