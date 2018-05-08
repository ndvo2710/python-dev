#  第三天
## 线程
线程是中轻量级的进程，所有线程均在同一个进程中，共享全局内存，用于任务并行
###  通过函数使用线程
实例1
````
import threading
import time


def helloworld():
    time.sleep(2)
    print("helloworld")


t = threading.Thread(target=helloworld)
t.start()
print("main thread")

````
注意：这里有两个线程一个是主线程，一个是通过threading模块产生的t线程，
这里程序并没有阻塞在helloword函数，主线程和t线程并行运行


实例2 同种任务并行

````
import threading
import time


def helloworld(id):
    time.sleep(2)
    print("thread %d helloworld" % id)


for i in range(5):
    t = threading.Thread(target=helloworld, args=(i,))
    t.start()
print("main thread")
````

实例3 线程间同步

````
import threading, time

count = 0

def adder():
    global count
    count = count + 1
    time.sleep(0.5)
    count = count + 1

threads = []
for i in range(10):
    thread = threading.Thread(target=adder)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(count)
````

加锁
````
import threading, time

count = 0

def adder(addlock):
    global count
    addlock.acquire()
    count = count + 1
    addlock.release()
    time.sleep(0.1)
    addlock.acquire()
    count = count + 1
    addlock.release()

addlock = threading.Lock()
threads = []
for i in range(100):
    thread = threading.Thread(target=adder,args=(addlock,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(count)
````
使用with 加锁

````
import threading, time

count = 0

def adder(addlock):
    global count
    with addlock:
        count = count + 1
    time.sleep(0.1)
    with addlock:
        count = count + 1

addlock = threading.Lock()
threads = []
for i in range(100):
    thread = threading.Thread(target=adder,args=(addlock,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(count)
````

### 通过类使用线程

实例1
继承threading.Thread 重写run方法
````
import threading, time


class HelloWorld(threading.Thread):
    def run(self):
        time.sleep(2)
        print("hellowrold")


t = HelloWorld()
t.start()
print("main thread")
````

实例2
````
import threading, time


class HelloWorld(threading.Thread):
    def __init__(self, id):
        self.id = id
        super(HelloWorld, self).__init__()
    def run(self):
        time.sleep(2)
        print("thread %d hellowrold" % self.id)

for i in range(5):
    t = HelloWorld(i)
    t.start()
print("main thread")
````

实例3
````
import threading, time


class HelloWorld(threading.Thread):
    count = 0
    def run(self):
        HelloWorld.count += 1
        time.sleep(0.5)
        HelloWorld.count += 1

threads = []
for i in range(5):
    t = HelloWorld()
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(HelloWorld.count)
````