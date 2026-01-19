#739. Daily Temperatures
#Medium
#
#Given an array of integers temperatures represents the daily temperatures,
#return an array answer such that answer[i] is the number of days you have to
#wait after the ith day to get a warmer temperature. If there is no future day
#for which this is possible, keep answer[i] == 0 instead.
#
#Example 1:
#Input: temperatures = [73,74,75,71,69,72,76,73]
#Output: [1,1,4,2,1,1,0,0]
#
#Example 2:
#Input: temperatures = [30,40,50,60]
#Output: [1,1,1,0]
#
#Example 3:
#Input: temperatures = [30,60,90]
#Output: [1,1,0]
#
#Constraints:
#    1 <= temperatures.length <= 10^5
#    30 <= temperatures[i] <= 100

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """Monotonic decreasing stack - O(n) time and space"""
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stack of indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)

        return result


class SolutionReverseIteration:
    """Iterate from right to left"""

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        hottest = 0

        for i in range(n - 1, -1, -1):
            curr = temperatures[i]

            if curr >= hottest:
                hottest = curr
                continue

            days = 1
            while temperatures[i + days] <= curr:
                days += result[i + days]

            result[i] = days

        return result


class SolutionBuckets:
    """Using temperature buckets for O(n) time"""

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        # Map temperature to most recent index
        temp_to_idx = [float('inf')] * 102  # Temps 30-100

        for i in range(n - 1, -1, -1):
            curr = temperatures[i]

            # Find minimum index with higher temperature
            min_idx = float('inf')
            for t in range(curr + 1, 101):
                if temp_to_idx[t] < min_idx:
                    min_idx = temp_to_idx[t]

            if min_idx != float('inf'):
                result[i] = min_idx - i

            temp_to_idx[curr] = i

        return result
