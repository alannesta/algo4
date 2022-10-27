"""
https://leetcode.com/problems/ransom-note/
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = [0] * 26

        for letter in magazine:
            result[ord(letter) - ord('a')] += 1

        for letter in ransomNote:
            result[ord(letter) - ord('a')] -= 1
            if result[ord(letter) - ord('a')] < 0:
                return False

        return True
