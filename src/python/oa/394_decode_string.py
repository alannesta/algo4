"""
394. Decode String
https://leetcode.com/problems/decode-string/

"""


class Solution:
    def decodeString(self, s: str) -> str:

        cur_state = StateParse(1, '', [])
        result = ''

        for i in range(len(s)):
            new_state = cur_state.update_state(s[i])
            if isinstance(new_state, StateEnd):
                result += new_state.get_result()
                cur_state = StateParse(1, '', [])
            else:
                cur_state = new_state

        if isinstance(cur_state, StateParse):
            result += cur_state.multiplier * cur_state.string

        return result


class State:
    def __init__(self, multiplier, string):
        self.multiplier = multiplier
        self.string = string

    def update_state(self, char):
        pass


class StateParse(State):
    def __init__(self, multiplier, string, stack):
        super().__init__(multiplier, string)
        self.stack = stack

    def update_state(self, char):
        if '0' <= char <= '9':
            tmp_multi = char
            self.stack.append((self.multiplier, self.string))
            return StateMultiplier(0, '', tmp_multi=tmp_multi, stack=self.stack)

        if 'a' <= char <= 'z':
            self.string = self.string + char
            return StateParse(self.multiplier, self.string, stack=self.stack)

        if char == ']':
            if len(self.stack) == 0:
                return StateEnd(self.multiplier, self.string)
            else:
                prev = self.stack.pop()
                return StateParse(multiplier=prev[0], string=(prev[1] + self.multiplier * self.string),
                                  stack=self.stack)


class StateMultiplier(State):
    def __init__(self, multiplier, string, tmp_multi, stack):
        super().__init__(multiplier, string)
        self.tmp_multi = tmp_multi
        self.stack = stack

    def update_state(self, char):
        if '0' <= char <= '9':
            tmp_multi = self.tmp_multi + char
            return StateMultiplier(self.multiplier, self.string, tmp_multi=tmp_multi, stack=self.stack)
        elif char == '[':
            self.multiplier = int(self.tmp_multi)
            return StateParse(self.multiplier, self.string, stack=self.stack)


class StateEnd(State):
    def update_state(self, char):
        pass

    def get_result(self):
        return self.multiplier * self.string


# s = "3[a]2[bc]"
# s = "2[abc]3[cd]ef"
# s = "3[a2[c]2[b]]"
# s = "3[a2[c2[b]]]"
s = "2[abc]xyc3[z]"

print(Solution().decodeString(s))
