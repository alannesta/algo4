"""
Implmentation using heapq module
examples from python official documentation
"""
import heapq
from collections import namedtuple
from dataclasses import dataclass, field
import itertools

PrioritizedItem = namedtuple("task", ['priority', 'item'])


pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


item1 = PrioritizedItem(priority=10, item="lol")
item2 = PrioritizedItem(priority=5, item="lol")
item3 = PrioritizedItem(priority=1, item="lol")
item4 = PrioritizedItem(priority=6, item="lol")
item5 = PrioritizedItem(priority=3, item="lol")

add_task(item1, item1.priority)
add_task(item2, item2.priority)
add_task(item3, item3.priority)
add_task(item4, item4.priority)
add_task(item5, item5.priority)

print(pop_task())
print(pop_task())
print(pop_task())
print(pop_task())
print(pop_task())