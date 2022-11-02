"""
problem sets that features two pointers and sliding windows
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 392 is sub sequence
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if not s:
            return True
        while j <= len(t) - 1:
            if t[j] == s[i]:
                if i < len(s) - 1:
                    i += 1
                    j += 1
                else:
                    return True
            else:
                j += 1

        return False

    # 3 Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0

        cur_l = 0
        cur_str = ''

        while right <= len(s) - 1:
            left = 0

            cur_str += s[right]

            # update结果的时机
            if len(cur_str) > cur_l:
                cur_l = len(cur_str)

            # end of str, break
            if right == len(s) - 1:
                break

            # peak next elem, 收缩window的时机
            while s[right + 1] in cur_str:
                if cur_str[left] == s[right + 1]:
                    cur_str = cur_str[left + 1:]
                    break
                else:
                    left += 1

            right = right + 1

        return cur_l

    # 3 Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        """
        v2, using hashmap to maintain window, more concise code
        :param s:
        :return:
        """
        left = right = 0

        cur_l = 0

        window = {}

        while right <= len(s) - 1:

            char = s[right]

            if char not in window:
                window[char] = 1
            else:
                window[char] += 1

            right += 1

            while window[char] > 1 and left <= len(s) - 1:
                char_l = s[left]
                window[char_l] -= 1
                left += 1

            # update结果的时机
            cur_l = max(cur_l, right - left)

        return cur_l

    # 76 Minimum Window Substring
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        valid = 0

        cur_min_l = (0, pow(10, 6))

        for char in t:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        left = right = 0

        while right <= len(s) - 1:
            char = s[right]

            if char in need:
                if char in window:
                    window[char] += 1
                else:
                    window[char] = 1

                if need[char] == window[char]:
                    valid += 1

            # 收缩window的时机
            while valid == len(need.keys()):

                # is valid, update result
                s_len = right - left + 1

                # update结果的时机
                if s_len < cur_min_l[1] - cur_min_l[0] + 1:
                    cur_min_l = (left, right)

                to_remove = s[left]

                if to_remove in need:
                    # 易错点1
                    # this check is needed, there may be duplicate chars
                    if need[to_remove] == window[to_remove]:
                        valid -= 1
                    window[to_remove] -= 1
                left += 1

            right += 1

        # 易错点2
        if cur_min_l[1] == pow(10, 6):
            return ""
        return s[cur_min_l[0]: cur_min_l[1] + 1]

    # 567 Permutation in String
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        need = {}
        left = right = 0
        valid = 0

        for char in s1:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        while right <= len(s2) - 1:
            char = s2[right]

            if char in need:
                if char in window:
                    window[char] += 1
                else:
                    window[char] = 1

                if window[char] == need[char]:
                    valid += 1

            # move left window until right + 1 - left == len(s1)
            while valid == len(need.keys()):
                if right + 1 - left == len(s1):
                    return True

                removed = s2[left]

                if removed in need:
                    if window[removed] == need[removed]:
                        valid -= 1

                    window[removed] -= 1

                left += 1

            right += 1

        return False

    # 438 Find All Anagrams in a String
    # exactly the same as #567
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        window = {}
        left = right = 0
        valid = 0

        result = []

        for char in p:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        while right <= len(s) - 1:
            char = s[right]

            if char in need:
                if char in window:
                    window[char] += 1
                else:
                    window[char] = 1

                if window[char] == need[char]:
                    valid += 1

            while valid == len(need.keys()):
                if right + 1 - left == len(p):
                    result.append(left)

                removed = s[left]

                if removed in need:
                    if window[removed] == need[removed]:
                        valid -= 1

                    window[removed] -= 1

                left += 1

            right += 1

        return result

    # 26 remove dup in-place
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        solution1: O(N2), move elems every time a dup is detected
        :param nums:
        :return:
        """
        dups = 0
        i = 0
        while i < len(nums) - 1 - dups:
            j = i + 1
            while nums[j] == nums[i]:
                # handle cases where list contains the same elem
                if dups >= len(nums) - i - 1:
                    break
                dups += 1
                self._move_rest(nums, j, dups)
            i += 1

        return len(nums) - dups

    def _move_rest(self, nums, idx, dups):
        # reduce number of elems that needs to move
        for i in range(idx, len(nums) - dups):
            nums[i] = nums[i + 1]

    # 26 remove dup in-place
    def removeDuplicates_v2(self, nums: List[int]) -> int:
        """
        remove dups using slow/fast pointers
        :param nums:
        :return:
        """
        slow = fast = 0

        while fast <= len(nums) - 1:
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1

        return slow + 1

    # 80 remove dups II
    def removeDuplicatesII(self, nums: List[int]) -> int:
        """
        !this does not meet the requirement as O(1) space complexity
        :param nums:
        :return:
        """
        if not nums:
            return 0
        look_up = {
            nums[0]: 1
        }
        slow = 0
        fast = 1

        while fast <= len(nums) - 1:
            if nums[fast] == nums[slow]:
                if nums[fast] not in look_up:
                    look_up[nums[fast]] = 1
                else:
                    look_up[nums[fast]] = look_up[nums[fast]] + 1
                    if look_up[nums[fast]] <= 2:
                        # edge case [12]
                        if slow < len(nums) - 1:
                            slow += 1
                            nums[slow] = nums[fast]
                    fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1

        return slow + 1

    # 27 remove element inplace
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0

        while fast <= len(nums) - 1:
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1  # 这个细节要注意, 和removeDuplicates_v2里slow pointer增加的文职不同
                fast += 1

        return slow  # not slow + 1

    # 83 remove dups from linked list
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        fast = slow = head

        while fast:
            if fast.val == slow.val:
                next_n = fast.next
                slow.next = next_n
                fast = next_n
            else:
                slow = slow.next
                fast = fast.next

        return head

    # 283 move zeros inplace
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_cnt = 0
        slow = fast = 0

        while fast <= len(nums) - 1:
            if nums[fast] == 0:
                z_cnt += 1
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1

        # set the elems to 0
        for i in range(1, z_cnt + 1):
            nums[-i] = 0

    # 316, 1081 remove duplicate letters and with smallest lexicographical order
    # 解题思路: https://www.youtube.com/watch?v=-zmul9EyKng&ab_channel=LeetCode%E5%8A%9B%E6%89%A3
    def removeDuplicateLetters(self, s: str) -> str:
        look_up = {}
        included = {}

        result = []

        for char in s:
            if char in look_up:
                look_up[char] += 1
            else:
                look_up[char] = 1

        for char in s:
            if char in included:
                look_up[char] -= 1
                continue

            while result:
                last_char = result[-1]
                if char < last_char and look_up[last_char] > 0:
                    included.pop(last_char)
                    result.pop()
                else:
                    break

            result.append(char)
            included[char] = True
            look_up[char] -= 1

        return ''.join(result)

    # 209: https://leetcode.com/problems/minimum-size-subarray-sum/
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        cur_sum = 0
        min_length = 2 ** 31 - 1

        while right < len(nums):
            cur_sum += nums[right]

            if cur_sum >= target:
                min_length = min(min_length, right - left + 1)

                while left < right:
                    cur_sum -= nums[left]
                    left += 1
                    if cur_sum >= target:
                        min_length = min(min_length, right - left + 1)
                    else:
                        break
            right += 1

        if min_length == 2 ** 31 - 1:
            min_length = 0

        return min_length
