# 第二套
##  递归
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
阶乘： n的阶乘为n * (n-1) *  (n-2) * ... * 1

``
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(5))
``

使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
``
def test():
    return test()
if __name__ == "__main__":
    test()
``
RecursionError: maximum recursion depth exceeded 递归异常，超过最大递归深度

x的n次幂 等于x 的n-1次幂乘x，x的0次幂等于1
``
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n -1)
if __name__ == "__main__":
    print(power(2, 6))
``

练习：取出n层嵌套列表里的所有元素
提示判断一个元素i是否是list 使用sinstance(i,list)函数

## 闭包
``
def npower():
    n = 2
    def  power(x):
        return x ** n
    return power

if __name__ == "__main__":
    f = npower()
    print(f(2))
    print(f(3))
``

在Python中创建一个闭包可以归结为以下三点
+ 闭包函数必须有内嵌函数
+ 内嵌函数需要引用该嵌套函数上一级命名空间中的变量
+ 闭包函数必须返回内嵌函数
在Python中，函数对象有一个__closure__属性，我们可以通过这个属性看看闭包的一些细节
``
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
``
从这里可以看到闭包的原理，当内嵌函数引用了包含它的函数（enclosing function）中的变量后，
这些变量会被保存在闭包函数的__closure__属性中，成为闭包函数本身的一部分；
也就是说，这些变量的生命周期会和闭包函数一样。

## 装饰器
