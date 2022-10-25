"""
https://leetcode.com/problems/implement-queue-using-stacks/
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
"""


class MyQueue:

    def __init__(self):
        self.queue = []

        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if len(self.out_stack) == 0:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        res = self.out_stack.pop()

        return res

    def peek(self) -> int:
        res = self.pop()
        self.out_stack.append(res)
        return res

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


from collections import deque


class MyStack:

    def __init__(self):
        self.in_queue = deque()
        self.out_queue = deque()

    def push(self, x: int) -> None:
        self.in_queue.appendleft(x)

    def pop(self) -> int:
        result = None
        if self.in_queue:
            while self.in_queue:
                poped = self.in_queue.pop()
                if len(self.in_queue) == 0:
                    result = poped
                else:
                    self.out_queue.appendleft(poped)

        else:
            while self.out_queue:
                poped = self.out_queue.pop()
                if len(self.out_queue) == 0:
                    result = poped
                else:
                    self.in_queue.appendleft(poped)

        return result

    def top(self) -> int:
        res = self.pop()
        self.in_queue.appendleft(res)
        return res

    def empty(self) -> bool:
        return (not self.in_queue) and (not self.out_queue)


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.pop())
