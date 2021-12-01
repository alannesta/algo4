"""
binary search related questions
"""
from typing import List
import math
import bisect


# 704: https://leetcode.com/problems/binary-search/
class Solution704:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # mid = (right + left) // 2  # may cause int overflow, not really an issue in python
            mid = left + (right - left) // 2  # 向下取整
            # mid = math.ceil((right + left) / 2) # 向上取整

            if nums[mid] == target:
                return mid

            elif nums[mid] >= target:
                right = mid - 1

            elif nums[mid] <= target:
                left = mid + 1

        return -1


# 35: search insertion position: (Attention: distinct element!!)
class Solution35:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # mid = (right + left) // 2  # may cause int overflow, not really an issue in python
            mid = left + (right - left) // 2  # 向下取整
            # mid = math.ceil((right + left) / 2) # 向上取整

            if nums[mid] == target:
                return mid

            elif nums[mid] >= target:
                right = mid - 1

            elif nums[mid] <= target:
                left = mid + 1

        # at this point(exit while loop), left = right + 1
        # 参考bisect.bisect
        return left


# 34: find position of elements
class Solution34:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # lower = self._search_bound(nums, target, type='lower')
        # upper = self._search_bound(nums, target, type='upper')
        lower = bisect.bisect_left(nums, target)
        upper = bisect.bisect_right(nums, target)
        if lower == 0 or upper == len(nums):
            upper = lower = -1

        return [lower, upper]

    def _search_bound(self, nums, target, type) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # 向下取整

            if nums[mid] == target:
                # Essential: 夹逼法
                if type == 'lower':
                    right = mid - 1
                if type == 'upper':
                    left = mid + 1

            elif nums[mid] >= target:
                right = mid - 1

            elif nums[mid] <= target:
                left = mid + 1

        if type == 'upper':
            # Essential: check if target does not exist in list
            if right < 0 or nums[right] != target:
                return -1

        if type == 'lower':
            # Essential: check if target does not exist in list
            if left > len(nums) - 1 or nums[left] != target:
                return -1

        # Essential: return left or right?
        if type == 'lower':
            # return left because right would be minus 1
            return left
        if type == 'upper':
            # return right because left would be plus 1
            return right


# 2089: https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution2089:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        left = 0
        right = len(nums) - 1

        pos = -1

        while left <= right:
            mid = left + (right - left) // 2  # 向下取整

            if nums[mid] == target:
                pos = mid
                break

            elif nums[mid] >= target:
                right = mid - 1

            elif nums[mid] <= target:
                left = mid + 1

        if pos == -1:
            return []

        left = right = pos

        # another way to search instead of search for upper and lower bounds (compare to #34)
        while left >= 0:
            print('loop')
            if nums[left] == nums[pos]:
                left -= 1
            else:
                break

        while right <= len(nums) - 1:
            if nums[right] == nums[pos]:
                right += 1
            else:
                break

        return list(range(left + 1, right))
