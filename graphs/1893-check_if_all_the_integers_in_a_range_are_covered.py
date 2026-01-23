#1893. Check if All the Integers in a Range Are Covered
#Easy
#
#You are given a 2D integer array ranges and two integers left and right. Each
#ranges[i] = [start_i, end_i] represents an inclusive interval between start_i
#and end_i.
#
#Return true if each integer in the inclusive range [left, right] is covered by
#at least one interval in ranges. Return false otherwise.
#
#An integer x is covered by an interval ranges[i] = [start_i, end_i] if
#start_i <= x <= end_i.
#
#Example 1:
#Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
#Output: true
#
#Example 2:
#Input: ranges = [[1,10],[10,20]], left = 21, right = 21
#Output: false
#
#Constraints:
#    1 <= ranges.length <= 50
#    1 <= start_i <= end_i <= 50
#    1 <= left <= right <= 50

from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        """
        Check each integer in [left, right].
        """
        for x in range(left, right + 1):
            covered = False
            for start, end in ranges:
                if start <= x <= end:
                    covered = True
                    break
            if not covered:
                return False
        return True


class SolutionSet:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        """
        Build set of covered integers.
        """
        covered = set()
        for start, end in ranges:
            for x in range(start, end + 1):
                covered.add(x)

        return all(x in covered for x in range(left, right + 1))


class SolutionLineSweep:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        """
        Line sweep algorithm.
        """
        diff = [0] * 52  # Difference array

        for start, end in ranges:
            diff[start] += 1
            diff[end + 1] -= 1

        # Compute prefix sum to get coverage count
        coverage = 0
        for i in range(1, 51):
            coverage += diff[i]
            if left <= i <= right and coverage == 0:
                return False

        return True


class SolutionSort:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        """
        Sort ranges and check coverage.
        """
        ranges.sort()
        current = left

        for start, end in ranges:
            if start > current:
                break
            if end >= current:
                current = end + 1

            if current > right:
                return True

        return current > right
