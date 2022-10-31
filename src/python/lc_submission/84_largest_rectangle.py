"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
classic problem

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        max_area = heights[0]

        for i in range(len(heights)):
            l = i - 1
            r = i + 1

            while l >= 0:
                if heights[l] >= heights[i]:
                    l -= 1
                else:
                    break

            while r < len(heights):
                if heights[r] >= heights[i]:
                    r += 1
                else:
                    break

            area = heights[i] * ((r - l) - 1)
            max_area = max(max_area, area)

        return max_area

