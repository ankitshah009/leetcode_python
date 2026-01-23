#1124. Longest Well-Performing Interval
#Medium
#
#We are given hours, a list of the number of hours worked per day for a
#given employee.
#
#A day is considered to be a tiring day if and only if the number of hours
#worked is (strictly) greater than 8.
#
#A well-performing interval is an interval of days for which the number of
#tiring days is strictly larger than the number of non-tiring days.
#
#Return the length of the longest well-performing interval.
#
#Example 1:
#Input: hours = [9,9,6,0,6,6,9]
#Output: 3
#Explanation: The longest well-performing interval is [9,9,6].
#
#Example 2:
#Input: hours = [6,6,6]
#Output: 0
#
#Constraints:
#    1 <= hours.length <= 10^4
#    0 <= hours[i] <= 16

from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        """
        Convert to +1/-1 for tiring/non-tiring days.
        Find longest subarray with sum > 0.
        Use prefix sum and hash map.
        """
        n = len(hours)
        prefix = 0
        result = 0
        first_occurrence = {}  # prefix_sum -> first index

        for i in range(n):
            prefix += 1 if hours[i] > 8 else -1

            if prefix > 0:
                result = i + 1
            else:
                # Look for prefix - 1 (then subarray sum is 1)
                if prefix - 1 in first_occurrence:
                    result = max(result, i - first_occurrence[prefix - 1])

                if prefix not in first_occurrence:
                    first_occurrence[prefix] = i

        return result


class SolutionMonoStack:
    def longestWPI(self, hours: List[int]) -> int:
        """
        Monotonic stack approach for longest subarray with positive sum.
        """
        n = len(hours)
        prefix = [0]
        for h in hours:
            prefix.append(prefix[-1] + (1 if h > 8 else -1))

        # Monotonic decreasing stack of indices
        stack = []
        for i in range(n + 1):
            if not stack or prefix[i] < prefix[stack[-1]]:
                stack.append(i)

        result = 0

        # Iterate from right to find longest positive subarray
        for j in range(n, -1, -1):
            while stack and prefix[j] > prefix[stack[-1]]:
                result = max(result, j - stack.pop())

        return result


class SolutionBruteForce:
    def longestWPI(self, hours: List[int]) -> int:
        """O(n^2) brute force for verification"""
        n = len(hours)
        result = 0

        for i in range(n):
            tiring = 0
            for j in range(i, n):
                if hours[j] > 8:
                    tiring += 1
                non_tiring = j - i + 1 - tiring
                if tiring > non_tiring:
                    result = max(result, j - i + 1)

        return result
