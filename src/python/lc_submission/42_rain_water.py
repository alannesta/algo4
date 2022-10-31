"""
https://leetcode.com/problems/trapping-rain-water/
leetcode经典系列

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
"""

from typing import List


# brute force, O(n2)
class Solution:
    def trap(self, height: List[int]) -> int:
        water_sum = 0
        for i in range(len(height)):
            if height[0:i]:
                l_max = max(height[0:i])
            else:
                l_max = 0

            if height[i + 1:]:
                r_max = max(height[i + 1:])
            else:
                r_max = 0

            water = max(min(l_max, r_max) - height[i], 0)
            water_sum += water

        return water_sum


# optimization based on Sol1, still exceed time limit
class Solution2:
    def trap(self, height: List[int]) -> int:
        water_sum = 0
        l_max = 0
        r_max = 0
        if len(height) <= 1:
            return water_sum
        for i in range(len(height)):
            if i == 0:
                # init
                r_max = height[1]
                continue
            # no need to check last elem
            if i == len(height) - 1:
                continue

            l_max = max(l_max, height[i - 1])

            # this is where that takes time
            if r_max == height[i]:
                r_max = max(height[i + 1:])

            water = max(min(l_max, r_max) - height[i], 0)
            water_sum += water

        return water_sum
