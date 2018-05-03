# 第二天
##  递归
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
阶乘： n的阶乘为n * (n-1) *  (n-2) * ... * 1

````
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(5))
````

使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
````
def test():
    return test()
if __name__ == "__main__":
    test()
````
RecursionError: maximum recursion depth exceeded 递归异常，超过最大递归深度

x的n次幂 等于x 的n-1次幂乘x，x的0次幂等于1
````
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n -1)
if __name__ == "__main__":
    print(power(2, 6))
````

练习：取出n层嵌套列表里的所有元素
提示判断一个元素i是否是list 使用sinstance(i,list)函数

## 闭包
````
def npower():
    n = 2
    def  power(x):
        return x ** n
    return power

if __name__ == "__main__":
    f = npower()
    print(f(2))
    print(f(3))
````

在Python中创建一个闭包可以归结为以下三点
+ 闭包函数必须有内嵌函数
+ 内嵌函数需要引用该嵌套函数上一级命名空间中的变量
+ 闭包函数必须返回内嵌函数
在Python中，函数对象有一个__closure__属性，我们可以通过这个属性看看闭包的一些细节
````
def npower():
    n = 2
    def  power(x):
        return x ** n
    return power

if __name__ == "__main__":
    f = npower()
    print(f(2))
    print(f.__closure__)
    print(f.__closure__[0].cell_contents)
````
从这里可以看到闭包的原理，当内嵌函数引用了包含它的函数（enclosing function）中的变量后，
这些变量会被保存在闭包函数的__closure__属性中，成为闭包函数本身的一部分；
也就是说，这些变量的生命周期会和闭包函数一样。

## 装饰器


装饰器是可调用的对象，其参数是另一个函数（被装饰的函数），装饰器可以处理被装饰的函数，然后把它返回，
也可以将其替换成另一个函数或可调用对象

替换为另一个函数
````
def deco(func):
    def inner():
        print("running inner()")
    return inner

@deco
def target():
    print('running target()')


if __name__ == "__main__":
    target()

````

它可以让被装饰的函数在不需要做任何代码变动的前提下增加额外的功能，
被装饰的函数当作参数传入，装饰器返回经过修饰后函数的名字；
内层函数（闭包）负责修饰被修饰函数。从上面这段描述中我们需要记住装饰器的几点属性，以便后面能更好的理解

+ 实质： 是一个函数
+ 参数：被装饰函数名
+ 返回：返回一个函数（被装饰的函数或者另一个函数）
+ 作用：为已经存在的对象添加额外的功能

统计函数的执行时间
````
import time

def decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)

    return wrapper

@decorator
def func():
    print("hello world")
    time.sleep(1)

func()
````

返回函数被装饰的函数
````
def add_decorator(f):
    print("加法")
    return f

@add_decorator
def add_method(x, y):
    return x + y


print(add_method(2,3))

````

调用被装饰函数时,参数传递给返回的函数，所以wrap的参数要与被装饰函数一致，或者写成wrap(*arg, **dict)
````
def add_decorator(f):
    def wrap(x,y):
        print("加法")
        return f(x,y)
    return wrap

@add_decorator
def add_method(x, y):
    return x + y


print(add_method(2,3))
````

带参数的装饰器，本质是一个返回装饰器的函数
````
def out_f(arg):
    print("out_f" + arg)
    def decorator(func):
        def inner():
            func()
        return inner
    return decorator

@out_f("123")
def func():
    print("hello word")


func()
````
参数123传给函数out_f  返回装饰器decorator，@out_f("123")  就是@decorator

### 可迭代的对象，迭代器
迭代的意思是重复做一些事很多次，for循环就是一种迭代，列表，字典，元组都是可迭代对象
实现__iter__方法的对象都是可迭代的对象。 __iter__ 返回一个迭代器，所谓迭代器就是具有next方法的对象
在掉用next方法的时，迭代器会返回它的下一个值，如果没有值了，则返回StopIteration
````
>>> l = [1,2,3]   # l为可迭代对象
>>> b = l.__iter__()    #b 为迭代器
>>> next(b)
1
>>> next(b)
2
>>> next(b)
3
>>> next(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
````