## asyncio
```
asyncio模块提供了使用协程构建并发应用的工具。它使用一种单线程单进程的的方式实现并发，应用的各个部分彼此合作, 可以显示的切换任务，一般会在程序阻塞I/O操作的时候发生上下文切换如等待读写文件,或者请求网络。同时asyncio也支持调度代码在将来的某个特定事件运行，从而支持一个协程等待另一个协程完成，以处理系统信号和识别其他一些事件。
```
### 异步并发的概念
```
对于其他的并发模型大多数采取的都是线性的方式编写。并且依赖于语言运行时系统或操作系统的底层线程或进程来适当地改变上下文，而基于asyncio的应用要求应用代码显示的处理上下文切换。
asyncio提供的框架以事件循环(event loop)为中心，程序开启一个无限的循环，程序会把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。

事件循环

事件循环是一种处理多并发量的有效方式，在维基百科中它被描述为「一种等待程序分配事件或消息的编程架构」，我们可以定义事件循环来简化使用轮询方法来监控事件，通俗的说法就是「当A发生时，执行B」。事件循环利用poller对象，使得程序员不用控制任务的添加、删除和事件的控制。事件循环使用回调方法来知道事件的发生。它是asyncio提供的「中央处理设备」，支持如下操作：

注册、执行和取消延迟调用（超时）
创建可用于多种类型的通信的服务端和客户端的Transports
启动进程以及相关的和外部通信程序的Transports
将耗时函数调用委托给一个线程池
单线程（进程）的架构也避免的多线程（进程）修改可变状态的锁的问题。
与事件循环交互的应用要显示地注册将运行的代码，让事件循环在资源可用时向应用代码发出必要的调用。如：一个套接字再没有更多的数据可以读取，那么服务器会把控制全交给事件循环。

```

### 协程
```
一般异步方法被称之为协程(Coroutine)。asyncio事件循环可以通过多种不同的方法启动一个协程。一般对于入口函数，最简答的方法就是使用run_until_complete(),并将协程直接传入这个方法。
import asyncio


async def foo():
    print("这是一个协程")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("开始运行协程")
        coro = foo()
        print("进入事件循环")
        loop.run_until_complete(coro)
    finally:
        print("关闭事件循环")
        loop.close()
输出

开始运行协程
进入事件循环
这是一个协程
关闭事件循环
这就是最简单的一个协程的例子，下面让我们了解一下上面的代码.
第一步首先得到一个事件循环的应用也就是定义的对象loop。可以使用默认的事件循环，也可以实例化一个特定的循环类(比如uvloop),这里使用了默认循环run_until_complete(coro)方法用这个协程启动循环，协程返回时这个方法将停止循环。
run_until_complete的参数是一个futrue对象。当传入一个协程，其内部会自动封装成task，其中task是Future的子类。关于task和future后面会提到。

从协程中返回值

将上面的代码，改写成下面代码

import asyncio


async def foo():
    print("这是一个协程")
    return "返回值"


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("开始运行协程")
        coro = foo()
        print("进入事件循环")
        result = loop.run_until_complete(coro)
        print(f"run_until_complete可以获取协程的{result}，默认输出None")
    finally:
        print("关闭事件循环")
        loop.close()
run_until_complete可以获取协程的返回值，如果没有给定返回值，则像函数一样，默认返回None。

协程调用协程

一个协程可以启动另一个协程，从而可以任务根据工作内容，封装到不同的协程中。我们可以在协程中使用await关键字，链式的调度协程，来形成一个协程任务流。向下面的例子一样。

import asyncio


async def main():
    print("主协程")
    print("等待result1协程运行")
    res1 = await result1()
    print("等待result2协程运行")
    res2 = await result2(res1)
    return (res1,res2)


async def result1():
    print("这是result1协程")
    return "result1"


async def result2(arg):
    print("这是result2协程")
    return f"result2接收了一个参数,{arg}"


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(main())
        print(f"获取返回值:{result}")
    finally:
        print("关闭事件循环")
        loop.close()
输出

主协程
等待result1协程运行
这是result1协程
等待result2协程运行
这是result2协程
获取返回值:('result1', 'result2接收了一个参数,result1')
关闭事件循环

```

### 协程中调用普通函数
```
在协程中可以通过一些方法去调用普通的函数。可以使用的关键字有call_soon,call_later，call_at。

call_soon

可以通过字面意思理解调用立即返回。

loop.call_soon(callback, *args, context=None)
在下一个迭代的时间循环中立刻调用回调函数,大部分的回调函数支持位置参数，而不支持”关键字参数”，如果是想要使用关键字参数，则推荐使用functools.aprtial()对方法进一步包装.可选关键字context允许指定要运行的回调的自定义contextvars.Context。当没有提供上下文时使用当前上下文。在Python 3.7中， asyncio
协程加入了对上下文的支持。使用上下文就可以在一些场景下隐式地传递变量，比如数据库连接session等，而不需要在所有方法调用显示地传递这些变量。
下面来看一下具体的使用例子。

import asyncio
import functools


def callback(args, *, kwargs="defalut"):
    print(f"普通函数做为回调函数,获取参数:{args},{kwargs}")


async def main(loop):
    print("注册callback")
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwargs="not defalut")
    loop.call_soon(wrapped, 2)
    await asyncio.sleep(0.2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main(loop))
finally:
    loop.close()
输出结果

注册callback
普通函数做为回调函数,获取参数:1,defalut
普通函数做为回调函数,获取参数:2,not defalut
通过输出结果我们可以发现我们在协程中成功调用了一个普通函数，顺序的打印了1和2。

有时候我们不想立即调用一个函数，此时我们就可以call_later延时去调用一个函数了。

call_later

loop.call_later(delay, callback, *args, context=None)
首先简单的说一下它的含义，就是事件循环在delay多长时间之后才执行callback函数.
配合上面的call_soon让我们看一个小例子

import asyncio


def callback(n):
    print(f"callback {n} invoked")


async def main(loop):
    print("注册callbacks")
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)
    await asyncio.sleep(0.4)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()
输出

注册callbacks
callback 3 invoked
callback 2 invoked
callback 1 invoked
通过上面的输出可以得到如下结果：
1.call_soon会在call_later之前执行，和它的位置在哪无关
2.call_later的第一个参数越小，越先执行。

call_at

loop.call_at(when, callback, *args, context=None)
call_at第一个参数的含义代表的是一个单调时间，它和我们平时说的系统时间有点差异，
这里的时间指的是事件循环内部时间，可以通过loop.time()获取，然后可以在此基础上进行操作。后面的参数和前面的两个方法一样。实际上call_later内部就是调用的call_at。

import asyncio


def call_back(n, loop):
    print(f"callback {n} 运行时间点{loop.time()}")


async def main(loop):
    now = loop.time()
    print("当前的内部时间", now)
    print("循环时间", now)
    print("注册callback")
    loop.call_at(now + 0.1, call_back, 1, loop)
    loop.call_at(now + 0.2, call_back, 2, loop)
    loop.call_soon(call_back, 3, loop)
    await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("进入事件循环")
        loop.run_until_complete(main(loop))
    finally:
        print("关闭循环")
        loop.close()
输出

进入事件循环
当前的内部时间 4412.152849525
循环时间 4412.152849525
注册callback
callback 3 运行时间点4412.152942526
callback 1 运行时间点4412.253202825
callback 2 运行时间点4412.354262512
关闭循环
因为call_later内部实现就是通过call_at所以这里就不多说了。
```