"""
与概率与随机抽样相关的系列问题
"""
import random
from typing import List


# 380: https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/
# 此题有单独的submission file

# 710: https://leetcode.com/problems/random-pick-with-blacklist/

class Solution710:
    """
    当n是很大的值时, 这个解法会超时
    """

    # def __init__(self, n: int, blacklist: List[int]):
    #     self.whitelist = []
    #     for i in range(n):
    #         if i not in blacklist:
    #             self.whitelist.append(i)
    #
    # def pick(self) -> int:
    #     return self.whitelist[random.randint(0, len(self.whitelist) - 1)]

    # 这个解法之需要遍历black list, 将black list的值swap到数组的尾部
    # 这样求随机数时之需要从前 n - len(blist)个元素里抽取
    def __init__(self, n: int, blacklist: List[int]):
        self.total_len = n
        self.blacklist_len = len(blacklist)
        # self.vals = list(range(n))

        self.look_up = {}
        for i in blacklist:
            self.look_up[i] = True

        last_idx = n - 1

        for i in blacklist:
            if i >= self.total_len - self.blacklist_len:
                continue

            elem = last_idx
            # map the black list element to a valid element in the later/invalid part of the list
            while elem in self.look_up:
                last_idx -= 1
                elem = last_idx

            self.look_up[i] = last_idx
            last_idx -= 1

    def pick(self) -> int:

        idx = random.randint(0, self.total_len - self.blacklist_len - 1)

        if idx in self.look_up:
            return self.look_up[idx]
        else:
            return idx
