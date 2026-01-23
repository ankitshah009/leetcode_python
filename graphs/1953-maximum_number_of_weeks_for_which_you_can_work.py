#1953. Maximum Number of Weeks for Which You Can Work
#Medium
#
#There are n projects numbered from 0 to n - 1. You are given an integer array
#milestones where each milestones[i] denotes the number of milestones the ith
#project has.
#
#You can work on the projects following these two rules:
#- Every week, you will finish exactly one milestone of one project. You must
#  work every week.
#- You cannot work on two milestones from the same project for two consecutive
#  weeks.
#
#Once all the milestones of all the projects are finished, or if the only
#milestones that can be worked on will cause you to violate the above rules,
#you will stop working. Note that you may not be able to finish every project's
#milestones due to these constraints.
#
#Return the maximum number of weeks you would be able to work on the projects
#without violating the rules mentioned above.
#
#Example 1:
#Input: milestones = [1,2,3]
#Output: 6
#
#Example 2:
#Input: milestones = [5,2,1]
#Output: 7
#
#Constraints:
#    n == milestones.length
#    1 <= n <= 10^5
#    1 <= milestones[i] <= 10^9

from typing import List

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        """
        Greedy: if max project has more than sum of others + 1, we're limited.
        Otherwise, we can complete everything.
        """
        total = sum(milestones)
        max_milestones = max(milestones)
        rest = total - max_milestones

        # If max can be interleaved with others
        if max_milestones <= rest + 1:
            return total

        # Otherwise, limited by: rest + (rest + 1) = 2 * rest + 1
        return 2 * rest + 1


class SolutionExplained:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        """
        Key insight:
        - If we have projects [a, b, c] with total T and max M
        - If M <= T - M + 1 (i.e., M <= rest + 1), we can do all T weeks
        - Otherwise, max project is too large, answer is 2 * (T - M) + 1
        """
        total = sum(milestones)
        max_m = max(milestones)

        # Can max project fit between others?
        if max_m <= total - max_m + 1:
            return total

        # Max project too large
        return 2 * (total - max_m) + 1
