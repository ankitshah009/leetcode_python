#813. Largest Sum of Averages
#Medium
#
#You are given an integer array nums and an integer k. You can partition the
#array into at most k non-empty adjacent subarrays. The score of a partition is
#the sum of the averages of each subarray.
#
#Note that the partition must use every integer in nums, and that the score is
#not necessarily an integer.
#
#Return the largest score you can achieve.
#
#Example 1:
#Input: nums = [9,1,2,3,9], k = 3
#Output: 20.00000
#Explanation: The best choice is [9], [1, 2, 3], [9]. The answer is 9 + 2 + 9 = 20.
#
#Example 2:
#Input: nums = [1,2,3,4,5,6,7], k = 4
#Output: 20.50000
#
#Constraints:
#    1 <= nums.length <= 100
#    1 <= nums[i] <= 10^4
#    1 <= k <= nums.length

class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        """
        DP: dp[i][j] = max score for nums[0:i] with j partitions.
        """
        n = len(nums)

        # Prefix sums for quick average calculation
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def avg(i, j):
            """Average of nums[i:j]"""
            return (prefix[j] - prefix[i]) / (j - i)

        # dp[i] = max score for nums[0:i]
        dp = [avg(0, i) for i in range(n + 1)]

        for _ in range(k - 1):
            new_dp = [0.0] * (n + 1)
            for i in range(1, n + 1):
                for j in range(i):
                    new_dp[i] = max(new_dp[i], dp[j] + avg(j, i))
            dp = new_dp

        return dp[n]


class SolutionMemo:
    """Memoized recursion"""

    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        from functools import lru_cache

        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        @lru_cache(maxsize=None)
        def dp(i, parts):
            """Max score for nums[i:] with exactly parts partitions"""
            if parts == 1:
                return (prefix[n] - prefix[i]) / (n - i)

            best = 0
            for j in range(i + 1, n - parts + 2):
                avg = (prefix[j] - prefix[i]) / (j - i)
                best = max(best, avg + dp(j, parts - 1))

            return best

        return dp(0, k)


class Solution2D:
    """Explicit 2D DP"""

    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # dp[i][j] = max score for first i elements with j groups
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i

        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for p in range(j - 1, i):
                    avg = (prefix[i] - prefix[p]) / (i - p)
                    dp[i][j] = max(dp[i][j], dp[p][j - 1] + avg)

        return dp[n][k]
