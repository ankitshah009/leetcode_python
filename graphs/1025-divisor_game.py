#1025. Divisor Game
#Easy
#
#Alice and Bob take turns playing a game, with Alice starting first.
#
#Initially, there is a number n on the chalkboard. On each player's turn,
#that player makes a move consisting of:
#    - Choosing any x with 0 < x < n and n % x == 0.
#    - Replacing the number n on the chalkboard with n - x.
#
#Also, if a player cannot make a move, they lose the game.
#
#Return true if and only if Alice wins the game, assuming both players
#play optimally.
#
#Example 1:
#Input: n = 2
#Output: true
#Explanation: Alice chooses 1, and Bob has no more moves.
#
#Example 2:
#Input: n = 3
#Output: false
#Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
#
#Constraints:
#    1 <= n <= 1000

class Solution:
    def divisorGame(self, n: int) -> bool:
        """
        Mathematical observation: Alice wins iff n is even.

        Proof:
        - If n is even, Alice can always choose x=1, leaving odd number
        - If n is odd, all divisors are odd, so n-x is even
        - Therefore, even player can always give odd, odd player gives even
        - Game ends at 1 (odd), so even-starter (Alice) wins if n is even
        """
        return n % 2 == 0


class SolutionDP:
    def divisorGame(self, n: int) -> bool:
        """
        DP: dp[i] = True if player to move wins with number i
        """
        if n == 1:
            return False

        dp = [False] * (n + 1)
        # dp[1] = False (no move possible)

        for i in range(2, n + 1):
            # Try all divisors
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break

        return dp[n]


class SolutionMemo:
    def divisorGame(self, n: int) -> bool:
        """Memoized recursion"""
        memo = {}

        def can_win(num):
            if num == 1:
                return False
            if num in memo:
                return memo[num]

            # Try all divisors
            for x in range(1, num):
                if num % x == 0 and not can_win(num - x):
                    memo[num] = True
                    return True

            memo[num] = False
            return False

        return can_win(n)
