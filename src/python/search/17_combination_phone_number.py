"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.key_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result
        self.traverse(digits, cur_path='')

        return self.result

    def traverse(self, digits, cur_path):
        if len(digits) == 0:
            self.result.append(cur_path)
            return

        """
        易错点:
        这里我最初写作:
        for digit in digits:
            letters = self.key_map[digits]
            for char in letters:
                cur_path += char
                self.traverse(digits[1:], cur_path)
                cur_path = cur_path[:-1]
                
        因为递归的原因, 下一次traverse已经处理了后续的digit, 所以这里不需要for digit in digits!
        这类组合问题的递归脑子里要有画面, 代码描述了一个step by step的过程, 一般不需要2个for循环的嵌套
        """
        letters = self.key_map[digits[0]]
        for char in letters:
            cur_path += char
            self.traverse(digits[1:], cur_path)
            cur_path = cur_path[:-1]
