import asyncio
import time
async def fn():           #添加async:变成了异步协程函数
    print("nihao!")

async def func1():
    print("i am ")
    # time.sleep(2)         #同步休眠，休眠的时候不能执行其他任何任务
    await asyncio.sleep(2)  #异步的休眠，这个任务休眠的时候立刻运行其他的任务。
    print('func1')

async def func2():
    print("i am ")
    # time.sleep(2)
    await asyncio.sleep(2)
    print('func2')

async def func3():
    print("i am ")
    # time.sleep(2)
    await asyncio.sleep(2)
    print('func3')
async def main():
    # #python要求：1.await挂起操作必须放在这个定义的main里面。2.await必须放在协程对象前面。
    # #第一种写法，并不推荐：
    # f1=func1()
    # await f1...        #await挂起实际是调用一个异步协程对象，相当于就让f1运行起来了

    # tasks=[func1(),func2(),func3()]
    #为了应对python3.11即将废除这种直接把协程对象放到列表里边的问题，以后需要手动在tasks里面创建tasks对象。
    tasks=[
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    
    await asyncio.wait(tasks)   
    #await是挂起操作，指提上日程开始执行；asyncio.wait指的是task里面的函数应该以异步协程的方式运行。
    #之所以推荐这种方法，是因为这一套模板能够很完美地适配一个爬虫。
    #我们可以把不同的url封装在函数里面，形成一个函数组，放进一个tasks列表然后直接套到这个模板里边。
    #效率极高。
    pass
if __name__=='__main__':
    t1=time.time()
    asyncio.run(main())
    t2=time.time()
    print('time',t2-t1)#time 2.010483503341675