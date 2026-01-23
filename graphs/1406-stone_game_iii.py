#1406. Stone Game III
#Hard
#
#Alice and Bob continue their games with piles of stones. There are several
#stones arranged in a row, and each stone has an associated value which is an
#integer given in the array stoneValue.
#
#Alice and Bob take turns, with Alice starting first. On each player's turn,
#that player can take 1, 2, or 3 stones from the first remaining stones in the row.
#
#The score of each player is the sum of the values of the stones taken. The
#score of each player is 0 initially.
#
#The objective of the game is to end with the highest score, and the winner is
#the player with the highest score and there could be a tie. The game continues
#until all the stones have been taken.
#
#Assume Alice and Bob play optimally.
#
#Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will
#end the game with the same score.
#
#Example 1:
#Input: stoneValue = [1,2,3,7]
#Output: "Bob"
#Explanation: Alice will always lose. Her best move will be to take three piles
#and the score become 6. Now the score of Bob is 7 and Bob wins.
#
#Example 2:
#Input: stoneValue = [1,2,3,-9]
#Output: "Alice"
#Explanation: Alice must choose all the three piles at the first move to win
#and leave Bob with negative score.
#If Alice chooses one pile her score will be 1 and the next move Bob's score
#becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
#If Alice chooses two piles her score will be 3 and the next move Bob's score
#becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
#
#Example 3:
#Input: stoneValue = [1,2,3,6]
#Output: "Tie"
#Explanation: Alice cannot win this game. She can end the game in a draw if she
#decided to choose all the first three piles, otherwise she will lose.
#
#Constraints:
#    1 <= stoneValue.length <= 5 * 10^4
#    -1000 <= stoneValue[i] <= 1000

from typing import List
from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
        DP where dp[i] = max score current player can get starting from index i,
        relative to opponent's score (score_current - score_opponent).

        When taking k stones, get sum(stones[i:i+k]) - dp[i+k]
        """
        n = len(stoneValue)

        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            if i >= n:
                return 0

            # Try taking 1, 2, or 3 stones
            best = float('-inf')
            stones_taken = 0

            for k in range(1, 4):
                if i + k - 1 < n:
                    stones_taken += stoneValue[i + k - 1]
                    # Score = stones I take - best opponent can do
                    best = max(best, stones_taken - dp(i + k))

            return best

        diff = dp(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"


class SolutionIterative:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """Iterative DP"""
        n = len(stoneValue)

        # dp[i] = max relative score starting from index i
        dp = [0] * (n + 3)  # Padding for i+1, i+2, i+3

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            stones = 0

            for k in range(1, 4):
                if i + k <= n:
                    stones += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], stones - dp[i + k])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"


class SolutionSuffixSum:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
        Alternative: dp[i] = max score player can achieve from position i.
        Use suffix sum to compute total available.
        """
        n = len(stoneValue)

        # Suffix sum
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]

        # dp[i] = max score starting from i
        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            for k in range(1, 4):
                if i + k <= n:
                    # Take k stones, opponent gets dp[i+k]
                    # My score = suffix_sum[i] - dp[i+k] (what's left after I take)
                    # Actually: my_score = sum(i to i+k-1) + suffix_sum[i+k] - dp[i+k]
                    dp[i] = max(dp[i], suffix_sum[i] - dp[i + k])

        total = suffix_sum[0]
        alice_score = dp[0]
        bob_score = total - alice_score

        if alice_score > bob_score:
            return "Alice"
        elif alice_score < bob_score:
            return "Bob"
        else:
            return "Tie"
