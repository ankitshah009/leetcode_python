#1872. Stone Game VIII
#Hard
#
#Alice and Bob take turns playing a game, with Alice starting first.
#
#There are n stones arranged in a row. On each player's turn, while the number
#of stones is more than one, they will do the following:
#
#1. Choose an integer x > 1, and remove the leftmost x stones from the row.
#2. Add a new stone, whose value is the sum of the removed stones, to the left
#   side of the row.
#
#The player who gains the most points wins. The score of a player is the sum
#of the values of all the stones they have added.
#
#Return the difference in score between Alice and Bob if they both play
#optimally.
#
#Example 1:
#Input: stones = [-1,2,-3,4,-5]
#Output: 5
#
#Example 2:
#Input: stones = [7,-6,5,10,5,-2,-6]
#Output: 13
#
#Example 3:
#Input: stones = [-10,-12]
#Output: -22
#
#Constraints:
#    n == stones.length
#    2 <= n <= 10^5
#    -10^4 <= stones[i] <= 10^4

from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        """
        Key insight: when Alice takes stones[0:i+1], she gets prefix[i+1].
        The game continues with stones starting at prefix[i+1].

        dp[i] = max(Alice - Bob) when choosing from index i onwards.
        dp[i] = max(prefix[i] - dp[i+1], dp[i+1])

        Process right to left, tracking max of (prefix[i] - dp[i+1]).
        """
        n = len(stones)

        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[i] = best (Alice - Bob) when game starts at index i
        # Alice must take at least 2 stones, so minimum index to take is 1
        # Taking all stones means getting prefix[n]

        # Process from right to left
        # dp[n-1] = prefix[n] (take all remaining)
        dp = prefix[n]

        # For i from n-2 down to 1:
        # dp[i] = max(prefix[i+1] - dp[i+1], dp[i+1])
        # But dp[i+1] is the previous dp value

        for i in range(n - 2, 0, -1):
            # Take stones[0:i+1] and get prefix[i+1], opponent gets -dp
            # Or skip and let dp[i] = dp[i+1]
            dp = max(prefix[i + 1] - dp, dp)

        return dp


class SolutionExplained:
    def stoneGameVIII(self, stones: List[int]) -> int:
        """
        Detailed explanation:

        When a player takes first x stones, they get sum(stones[0:x]).
        The remaining game has a new stone with this sum at position 0.

        Let prefix[i] = sum of first i stones.

        If Alice takes first i stones, she gets prefix[i].
        Bob then plays optimally on remaining stones starting with prefix[i].

        dp[i] = max difference (current player - opponent) starting at index i.
        Alice wants to maximize, Bob to minimize from his perspective.

        dp[i] = max over j>=i+1 of (prefix[j] - dp[j])
              = max(prefix[i+1] - dp[i+1], dp[i+1])

        The second form works because:
        dp[i+1] = max over j>=i+2 of (prefix[j] - dp[j])

        So dp[i] considers either taking at position i+1 or leaving it.
        """
        n = len(stones)

        prefix = [0]
        for stone in stones:
            prefix.append(prefix[-1] + stone)

        # Start from the end
        result = prefix[n]  # Take all

        for i in range(n - 2, 0, -1):
            # Option: take up to index i+1 and get prefix[i+1]
            # Then opponent plays and gets -result
            result = max(prefix[i + 1] - result, result)

        return result
