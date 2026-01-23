#1176. Diet Plan Performance
#Easy
#
#A dieter consumes calories[i] calories on the i-th day.
#
#Given an integer k, for every consecutive sequence of k days
#(calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k),
#they look at T, the total calories consumed during that sequence of k days:
#    If T < lower, they performed poorly on their diet and lose 1 point;
#    If T > upper, they performed well on their diet and gain 1 point;
#    Otherwise, they performed normally and there is no change in points.
#
#Initially, the dieter has zero points. Return the total number of points the
#dieter has after dieting for calories.length days.
#
#Note that the total points can be negative.
#
#Example 1:
#Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
#Output: 0
#Explanation: Since k = 1, we consider each element of the array separately
#and compare it to lower and upper.
#calories[0] and calories[1] are less than lower so 2 points are lost.
#calories[3] and calories[4] are greater than upper so 2 points are gained.
#
#Example 2:
#Input: calories = [3,2], k = 2, lower = 0, upper = 1
#Output: 1
#Explanation: Since k = 2, we consider subarrays of length 2.
#calories[0] + calories[1] > upper so 1 point is gained.
#
#Example 3:
#Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
#Output: 0
#
#Constraints:
#    1 <= k <= calories.length <= 10^5
#    0 <= calories[i] <= 20000
#    0 <= lower <= upper

from typing import List

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        """Sliding window to track sum of k consecutive days"""
        n = len(calories)
        points = 0

        # Initial window sum
        window_sum = sum(calories[:k])

        # Check first window
        if window_sum < lower:
            points -= 1
        elif window_sum > upper:
            points += 1

        # Slide window
        for i in range(k, n):
            window_sum += calories[i] - calories[i - k]

            if window_sum < lower:
                points -= 1
            elif window_sum > upper:
                points += 1

        return points


class SolutionPrefixSum:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        """Using prefix sum"""
        n = len(calories)

        # Build prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + calories[i]

        points = 0
        for i in range(k, n + 1):
            window_sum = prefix[i] - prefix[i - k]
            if window_sum < lower:
                points -= 1
            elif window_sum > upper:
                points += 1

        return points
