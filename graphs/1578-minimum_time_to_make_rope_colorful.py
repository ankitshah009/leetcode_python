#1578. Minimum Time to Make Rope Colorful
#Medium
#
#Alice has n balloons arranged on a rope. You are given a 0-indexed string colors
#where colors[i] is the color of the ith balloon.
#
#Alice wants the rope to be colorful. She does not want two consecutive balloons
#to be of the same color, so she asks Bob for help. Bob can remove some balloons
#from the rope to make it colorful. You are given a 0-indexed integer array
#neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove
#the ith balloon from the rope.
#
#Return the minimum time Bob needs to make the rope colorful.
#
#Example 1:
#Input: colors = "abaac", neededTime = [1,2,3,4,5]
#Output: 3
#Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
#Bob can remove the blue balloon at index 2. This takes 3 seconds.
#There are no longer two consecutive balloons of the same color. Total time = 3.
#
#Example 2:
#Input: colors = "abc", neededTime = [1,2,3]
#Output: 0
#Explanation: The rope is already colorful. Bob does not need to remove any balloons.
#
#Example 3:
#Input: colors = "aabaa", neededTime = [1,2,3,4,1]
#Output: 2
#Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes
#1 second to remove. Total time = 1 + 1 = 2.
#
#Constraints:
#    n == colors.length == neededTime.length
#    1 <= n <= 10^5
#    1 <= neededTime[i] <= 10^4
#    colors contains only lowercase English letters.

from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        For each group of consecutive same colors, keep the balloon with
        maximum time and remove all others.
        """
        total_cost = 0
        i = 0
        n = len(colors)

        while i < n:
            # Find group of same color
            j = i
            group_sum = 0
            group_max = 0

            while j < n and colors[j] == colors[i]:
                group_sum += neededTime[j]
                group_max = max(group_max, neededTime[j])
                j += 1

            # If group has more than one balloon, remove all except max
            if j - i > 1:
                total_cost += group_sum - group_max

            i = j

        return total_cost


class SolutionOnePass:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Single pass: track previous color and max time in current group.
        """
        total = 0
        prev_color = ''
        prev_max = 0

        for i, c in enumerate(colors):
            if c == prev_color:
                # Same group: add min of current and previous max
                total += min(prev_max, neededTime[i])
                prev_max = max(prev_max, neededTime[i])
            else:
                # New group
                prev_color = c
                prev_max = neededTime[i]

        return total


class SolutionGroupBy:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Using itertools.groupby to identify groups.
        """
        from itertools import groupby

        total = 0
        idx = 0

        for color, group in groupby(colors):
            # Get times for this group
            times = []
            for _ in group:
                times.append(neededTime[idx])
                idx += 1

            # Keep max, remove rest
            if len(times) > 1:
                total += sum(times) - max(times)

        return total


class SolutionSimple:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Simple iteration comparing adjacent elements.
        """
        total = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # Remove the cheaper one
                total += min(neededTime[i], neededTime[i - 1])
                # Keep the more expensive for next comparison
                neededTime[i] = max(neededTime[i], neededTime[i - 1])

        return total
