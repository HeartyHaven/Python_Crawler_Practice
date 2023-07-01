
from Crypto.Cipher import AES
from base64 import b64encode
import json
import requests
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
#请求方式是post
data={
"csrf_token":"",
"cursor": "-1",
"offset": "0",
"orderType": "1",
"pageNo": "1",
"pageSize": "20",
"rid": "R_SO_4_447926067",
"threadId": "R_SO_4_447926067"
}#就是那个i4m,未加密的原始参数。
#服务于d的参数，i是手动固定的，人家的函数是随机的。
i="9DtJctD0E8p5b9CW"
e="010001"
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"

def to_16(data):#这个是把data补到16的倍数位，具体为什么或者怎么做，我确实也不知道。
    pad=16-len(data)%16
    data+=chr(pad)*pad
    return data

def get_encSecKey():
    return "3b2e893f109c3407502321939065d13e6c69e11b914a5a3701385f90a5dd0def0e8d9b884442daa78a7161eaf74e5e3fb1ef009630bab921f2d8e46aba9bb2d705fba77b0eac4e5ba102d798c014ae3286c851ebee90f5cc84c2d99426485cb61ff49c3c1b96142eb509f7bfef2bd9dc5bd16ce74ca3111b317e6e08f1646e3d"
def enc_params(data,key): #默认这里收到的是字符串不是对象,这个函数实际模拟了b函数。里面要用的AES加密算法可以采用第三方库crypto
    aes=AES.new(key=key.encode('utf-8'),IV="0102030405060708".encode('utf-8'),mode=AES.MODE_CBC) #这些参数设置在源程序中可以发现端倪        #实例化
    data=to_16(data)
    enp=aes.encrypt(data.encode('utf-8'))           #加密，加密的内容的长度必须是16的倍数，不满16个要补16-len个char(16-len),刚好16个的话，要补16个char(16)
    enp=str(b64encode(enp),"utf-8") #这里直接加密得到的东西不能被utf-8识别，所以要先用b64对它进行编码，才能够被utf-8识别。
    return enp
def get_params(data):#默认收到的是字符串而不是对象
    tmp1=enc_params(data,g)
    tmp2=enc_params(tmp1,i)
    return tmp2             #返回的就是params


headers={
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9",
"content-length": "604",
"content-type": "application/x-www-form-urlencoded",
"cookie": "NMTID=00O90gZNFkdSA1F7k8mmptFCwBlGukAAAGJD6S-KA; _iuqxldmzr_=32; _ntes_nnid=9074d657518d90a4dc7265fe5b2d9e9d,1688184602597; _ntes_nuid=9074d657518d90a4dc7265fe5b2d9e9d; WNMCID=byarsu.1688184606843.01.0; WEVNSM=1.0.0; WM_NI=oQunZKwnzmipN0kLY2owl2S9DWSn2aphkFq5RA05sXAR49CwrbqH3%2Bl59oi6vxImQGchcHefp190Ng5bPtnDMcPtGFwAnxK29RgrL0BiSwx6C2IkEF8NU01Bgx2YkpZiaW4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed7b87f8f9aa3d9f15ff5b88fa2d84a829f9b83c864a58ce58ec649f1878cb7c12af0fea7c3b92aad8fbb8fd941b5b2b68eec7c8ef0a5addc3aada9a4d3d23388899d8fb16bb4b8a5a7f43f929f00d6f254838efcdac27db2bebfa9b221b0ebf790ec3eb6a8878ed44da1b8ada9e86eb4eff7d1cd6df7bea095ed508fbda095c64eb59fa299ca3afb8ea993cf3c82b79d98fb3e81ee878cc84efc929bd1b44aa5a8febaea7c9ab7afb8b737e2a3; WM_TID=3THH8F5gC5FARAUBFQbA1wCv2HG2cWAE; ntes_utid=tid._.oinrWOMRdmZBRlQAFQfEhwD7iDT2cCtb._.0; sDeviceId=YD-HbiZQ3JdiChFR0FUERfFxa9VPfUXz8mJ; JSESSIONID-WYYY=2H%2Fi1X2%2BJgNYfpyGgq8bAV9ZlCkNmGlR%2BkbhKAXtuvhMIFzRCOJ1nCjMAG1pAPRwnb6bFSj%2BKGETpe7bdX5HDmrxUXPYg3smJ%2BzdfDz2UM4%2FUkqGQVn7FPlRHi%5CXGJRB5dwIj6qY%2F21EqudNecrAxbjqQc%2Fy20%2BVkJCn0ixY4n%5CputeX%3A1688201589506",
"origin": "https://music.163.com",
"referer": "https://music.163.com/song?id=447926067",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

resp=requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
},headers=headers)
# print(get_params(json.dumps(data)))
# print(get_encSecKey())
print(resp.text)#很遗憾，AES加密算法这里我由于没有相关知识，导致非常迷糊，然后为什么要转码我也不知道。只是相当于把js的代码用py复现了一下。
