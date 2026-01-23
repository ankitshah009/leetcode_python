#1655. Distribute Repeating Integers
#Hard
#
#You are given an array of n integers, nums, where there are at most 50 unique
#values in the array. You are also given an array of m customer order quantities,
#quantity, where quantity[i] is the amount of integers the ith customer ordered.
#Determine if it is possible to distribute nums such that:
#- The ith customer gets exactly quantity[i] integers,
#- The integers the ith customer gets are all equal, and
#- Every customer is satisfied.
#
#Return true if it is possible to distribute nums according to the above
#conditions.
#
#Example 1:
#Input: nums = [1,2,3,4], quantity = [2]
#Output: false
#Explanation: No customer can get 2 integers of the same value.
#
#Example 2:
#Input: nums = [1,2,3,3], quantity = [2]
#Output: true
#Explanation: Customer gets [3,3].
#
#Example 3:
#Input: nums = [1,1,2,2], quantity = [2,2]
#Output: true
#Explanation: 1st customer gets [1,1], 2nd gets [2,2].
#
#Constraints:
#    n == nums.length
#    1 <= n <= 10^5
#    1 <= nums[i] <= 1000
#    m == quantity.length
#    1 <= m <= 10
#    1 <= quantity[i] <= 10^5
#    There are at most 50 unique values in nums.

from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        """
        Bitmask DP: try to assign subsets of customers to each unique value.
        """
        counts = list(Counter(nums).values())
        m = len(quantity)

        # Precompute sum of each subset of customers
        subset_sum = [0] * (1 << m)
        for mask in range(1 << m):
            for i in range(m):
                if mask & (1 << i):
                    subset_sum[mask] += quantity[i]

        @lru_cache(maxsize=None)
        def dp(idx: int, mask: int) -> bool:
            """
            Can we satisfy customers in mask using counts[idx:] ?
            """
            if mask == 0:
                return True
            if idx == len(counts):
                return False

            # Try all subsets of remaining customers
            submask = mask
            while submask > 0:
                if subset_sum[submask] <= counts[idx]:
                    if dp(idx + 1, mask ^ submask):
                        return True
                submask = (submask - 1) & mask

            # Don't use this count
            return dp(idx + 1, mask)

        return dp(0, (1 << m) - 1)


class SolutionIterative:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        """
        Iterative bitmask DP.
        """
        counts = list(Counter(nums).values())
        m = len(quantity)
        full_mask = (1 << m) - 1

        # Precompute subset sums
        subset_sum = [0] * (1 << m)
        for mask in range(1 << m):
            for i in range(m):
                if mask & (1 << i):
                    subset_sum[mask] += quantity[i]

        # dp[mask] = can we satisfy customers in mask?
        dp = [False] * (1 << m)
        dp[0] = True

        for count in counts:
            # Process in reverse to avoid using same count twice
            for mask in range(full_mask, 0, -1):
                if dp[mask]:
                    continue

                # Try assigning subset to this count
                submask = mask
                while submask > 0:
                    if subset_sum[submask] <= count and dp[mask ^ submask]:
                        dp[mask] = True
                        break
                    submask = (submask - 1) & mask

        return dp[full_mask]


class SolutionBacktrack:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        """
        Backtracking with pruning.
        """
        counts = list(Counter(nums).values())
        quantity.sort(reverse=True)  # Try larger quantities first
        m = len(quantity)

        def backtrack(customer_idx: int) -> bool:
            if customer_idx == m:
                return True

            needed = quantity[customer_idx]
            seen = set()  # Avoid duplicate counts

            for i, count in enumerate(counts):
                if count in seen or count < needed:
                    continue

                seen.add(count)
                counts[i] -= needed

                if backtrack(customer_idx + 1):
                    return True

                counts[i] += needed

            return False

        return backtrack(0)


class SolutionOptimized:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        """
        Optimized with early termination.
        """
        counts = sorted(Counter(nums).values(), reverse=True)
        quantity.sort(reverse=True)

        # Early check
        if sum(counts) < sum(quantity):
            return False

        m = len(quantity)

        # Precompute subset sums
        subset_sum = {}
        for mask in range(1 << m):
            total = 0
            for i in range(m):
                if mask & (1 << i):
                    total += quantity[i]
            subset_sum[mask] = total

        @lru_cache(maxsize=None)
        def dp(idx: int, mask: int) -> bool:
            if mask == 0:
                return True
            if idx == len(counts):
                return False

            remaining_sum = sum(counts[idx:])
            if remaining_sum < subset_sum[mask]:
                return False

            submask = mask
            while submask > 0:
                if subset_sum[submask] <= counts[idx]:
                    if dp(idx + 1, mask ^ submask):
                        return True
                submask = (submask - 1) & mask

            return dp(idx + 1, mask)

        return dp(0, (1 << m) - 1)
