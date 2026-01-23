#650. 2 Keys Keyboard
#Medium
#
#There is only one character 'A' on the screen of a notepad. You can perform one
#of two operations on this notepad for each step:
#
#- Copy All: You can copy all the characters present on the screen (a partial copy
#  is not allowed).
#- Paste: You can paste the characters which are copied last time.
#
#Given an integer n, return the minimum number of operations to get the character
#'A' exactly n times on the screen.
#
#Example 1:
#Input: n = 3
#Output: 3
#Explanation: Initially, we have one character 'A'.
#In step 1, we use Copy All operation.
#In step 2, we use Paste operation to get 'AA'.
#In step 3, we use Paste operation to get 'AAA'.
#
#Example 2:
#Input: n = 1
#Output: 0
#
#Constraints:
#    1 <= n <= 1000

class Solution:
    def minSteps(self, n: int) -> int:
        """
        Prime factorization approach.
        To get n A's, we need sum of prime factors of n.
        """
        result = 0
        factor = 2

        while n > 1:
            while n % factor == 0:
                result += factor
                n //= factor
            factor += 1

        return result


class SolutionDP:
    """Dynamic programming"""

    def minSteps(self, n: int) -> int:
        # dp[i] = min steps to get i A's
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = i  # Worst case: copy 1, paste i-1 times

            # Try all divisors
            for j in range(i // 2, 1, -1):
                if i % j == 0:
                    # Copy j A's, paste i/j - 1 times
                    dp[i] = dp[j] + i // j
                    break

        return dp[n]


class SolutionMemo:
    """Top-down with memoization"""

    def minSteps(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(curr, clipboard):
            if curr == n:
                return 0
            if curr > n:
                return float('inf')

            # Paste
            paste = dp(curr + clipboard, clipboard) + 1 if clipboard > 0 else float('inf')

            # Copy all then paste
            copy_paste = dp(curr * 2, curr) + 2 if curr < n else float('inf')

            return min(paste, copy_paste)

        if n == 1:
            return 0

        return dp(2, 1) + 2  # Start with copy + paste = 2 A's
