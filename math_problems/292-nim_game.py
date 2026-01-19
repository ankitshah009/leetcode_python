#292. Nim Game
#Easy
#
#You are playing the following Nim Game with your friend:
#
#Initially, there is a heap of stones on the table.
#You and your friend will alternate taking turns, and you go first.
#On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
#The one who removes the last stone is the winner.
#
#Given n, the number of stones in the heap, return true if you can win the game
#assuming both you and your friend play optimally, otherwise return false.
#
#Example 1:
#Input: n = 4
#Output: false
#Explanation: These are the possible outcomes:
#1. You remove 1 stone. Your friend removes 3 stones, including the last stone.
#   Your friend wins.
#2. You remove 2 stones. Your friend removes 2 stones, including the last stone.
#   Your friend wins.
#3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
#In all outcomes, your friend wins.
#
#Example 2:
#Input: n = 1
#Output: true
#
#Example 3:
#Input: n = 2
#Output: true
#
#Constraints:
#    1 <= n <= 2^31 - 1

class Solution:
    def canWinNim(self, n: int) -> bool:
        # Pattern analysis:
        # n=1: Win (take 1)
        # n=2: Win (take 2)
        # n=3: Win (take 3)
        # n=4: Lose (opponent can always counter)
        # n=5: Win (take 1, leave 4 for opponent)
        # n=6: Win (take 2, leave 4 for opponent)
        # n=7: Win (take 3, leave 4 for opponent)
        # n=8: Lose

        # Pattern: Lose when n is divisible by 4
        # Because whatever you take (1-3), opponent can take (3-1) to make sum 4
        # Eventually opponent takes last stone

        return n % 4 != 0

    # DP approach (for understanding, not practical for large n)
    def canWinNimDP(self, n: int) -> bool:
        if n <= 3:
            return True

        # dp[i] = True if first player wins with i stones
        dp = [False] * (n + 1)
        dp[1] = dp[2] = dp[3] = True

        for i in range(4, n + 1):
            # Win if any move leads to losing state for opponent
            dp[i] = not dp[i-1] or not dp[i-2] or not dp[i-3]

        return dp[n]
