#651. 4 Keys Keyboard
#Medium
#
#Imagine you have a special keyboard with the following keys:
#- A: Print one 'A' on the screen.
#- Ctrl-A: Select the whole screen.
#- Ctrl-C: Copy selection to buffer.
#- Ctrl-V: Print buffer on screen appending it after what has already been printed.
#
#Given an integer n, return the maximum number of 'A' you can print on the screen
#with at most n key presses.
#
#Example 1:
#Input: n = 3
#Output: 3
#Explanation: A, A, A
#
#Example 2:
#Input: n = 7
#Output: 9
#Explanation: A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V
#
#Constraints:
#    1 <= n <= 50

class Solution:
    def maxA(self, n: int) -> int:
        """
        DP approach.
        dp[i] = max A's with i keystrokes
        """
        if n <= 6:
            return n

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Option 1: Just press A
            dp[i] = dp[i - 1] + 1

            # Option 2: Use Ctrl-A, Ctrl-C, then multiple Ctrl-V
            # j = position where we do Ctrl-A, Ctrl-C
            # Then we paste (i - j - 2) times, multiplying by (i - j - 1)
            for j in range(i - 3, 0, -1):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        return dp[n]


class SolutionMath:
    """Mathematical observation: optimal to multiply by 4 or 5"""

    def maxA(self, n: int) -> int:
        if n <= 6:
            return n

        # For n > 6, use pattern of multiplying
        # Best multipliers are 4 (using 3 keys) or 5 (using 4 keys)
        dp = list(range(n + 1))

        for i in range(7, n + 1):
            # Try multiplying by 3, 4, 5
            dp[i] = max(dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4)

        return dp[n]
