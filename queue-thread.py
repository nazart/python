import queue
import threading
import time
import numpy as np
def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()

q = queue.Queue()
threads = []
num_worker_threads = 10
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
def do_work(item):
	print('empieza el item', item)
	a = np.random.randint(0,20)
	time.sleep(a)
	print('esperando ', a, ' Segundos en el item numero ', item)
	print('finalizo', item)

def source():
	return [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

for item in source():
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()