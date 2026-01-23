#1000. Minimum Cost to Merge Stones
#Hard
#
#There are n piles of stones arranged in a row. The i-th pile has stones[i]
#stones.
#
#A move consists of merging exactly k consecutive piles into one pile, and the
#cost of this move is equal to the total number of stones in these k piles.
#
#Return the minimum cost to merge all piles of stones into one pile. If it is
#impossible, return -1.
#
#Example 1:
#Input: stones = [3,2,4,1], k = 2
#Output: 20
#Explanation: Merge [3,2] cost 5, merge [4,1] cost 5, merge [5,5] cost 10.
#Total = 20.
#
#Example 2:
#Input: stones = [3,2,4,1], k = 3
#Output: -1
#
#Example 3:
#Input: stones = [3,5,1,2,6], k = 3
#Output: 25
#
#Constraints:
#    n == stones.length
#    1 <= n <= 30
#    1 <= stones[i] <= 100
#    2 <= k <= 30

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        """
        DP: dp[i][j] = min cost to merge stones[i:j+1] into minimum piles.
        """
        n = len(stones)

        # Check if possible: each merge reduces piles by k-1
        if (n - 1) % (k - 1) != 0:
            return -1

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[i][j] = min cost to merge stones[i:j+1] into as few piles as possible
        dp = [[0] * n for _ in range(n)]

        for length in range(k, n + 1):  # Subarray length
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                # Try all split points
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])

                # If can merge into one pile, add cost
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return dp[0][n - 1]


class SolutionMemo:
    """Memoization with pile count"""

    def mergeStones(self, stones: list[int], k: int) -> int:
        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i: int, j: int, piles: int) -> int:
            """Min cost to merge stones[i:j+1] into exactly 'piles' piles."""
            if (j - i + 1 - piles) % (k - 1) != 0:
                return float('inf')

            if i == j:
                return 0 if piles == 1 else float('inf')

            if piles == 1:
                return dp(i, j, k) + prefix[j + 1] - prefix[i]

            # Split into left part with 1 pile and right part with piles-1 piles
            result = float('inf')
            for mid in range(i, j, k - 1):
                result = min(result, dp(i, mid, 1) + dp(mid + 1, j, piles - 1))

            return result

        return dp(0, n - 1, 1)
