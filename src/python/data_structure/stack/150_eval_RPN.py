"""
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9


Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
"""
from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ('+', '-', '*', '/')
        stack = []
        for token in tokens:
            if token in operators:
                op = token
                num2 = stack.pop()
                num1 = stack.pop()
                if op == '+':
                    stack.append(num1 + num2)
                elif op == '-':
                    stack.append(num1 - num2)
                elif op == '*':
                    stack.append(num1 * num2)
                elif op == '/':
                    # stack.append(num1 // num2)
                    result = num1 / num2
                    if result > 0:
                        stack.append(math.floor(result))
                    else:
                        stack.append(math.ceil(result))
            else:
                stack.append(int(token))

        return stack.pop()

