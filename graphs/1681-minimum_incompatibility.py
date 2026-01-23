#1681. Minimum Incompatibility
#Hard
#
#You are given an integer array nums and an integer k. You are asked to
#distribute this array into k subsets of equal size such that there are no two
#equal elements in the same subset.
#
#The incompatibility of a subset is defined as the difference between the
#maximum and minimum elements in that subset.
#
#Return the minimum possible sum of incompatibilities of the k subsets after
#distributing the array optimally, or return -1 if it is not possible.
#
#Example 1:
#Input: nums = [1,2,1,4], k = 2
#Output: 4
#Explanation: The optimal distribution is [1,2] and [1,4].
#Incompatibilities are 2-1=1 and 4-1=3. Total = 4.
#
#Example 2:
#Input: nums = [6,3,8,1,3,1,2,2], k = 4
#Output: 6
#
#Example 3:
#Input: nums = [5,3,3,6,3,3], k = 3
#Output: -1
#Explanation: It's impossible since we have 4 threes and can only use 2 per subset.
#
#Constraints:
#    1 <= k <= nums.length <= 16
#    nums.length is divisible by k
#    1 <= nums[i] <= nums.length

from typing import List
from functools import lru_cache
from collections import Counter

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        """
        Bitmask DP: precompute valid subsets and their incompatibilities.
        """
        n = len(nums)
        subset_size = n // k

        # Check if possible
        if max(Counter(nums).values()) > k:
            return -1

        # Precompute incompatibility for all valid subsets of size subset_size
        subset_incompat = {}
        for mask in range(1, 1 << n):
            if bin(mask).count('1') != subset_size:
                continue

            # Extract elements in this subset
            elements = [nums[i] for i in range(n) if mask & (1 << i)]

            # Check if all distinct
            if len(set(elements)) != subset_size:
                continue

            subset_incompat[mask] = max(elements) - min(elements)

        # DP: dp[mask] = min incompatibility using elements in mask
        @lru_cache(maxsize=None)
        def dp(remaining: int) -> int:
            if remaining == 0:
                return 0

            result = float('inf')

            # Try all valid subsets that are subsets of remaining
            for subset, incompat in subset_incompat.items():
                if (subset & remaining) == subset:
                    result = min(result, incompat + dp(remaining ^ subset))

            return result

        result = dp((1 << n) - 1)
        return result if result != float('inf') else -1


class SolutionBacktrack:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        """
        Backtracking with pruning.
        """
        n = len(nums)
        subset_size = n // k

        if max(Counter(nums).values()) > k:
            return -1

        nums.sort()
        groups = [[] for _ in range(k)]
        min_sum = [float('inf')]

        def backtrack(idx: int, curr_sum: int):
            if curr_sum >= min_sum[0]:
                return

            if idx == n:
                min_sum[0] = curr_sum
                return

            seen = set()

            for i in range(k):
                if len(groups[i]) < subset_size and nums[idx] not in seen:
                    if groups[i] and nums[idx] in [g for g in groups[i]]:
                        continue

                    seen.add(nums[idx] if groups[i] else None)

                    was_empty = len(groups[i]) == 0
                    old_min = groups[i][0] if groups[i] else nums[idx]

                    groups[i].append(nums[idx])

                    add_sum = 0
                    if len(groups[i]) == subset_size:
                        add_sum = groups[i][-1] - groups[i][0]

                    backtrack(idx + 1, curr_sum + add_sum)

                    groups[i].pop()

                # Early termination: if group is empty and we don't add, skip remaining empty groups
                if not groups[i]:
                    break

        backtrack(0, 0)
        return min_sum[0] if min_sum[0] != float('inf') else -1


class SolutionIterative:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        """
        Iterative DP with bitmask.
        """
        n = len(nums)
        group_size = n // k

        if max(Counter(nums).values()) > k:
            return -1

        # Precompute valid groups
        valid = {}
        for mask in range(1, 1 << n):
            if bin(mask).count('1') != group_size:
                continue

            elements = sorted([nums[i] for i in range(n) if mask & (1 << i)])
            if len(set(elements)) == group_size:
                valid[mask] = elements[-1] - elements[0]

        # DP
        INF = float('inf')
        dp = {0: 0}

        for mask in range(1, 1 << n):
            if bin(mask).count('1') % group_size != 0:
                continue

            # Find best way to form this mask
            best = INF
            for group, cost in valid.items():
                if (group & mask) == group:
                    prev = mask ^ group
                    if prev in dp:
                        best = min(best, dp[prev] + cost)

            if best < INF:
                dp[mask] = best

        return dp.get((1 << n) - 1, -1)
