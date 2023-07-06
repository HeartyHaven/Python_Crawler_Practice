#本节任务：requests.get()->变成异步操作aiohttp
#需要安装库aiohttp
import aiohttp
import asyncio      #这两个分不开的。
#我现在想同时下载三个图片
urls=[
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220929/spzzt0t2vus.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220929/hwi11zgbwhq.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20220929/p5e5ne4j3hd.jpg"
]
async def picdownload(url):
#发送请求->得到图片内容->写入文件
    name=url.rsplit("/",1)[1]  #获取一个文件名.rsplit=right split从右边开始切分，切一次。
    async with aiohttp.ClientSession() as session:#with的意义在于自动有上下文理解能力，能够在你跳出这个缩进的时候自动关闭这个open的东西。
    #这个aiohttp.ClientSession等价于原来的requests这个模块
        async with session.get(url) as resp:    #requests.get(url)
            #请求下来了。写入文件。
            #也可以利用aiofiles实现异步写入文件。
            with open(name,mode='wb') as f:
                f.write(await resp.content.read())#async下获取二进制字节内容还需要最后加一个read()
            # resp.text():async之下读取文本要加个括号
            #resp.json()：async之下读取json没有变化
            #异步操作在使用的时候讲究“挂起”，执行的时候要加一个await
    print(name+"done!")
    pass

async def main():
    tasks=[]
    for url in urls:
        tasks.append(picdownload(url))      #封装针对不同url的协程对象。
    
    await asyncio.wait(tasks)               #都是套路
    pass

if __name__=='__main__':
    asyncio.run(main())                     #这样写效率巨TM高