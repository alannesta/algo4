"""
priority queue implementation using a dict + multiple queues
reference: scrapy priority queue
"""
import random

from collections import deque
from typing import Any


class PriorityQueue:
    """
    Priority Queue
    Tasks priority order is natural integer order
    """

    def __init__(self):
        self.pq = {}
        self.current_priority = 0

    def add_task(self, task: Any, priority: int = 0):
        sub_queue = self.pq.get(priority, None)
        if not sub_queue:
            sub_queue = deque()
            sub_queue.appendleft(task)
            self.pq[priority] = sub_queue
        else:
            sub_queue.appendleft(task)

        if priority > self.current_priority:
            self.current_priority = priority

    def pop_task(self):
        sub_queue = self.pq.get(self.current_priority, None)
        if not sub_queue:
            return None

        task = sub_queue.pop()
        if len(sub_queue) == 0:
            self.pq.pop(self.current_priority, None)
            if self.pq.keys():
                self.current_priority = max(self.pq.keys())
            else:
                self.current_priority = 0

        return task

    def peek(self):
        sub_queue = self.pq.get(self.current_priority, None)
        if not sub_queue:
            return None

        print('next task: ', sub_queue[-1])

pq = PriorityQueue()

for i in range(1, 5):
    p = random.randint(0, 10)
    print('add task with priority: ', p)
    pq.add_task("dummy_" + str(p), p)

print(pq.pop_task())
pq.peek()
print(pq.pop_task())
pq.peek()
print(pq.pop_task())
pq.peek()
print(pq.pop_task())
pq.peek()
print(pq.pop_task())
pq.peek()
print(pq.pop_task())

