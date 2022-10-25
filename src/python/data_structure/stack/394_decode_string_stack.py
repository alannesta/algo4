"""
https://leetcode.com/problems/decode-string/
"""
from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                tmp = deque()
                digits = deque()
                while stack[-1] != '[':
                    char = stack.pop()
                    tmp.appendleft(char)
                stack.pop()  # pop '['
                # 注意stack为空时抛出的exception
                while stack and '0' <= stack[-1] <= '9':
                    num = stack.pop()
                    digits.appendleft(num)

                num = int("".join(digits))
                flat = num * ("".join(tmp))
                stack.append(flat)

        return "".join(stack)


# s = "3[a]2[bc]"
s1 = "3[a2[c]]"
# s2 = "2[abc]3[cd]ef"
s2 = "10[a]"

print(Solution().decodeString(s2))
