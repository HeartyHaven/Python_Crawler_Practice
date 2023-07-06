import aiohttp
import asyncio
import requests
from lxml import etree
import chardet
import aiofiles
def getcatalog(menuurl):
    resp0=requests.get(menuurl).text
    tree=etree.HTML(resp0)
    urls=tree.xpath('/html/body/div[3]/div/dl/dd/a/@href')
    urls=['https://www.biqudd.com/126_126944/'+i for i in urls[12:]]
    return urls
# print(urls)
# resp=requests.get(urls[0])
# print(resp.text)
async def aiocorrection(cont):
    cont = cont.replace(u'\xa0', u' ')
    cont = cont.replace(u'\x9f', u' ')
    cont = cont.replace(u'\x98', u' ')
    cont = cont.replace(u'\xdb', u' ')
    cont = cont.replace(u'\xf0', u' ')
    cont = cont.replace(u'\x83', u' ')
    cont = cont.replace(u'\x86', u' ')
    cont = cont.replace(u'\x87', u' ')
    cont = cont.replace(u'\x8c', u' ')
    cont = cont.replace(u'\xef', u' ')
    cont = cont.replace(u'\xf4', u' ')
    return cont

async def aiogetcontent(url):
    # print(url)
    name=url.rsplit("/",1)[1].strip(".html")
    async with aiohttp.ClientSession() as session:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                content = await resp.read()
                encoding = chardet.detect(content)['encoding']
                content = content.decode(encoding,errors='ignore')
                tree = etree.HTML(content)
            contents=tree.xpath('/html/body/div[1]/div[2]/div/div[4]/text()')
            contstr=''
            for cont in contents[1:]:
                cont=await aiocorrection(cont)
                contstr+=cont
                contstr+='\n'
            async with aiofiles.open('essays/'+name,mode='w',encoding='utf-8',errors='ignore') as f:
                try:
                    await f.write(contstr)
                except UnicodeError:
                    print(contstr)
    # print(name+' done!')
    pass
async def main():
    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(aiogetcontent(url)))
    await asyncio.wait(tasks)
    pass
if __name__=='__main__':
    menuurl = 'https://www.biqudd.com/126_126944/'
    urls=getcatalog(menuurl)
    asyncio.run(main())