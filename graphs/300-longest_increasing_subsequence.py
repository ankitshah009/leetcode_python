#300. Longest Increasing Subsequence
#Medium
#
#Given an integer array nums, return the length of the longest strictly
#increasing subsequence.
#
#Example 1:
#Input: nums = [10,9,2,5,3,7,101,18]
#Output: 4
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
#length is 4.
#
#Example 2:
#Input: nums = [0,1,0,3,2,3]
#Output: 4
#
#Example 3:
#Input: nums = [7,7,7,7,7,7,7]
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 2500
#    -10^4 <= nums[i] <= 10^4
#
#Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
#complexity?

from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Binary search approach - O(n log n).
        Maintain a sorted array where tails[i] is the smallest tail element
        for LIS of length i+1.
        """
        tails = []

        for num in nums:
            # Find position to insert/replace
            pos = bisect.bisect_left(tails, num)

            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)


class SolutionDP:
    """Dynamic programming - O(n^2)"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # dp[i] = LIS ending at index i

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class SolutionMemo:
    """Memoization approach"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def lis_ending_at(i):
            max_len = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, 1 + lis_ending_at(j))
            return max_len

        return max(lis_ending_at(i) for i in range(len(nums)))


class SolutionPatience:
    """Patience sorting visualization"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = []

        for num in nums:
            # Binary search for the leftmost pile where we can place this card
            left, right = 0, len(piles)

            while left < right:
                mid = (left + right) // 2
                if piles[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(piles):
                piles.append(num)
            else:
                piles[left] = num

        return len(piles)
