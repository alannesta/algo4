"""
https://leetcode.com/problems/first-unique-character-in-a-string/

https://www.1point3acres.com/bbs/thread-937337-1-1.html

坑:
>>> isinstance(False, int)
True
>>> False == 0
True
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        look_up = {}

        for idx, char in enumerate(s):
            if char in look_up:
                look_up[char] = 'Dup'
            else:
                look_up[char] = idx

        for char in look_up.keys():
            # 这道题的坑在于对idx为0时的check, python里 False == 0
            if look_up[char] != 'Dup':
                return look_up[char]
        return -1


test = "loveleetcode"

print(Solution().firstUniqChar(test))