"""
python:
https://docs.python.org/3/reference/lexical_analysis.html#integer-literals


>>> kaka = 0b000010
>>> int(kaka)
2
>>> kaka = 0b11
>>> int(kaka)
3
>>> bin(3)
'0b11'
>>> bin(47)
'0b101111'
>>> type(bin(47))
<class 'str'>
>>> int(bin(47), 2)
47

>>> kaka = 0b101111
>>> type(kaka)
<class 'int'>

ord() and chr() for ASCII code point(int) <--> char conversion
https://docs.python.org/3/library/functions.html#ord
ord: return an integer representing the Unicode code point of that character
chr: Return the string representing a character whose Unicode code point is the integer i.

>>> chr(kaka)
'/'
>>> ord('a')
97
>>> bin(ord('a'))
'0b1100001'
>>>

32 bit int

>>> bin(2**31 - 1)
'0b1111111111111111111111111111111'

# overflow
>>> bin(2**31)
'0b10000000000000000000000000000000'

check if a certain bit is set(by pos):


"""
