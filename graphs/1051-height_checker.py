#1051. Height Checker
#Easy
#
#A school is trying to take an annual photo of all the students. The students
#are asked to stand in a single file line in non-decreasing order by height.
#Let this ordering be represented by the integer array expected where
#expected[i] is the expected height of the ith student in line.
#
#You are given an integer array heights representing the current order that
#the students are standing in. Each heights[i] is the height of the ith
#student in line (0-indexed).
#
#Return the number of indices where heights[i] != expected[i].
#
#Example 1:
#Input: heights = [1,1,4,2,1,3]
#Output: 3
#Explanation:
#heights:  [1,1,4,2,1,3]
#expected: [1,1,1,2,3,4]
#Indices 2, 4, and 5 do not match.
#
#Example 2:
#Input: heights = [5,1,2,3,4]
#Output: 5
#Explanation: All indices do not match.
#
#Example 3:
#Input: heights = [1,2,3,4,5]
#Output: 0
#Explanation: All indices match.
#
#Constraints:
#    1 <= heights.length <= 100
#    1 <= heights[i] <= 100

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Sort and compare with original.
        """
        expected = sorted(heights)
        return sum(h != e for h, e in zip(heights, expected))


class SolutionCountingSort:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Counting sort - O(n + k) where k is range of heights.
        """
        count = [0] * 101

        for h in heights:
            count[h] += 1

        result = 0
        expected_idx = 1

        for h in heights:
            # Find next expected height
            while count[expected_idx] == 0:
                expected_idx += 1

            if h != expected_idx:
                result += 1

            count[expected_idx] -= 1

        return result


class SolutionOnePass:
    def heightChecker(self, heights: List[int]) -> int:
        """Alternative counting sort implementation"""
        count = [0] * 101
        for h in heights:
            count[h] += 1

        # Build expected array using prefix counts
        result = 0
        j = 0

        for h in heights:
            while count[j] == 0:
                j += 1

            if h != j:
                result += 1

            count[j] -= 1

        return result
