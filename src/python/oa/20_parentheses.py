class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parent_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char in parent_map.keys():
                if not stack:
                    return False
                prev = stack.pop()
                if prev != parent_map[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
