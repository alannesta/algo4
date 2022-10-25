"""
https://leetcode.com/problems/simplify-path/

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        for part in parts:
            if part == '..':
                if stack:
                    stack.pop()
            elif part == '.':
                continue
            elif part == '':
                continue
            else:
                stack.append(part)

        return '/' + "/".join(stack)


# s = '/home//foo/../test'
# s = '/../'
# s = '/home/./test//'
#
# print(Solution().simplifyPath(s))
