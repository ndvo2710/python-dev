from multiprocessing import Process, Queue,  Lock, Value
import requests, time, queue

start = time.time()

count = 100
num = 2
url = 'http://127.0.0.1'

lock = Lock()
q = Queue()
processes = []
result = {}

def get_content(url):
    while True:
        try:
            q.get(block=False)
        except queue.Empty:
            break
        try:
            r = requests.get(url)
        except:
            result["error"] = result.setdefault("error", 0) + 1
        else:
            result[r.status_code] = result.setdefault(r.status_code, 0) + 1
    for item in result:
        print("status_code[%s]: %d" % (item, result.get(item)))

for i in range(count):
    q.put(i)

for i in range(num):
    p = Process(target=get_content, args=(url,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

end = time.time()
t = end - start
print("time %d" %  t)
