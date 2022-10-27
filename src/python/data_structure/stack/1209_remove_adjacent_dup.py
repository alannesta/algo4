"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

"""


# 超时
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif stack[-1] == char:
                # time complexity is high when k is large and char count is just below k
                if not self.clear_stack(stack, k, char):
                    stack.append(char)
            else:
                stack.append(char)

        return "".join(stack)

    def clear_stack(self, stack, k, char):
        poped = []
        cleared = True
        while k > 1:
            if not stack:
                # restore stack
                while poped:
                    stack.append(poped.pop())
                cleared = False
                break

            if stack[-1] == char:
                elem = stack.pop()
                poped.append(elem)
                k -= 1
            else:
                # restore stack
                while poped:
                    stack.append(poped.pop())
                cleared = False
                break

        return cleared


class Solution2:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append([char, 1])
            elif stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        result = ''
        for item in stack:
            result += item[0] * item[1]
        return result


s = "deeedbbcccbdaa"
# s = "abbaca"
# s = "pbbcggttciiippooaais"
print(Solution2().removeDuplicates(s, 3))
