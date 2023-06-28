import requests
url="https://fanyi.baidu.com/sug"
s=input("input the word:")
dat={
    "kw":s
}
#发送的数据必须放在字典中，通过data进行参数传递
resp=requests.post(url,data=dat)
print(resp.json())