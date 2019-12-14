#deque起到FIFO的作用
from collections import deque

de=deque((i for i in range(10)),maxlen=10)

de.rotate(3) #向右错位，自身发生改变.可以尝试自己制作一个deque class

de.append(11)
de.append([11,12,13])
de.extend((i for i in (13,14,15)))
de.extendleft((i for i in (4,3,2)))#注意添加的顺序
de.pop() #社区最后一个元素，但不改变maxlen

#deque的常见操作见p56

#请关注其它形式的队列操作，它们很重要
'''
queue
Provides the synchronized (i.e. thread-safe) classes Queue, LifoQueue and Priori
tyQueue. These are used for safe communication between threads. All three classes
can be bounded by providing a maxsize argument greater than 0 to the constructor.
However, they don’t discard items to make room as deque does. Instead, when the
queue is full the insertion of a new item blocks — i.e. it waits until some other thread
56 | Chapter 2: An array of sequencesmakes room by taking an item from the queue, which is useful to throttle the num‐
ber of live threads.

multiprocessing
Implements its own bounded Queue, very similar to queue.Queue but designed for
inter-process communication. There is also has a specialized multiprocess
ing.JoinableQueue for easier task management.

asyncio
Newly added to Python 3.4, asyncio provides Queue, LifoQueue, PriorityQueue
and JoinableQueue with APIs inspired by the classes in queue and multiprocess
ing, but adapted for managing tasks in asynchronous programming.

heapq
In contrast to the previous three modules, heapq does not implement a queue class,
but provides functions like heappush and heappop that let you use a mutable se‐
quence as a heap queue or priority queue.
'''