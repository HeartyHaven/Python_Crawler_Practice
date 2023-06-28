import requests
url="https://api.bilibili.com/x/web-interface/popular"
#重新封装参数
param={
"ps": "20",
"pn": "1"
}
header={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
resp=requests.get(url=url,params=param,headers=header)
# print(resp.request.headers)

print(resp.json())
resp.close()#访问完了之后要把链接关闭，否则打开次数过多就容易报错