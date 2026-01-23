#55. Jump Game
#Medium
#
#You are given an integer array nums. You are initially positioned at the array's
#first index, and each element in the array represents your maximum jump length
#at that position.
#
#Return true if you can reach the last index, or false otherwise.
#
#Example 1:
#Input: nums = [2,3,1,1,4]
#Output: true
#Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#Example 2:
#Input: nums = [3,2,1,0,4]
#Output: false
#Explanation: You will always arrive at index 3 no matter what. Its maximum jump
#length is 0, which makes it impossible to reach the last index.
#
#Constraints:
#    1 <= nums.length <= 10^4
#    0 <= nums[i] <= 10^5

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy - track furthest reachable index.
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= len(nums) - 1:
                return True

        return True


class SolutionBackward:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy backward - find leftmost position that can reach end.
        """
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


class SolutionDP:
    def canJump(self, nums: List[int]) -> bool:
        """
        Dynamic Programming - O(n^2).
        dp[i] = True if we can reach position i.
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for j in range(1, nums[i] + 1):
                    if i + j < n:
                        dp[i + j] = True

        return dp[n - 1]


class SolutionDPOptimized:
    def canJump(self, nums: List[int]) -> bool:
        """
        DP with early termination.
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            end = min(i + nums[i], n - 1)
            for j in range(i + 1, end + 1):
                dp[j] = True

            if dp[n - 1]:
                return True

        return dp[n - 1]
