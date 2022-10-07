def reverseBits(n: int) -> int:
    mask = 1
    reversed = None
    for i in range(32):
        # bit is 0
        if n & mask == 0:
            if reversed is None:
                reversed = 0
            else:
                reversed = reversed << 1
        else:
            # bit is 1
            if reversed is None:
                reversed = 1
            else:
                reversed = (reversed << 1) + 1
        mask = mask << 1

    print(bin(reversed))
    return reversed


def test(n):
    bin_str = bin(n).replace('0b', '')
    fill = 32 - len(bin_str)
    final = '0' * fill + bin_str
    # print(final)
    reversed = '0b' + final[::-1]
    print(reversed)
    return int(reversed, 2)

print(reverseBits(5))

test(5)