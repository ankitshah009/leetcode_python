#698. Partition to K Equal Sum Subsets
#Medium
#
#Given an integer array nums and an integer k, return true if it is possible
#to divide this array into k non-empty subsets whose sums are all equal.
#
#Example 1:
#Input: nums = [4,3,2,3,5,2,1], k = 4
#Output: true
#Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3),
#(2,3) with equal sums.
#
#Example 2:
#Input: nums = [1,2,3,4], k = 3
#Output: false
#
#Constraints:
#    1 <= k <= nums.length <= 16
#    1 <= nums[i] <= 10^4
#    The frequency of each element is in the range [1, 4].

class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        """
        Backtracking: try to fill k buckets with target sum each.
        """
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)  # Optimization: try larger numbers first

        if nums[0] > target:
            return False

        n = len(nums)
        used = [False] * n

        def backtrack(bucket_idx, curr_sum, start):
            if bucket_idx == k:
                return True

            if curr_sum == target:
                return backtrack(bucket_idx + 1, 0, 0)

            for i in range(start, n):
                if used[i]:
                    continue
                if curr_sum + nums[i] > target:
                    continue
                # Skip duplicates at same position
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                if backtrack(bucket_idx, curr_sum + nums[i], i + 1):
                    return True
                used[i] = False

            return False

        return backtrack(0, 0, 0)


class SolutionBitmask:
    """DP with bitmask for subset state"""

    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        n = len(nums)

        # dp[mask] = remaining sum for current subset if reachable, else -1
        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue

            for i in range(n):
                if mask & (1 << i):
                    continue

                new_mask = mask | (1 << i)
                if dp[new_mask] != -1:
                    continue

                # Current subset sum after adding nums[i]
                new_sum = (dp[mask] + nums[i]) % target

                if dp[mask] + nums[i] <= target:
                    dp[new_mask] = new_sum

        return dp[(1 << n) - 1] == 0


class SolutionMemo:
    """Memoized backtracking with bitmask"""

    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        from functools import lru_cache

        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(mask, curr_sum):
            if mask == (1 << n) - 1:
                return True

            for i in range(n):
                if mask & (1 << i):
                    continue

                new_sum = curr_sum + nums[i]
                if new_sum > target:
                    break  # Sorted, so rest are also too big

                new_mask = mask | (1 << i)

                if new_sum == target:
                    if dp(new_mask, 0):
                        return True
                else:
                    if dp(new_mask, new_sum):
                        return True

            return False

        return dp(0, 0)
