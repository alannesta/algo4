"""
https://leetcode.com/problems/string-to-integer-atoi/

经典方法string to integer

常规解法, switch case
"""

INT_RANGE = (-2 ** 31, 2 ** 31 - 1)


class Solution:
    def myAtoi(self, s: str) -> int:
        parsed = ''
        sign = '+'

        sign_set = False
        parsing = False

        for char in s:
            if '0' <= char <= '9':
                parsed += char
                parsing = True

            elif char == ' ':
                if parsing:
                    break
                if sign_set:
                    return 0

            elif char == '+' or char == '-':
                if parsing:
                    break
                if sign_set:
                    return 0
                else:
                    sign_set = True
                    sign = char
            else:
                # other ASCII characters(words)
                if parsing:
                    # parse finished
                    break
                else:
                    return 0
        try:
            result = int(parsed) if sign == '+' else -int(parsed)
            if result < INT_RANGE[0]:
                result = INT_RANGE[0]

            if result > INT_RANGE[1]:
                result = INT_RANGE[1]

            return result
        except:
            # any other cases (empty input, only the sign etc)
            return 0
