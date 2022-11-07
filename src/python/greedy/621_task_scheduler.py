"""
https://leetcode.com/problems/task-scheduler/

"""

from typing import List
from collections import defaultdict, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        if n == 0:
            return len(tasks)

        task_pool = defaultdict(int)
        max_heap = []
        schedule = []
        next_valid = None

        for task in tasks:
            task_pool[task] -= 1

        for task, reverse_count in task_pool.items():
            # (task_count, task_key)
            # python heapq is a min heap, we reverse the count to do the trick here
            # so that task with most occurences is on top of the min heap
            heapq.heappush(max_heap, [task_pool[task], task])

        while True:
            cur_task = max_heap[0]  # peek

            if cur_task[1] == next_valid or cur_task[1] not in schedule[-n:]:
                schedule.append(cur_task[1])
                t = heapq.heappop(max_heap)
                t[0] += 1
                if t[0] != 0:
                    # push back
                    heapq.heappush(max_heap, t)
            else:
                # still in cool down mode, process next candidate in heap
                poped = []
                found = False
                while not found:
                    if not max_heap:
                        schedule.append("idle")
                        found = True
                        continue
                    cur_task = heapq.heappop(max_heap)
                    if cur_task[1] in schedule[-n:]:
                        poped.append(cur_task)
                        continue
                    else:
                        found = True
                        schedule.append(cur_task[1])
                        cur_task[0] += 1
                        if cur_task[0] != 0:
                            # push back
                            heapq.heappush(max_heap, cur_task)

                while poped:
                    # put back
                    heapq.heappush(max_heap, poped.pop())

            if not max_heap:
                break

        print(schedule)
        return len(schedule)

    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     task_pool = defaultdict(int)
    #
    #     if n == 0:
    #         return len(tasks)
    #     schedule = []
    #
    #     most_task_count = 0
    #     start_task = None
    #     for task in tasks:
    #         task_pool[task] += 1
    #         if task_pool[task] >= most_task_count:
    #             most_task_count = task_pool[task]
    #             start_task = task
    #
    #     distinct_tasks = list(task_pool.keys())
    #
    #     while True:
    #         # start with task with most count
    #         if not schedule:
    #             schedule.append(start_task)
    #             task_pool[start_task] -= 1
    #             if task_pool[start_task] == 0:
    #                 del task_pool[start_task]
    #                 distinct_tasks.remove(start_task)
    #             continue
    #
    #         # prev_n_task_key = schedule[-(n + 1)]
    #         unpickable = schedule[-n:]
    #
    #         found_task = False
    #         for key in distinct_tasks:
    #             if key not in unpickable:
    #                 found_task = True
    #                 schedule.append(key)
    #                 task_pool[key] -= 1
    #                 if task_pool[key] == 0:
    #                     del task_pool[key]
    #                     distinct_tasks.remove(key)
    #                 break
    #         if not found_task:
    #             schedule.append("idle")
    #
    #         if not distinct_tasks:
    #             break
    #
    #     print(schedule)
    #
    #     return len(schedule)
