import requests
query=input("input the keyword:")
url=f"https://www.so.com/s?q={query}"
dic={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
resq=requests.get(url,headers=dic)
print(resq)
print(resq.text)