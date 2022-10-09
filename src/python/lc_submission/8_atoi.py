"""
https://leetcode.com/problems/string-to-integer-atoi/

经典方法string to integer
"""
from abc import ABC, abstractmethod

SPACE = ' '
SIGN = ('+', '-')
INT_RANGE = (-2 ** 31, 2 ** 31 - 1)


class FSM:
    def __init__(self, str_input):
        self.str_input = str_input
        self.state: State = InitialState(sign='+', parsed='')

    def update_state(self, char):
        self.state = self.state.update(char)

    def parse(self):
        result = int(self.state.parsed) if self.state.sign == '+' else -int(self.state.parsed)
        if result < INT_RANGE[0]:
            result = INT_RANGE[0]

        if result > INT_RANGE[1]:
            result = INT_RANGE[1]

        return result

    def run(self):
        for char in self.str_input:
            self.update_state(char)

            if isinstance(self.state, ErrorState):
                print('invalid input string: ', self.str_input)
                break

            if isinstance(self.state, FinishedState):
                result = self.parse()
                return result

        if isinstance(self.state, (FinishedState, IntegerState)):
            return self.parse()

        # leetcode edge case, for any other state, return 0
        return 0

class State(ABC):
    def __init__(self, sign, parsed):
        self.sign = sign
        self.parsed = parsed

    @abstractmethod
    def update(self, char) -> 'State':
        ...


class InitialState(State):
    def update(self, char):
        if char == SPACE:
            return self

        if char in SIGN:
            self.sign = char
            return SignState(sign=self.sign, parsed=self.parsed)

        if '0' <= char <= '9':
            self.parsed += char
            return IntegerState(sign=self.sign, parsed=self.parsed)

        # any other char is invalid
        return ErrorState(parsed='0', sign='+')


class SignState(State):
    def update(self, char):
        if '0' <= char <= '9':
            self.parsed += char
            return IntegerState(sign=self.sign, parsed=self.parsed)
        else:
            return ErrorState(sign=self.sign, parsed=self.parsed)


class IntegerState(State):
    def update(self, char):
        if '0' <= char <= '9':
            self.parsed += char
            return IntegerState(sign=self.sign, parsed=self.parsed)
        else:
            return FinishedState(sign=self.sign, parsed=self.parsed)


class FinishedState(State):
    def update(self, char):
        pass


class ErrorState(State):
    def update(self, char):
        pass


kaka = '2' * 40

automation = FSM('words and 987')
print(automation.run())
# print(automation.state.parsed)
