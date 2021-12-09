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

            elif nums[mid] > target:
                right = mid - 1

            elif nums[mid] < target:
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

        lower = self._search_lower_bound(nums, target)
        if lower == -1:
            return [-1, -1]
        upper = self._search_upper_bound(nums, target)

        # using bisect api
        # lower = bisect.bisect_left(nums, target)
        # upper = bisect.bisect_right(nums, target)
        # if lower == 0 or upper == len(nums):
        #     upper = lower = -1

        return [lower, upper]

    # 双闭区间模版
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

    # 左闭右开区间模版: 搜索右边界
    def _search_upper_bound(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid

            elif nums[mid] == target:
                # Essential: 收缩左指针
                left = mid + 1

        if left == 0:
            return -1

        if nums[left - 1] == target:
            return left - 1
        else:
            return -1

    # 左闭右开区间模版: 搜索左边界
    def _search_lower_bound(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid

            elif nums[mid] == target:
                # Essential: 收缩右指针
                right = mid

        if left == len(nums):
            return - 1

        if nums[left] == target:
            return left
        else:
            return -1


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


# 33 search in rotate array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution33:
    def search(self, nums: List[int], target: int) -> int:
        # step 1: search for pivot point
        p_target = nums[-1]
        if p_target == target:
            return len(nums) - 1

        pivot = self.findMin(nums)

        res = self.bsearch(nums, 0, pivot, target)
        if res != -1:
            return res

        return self.bsearch(nums, pivot, len(nums), target)

    def bsearch(self, nums, left, right, target):

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid

            elif nums[mid] < target:
                left = mid + 1

        return -1

    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left


# 153:https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# bsearch with no target...
class Solution153:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
