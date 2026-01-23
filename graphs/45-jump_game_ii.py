#45. Jump Game II
#Medium
#
#You are given a 0-indexed array of integers nums of length n. You are initially
#positioned at nums[0].
#
#Each element nums[i] represents the maximum length of a forward jump from index
#i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#    0 <= j <= nums[i] and i + j < n
#
#Return the minimum number of jumps to reach nums[n - 1]. The test cases are
#generated such that you can reach nums[n - 1].
#
#Example 1:
#Input: nums = [2,3,1,1,4]
#Output: 2
#Explanation: The minimum number of jumps to reach the last index is 2.
#Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#Example 2:
#Input: nums = [2,3,0,1,4]
#Output: 2
#
#Constraints:
#    1 <= nums.length <= 10^4
#    0 <= nums[i] <= 1000
#    It's guaranteed that you can reach nums[n - 1].

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy BFS-like approach - O(n) time, O(1) space.
        Track the farthest reachable position at each level.
        """
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            # Reached the end of current level
            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= n - 1:
                    break

        return jumps


class SolutionBFS:
    def jump(self, nums: List[int]) -> int:
        """
        Explicit BFS approach.
        """
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        left = right = 0

        while right < n - 1:
            jumps += 1
            farthest = 0

            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest

        return jumps


class SolutionDP:
    def jump(self, nums: List[int]) -> int:
        """
        Dynamic Programming - O(n^2) time.
        dp[i] = minimum jumps to reach position i.
        """
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[n - 1]


class SolutionBackward:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy backward approach - find leftmost position that can reach target.
        """
        n = len(nums)
        target = n - 1
        jumps = 0

        while target > 0:
            # Find leftmost position that can reach target
            for i in range(target):
                if i + nums[i] >= target:
                    target = i
                    jumps += 1
                    break

        return jumps
