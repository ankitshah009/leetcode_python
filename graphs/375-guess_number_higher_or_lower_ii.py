#375. Guess Number Higher or Lower II
#Medium
#
#We are playing the Guessing Game. The game will work as follows:
#
#1. I pick a number between 1 and n.
#2. You guess a number.
#3. If you guess the right number, you win the game.
#4. If you guess the wrong number, then I will tell you whether the number I
#   picked is higher or lower, and you will continue guessing.
#5. Every time you guess a wrong number x, you will pay x dollars. If you run
#   out of money, you lose the game.
#
#Given a particular n, return the minimum amount of money you need to guarantee
#a win regardless of what number I pick.
#
#Example 1:
#Input: n = 10
#Output: 16
#Explanation: The winning strategy is as follows:
#- The range is [1,10]. Guess 7.
#    - If this is my number, your total is $0. Otherwise, you pay $7.
#    - If my number is higher, the range is [8,10]. Guess 9.
#        - If this is my number, your total is $7. Otherwise, you pay $9.
#        - If my number is higher, it must be 10. Your total is $7 + $9 = $16.
#        - If my number is lower, it must be 8. Your total is $7 + $9 = $16.
#    - If my number is lower, the range is [1,6]. Guess 3.
#        - If this is my number, your total is $7. Otherwise, you pay $3.
#        - If my number is higher, the range is [4,6]. Guess 5.
#            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
#            - If my number is higher, it must be 6. Total is $7 + $3 + $5 = $15.
#            - If my number is lower, it must be 4. Total is $7 + $3 + $5 = $15.
#        - If my number is lower, the range is [1,2]. Guess 1.
#            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
#            - If my number is higher, it must be 2. Total is $7 + $3 + $1 = $11.
#The worst case in all these scenarios is that you pay $16. Hence, you only need
#$16 to guarantee a win.
#
#Example 2:
#Input: n = 1
#Output: 0
#
#Example 3:
#Input: n = 2
#Output: 1
#
#Constraints:
#    1 <= n <= 200

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
        Minimax DP.
        dp[i][j] = minimum cost to guarantee win for range [i, j]

        For each guess k in [i, j]:
        cost = k + max(dp[i][k-1], dp[k+1][j])  # worst case

        dp[i][j] = min over all k of cost  # best strategy
        """
        # dp[i][j] = min cost for range [i, j]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # Fill by increasing range length
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                dp[i][j] = float('inf')

                for k in range(i, j + 1):
                    left_cost = dp[i][k - 1] if k > i else 0
                    right_cost = dp[k + 1][j] if k < j else 0
                    cost = k + max(left_cost, right_cost)
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n]


class SolutionMemo:
    """Memoization approach"""

    def getMoneyAmount(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i >= j:
                return 0

            min_cost = float('inf')
            for k in range(i, j + 1):
                cost = k + max(dp(i, k - 1), dp(k + 1, j))
                min_cost = min(min_cost, cost)

            return min_cost

        return dp(1, n)


class SolutionOptimized:
    """Optimized with binary search-like pruning"""

    def getMoneyAmount(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i >= j:
                return 0

            # For small ranges, try all
            if j - i <= 2:
                return min(
                    k + max(dp(i, k - 1), dp(k + 1, j))
                    for k in range(i, j + 1)
                )

            # For larger ranges, optimal k is around 2/3 point
            # due to the cost being proportional to k
            min_cost = float('inf')
            for k in range((i + j) // 2, j + 1):
                cost = k + max(dp(i, k - 1), dp(k + 1, j))
                if cost < min_cost:
                    min_cost = cost
                elif dp(i, k - 1) > dp(k + 1, j):
                    break  # No need to try higher k

            return min_cost

        return dp(1, n)
