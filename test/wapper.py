#既不需要侵入，也不需要函数重复执行
import time


def deco(func):
    print(func)
    def wrapper(a,b):
        startTime = time.time()
        result = func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
        return result
    return wrapper


@deco
def func(a,b):
    print("hello")
    time.sleep(1)
    print("a + b = %s"%(a+b))
    return a+b

if __name__ == '__main__':
    f = func #这里f被赋值为func，执行f()就是执行func()
    print(f(3,4))
