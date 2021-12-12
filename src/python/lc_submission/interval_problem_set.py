"""
https://leetcode.com/problems/interval-list-intersections/

You are given two lists of closed intervals, firstList and secondList,

where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals
is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.
"""
from typing import List


# 986 intersection interval
class Solution986:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0

        results = []

        while i <= len(firstList) - 1 and j <= len(secondList) - 1:
            if self._intersect(firstList[i], secondList[j]):
                results.append([min(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])

                if firstList[i][1] >= secondList[j][1]:
                    j += 1
                else:
                    i += 1

            if firstList[i][1] >= secondList[j][1]:
                j += 1
            else:
                i += 1

        return results

    def _intersect(self, list1, list2):
        if (list1[0] >= list2[0] and list1[1] <= list2[1]) or (list2[0] >= list1[0] and list2[1] <= list1[1]):
            return True

        return False


# 56 merge inerval:
# https://leetcode.com/problems/merge-intervals/
class Solution56:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0

        results = []

        # Essential: sort by start pos of interval
        intervals = sorted(intervals, key=lambda x: x[0])

        while i <= len(intervals) - 2:

            merged = [intervals[i][0], intervals[i][1]]

            j = i + 1

            while j <= len(intervals) - 1 and intervals[j][0] <= merged[1]:
                # merged[0] = intervals[i][0]  # already sorted
                merged[1] = max(merged[1], intervals[j][1])

                j = j + 1

            results.append(merged)

            i = j

            if i == len(intervals) - 1:
                results.append(intervals[-1])

        return results


# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/
class Solution1288:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])

        removed = {}

        for i in range(len(intervals)):
            if i in removed:
                continue
            for j in range(i + 1, len(intervals)):
                if intervals[j][1] <= intervals[i][1]:
                    removed[j] = True

                elif intervals[j][0] == intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    removed[i] = True

        return len(intervals) - len(removed.keys())
