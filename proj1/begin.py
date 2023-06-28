from urllib.request import urlopen
#网址库中找到打开网址库
url="http://www.baidu.com"
resp=urlopen(url)
# print(resp.read())
# print(resp.read().decode("utf-8"))
with open("mybaidu.html",mode="w")as f:
    f.write(resp.read().decode("utf-8"))
f.close()#读完文件之后记得关掉
print("over!")