#1449. Form Largest Integer With Digits That Add up to Target
#Hard
#
#Given an array of integers cost where cost[i] is the cost of ith digit (i+1)
#in a string, return the maximum integer you can paint under the following rules:
#    The cost of painting a digit (i+1) is given by cost[i] (0-indexed).
#    The total cost used must be equal to target.
#    The integer does not have 0 digits.
#
#Since the answer may be very large, return it as a string. If there is no way
#to paint any integer given the condition, return "0".
#
#Example 1:
#Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
#Output: "7772"
#Explanation: The cost to paint the digit '7' is 2, and the digit '2' is 3.
#Then cost("7772") = 2*3 + 3 = 9. You could also paint "977", but "7772" is the
#largest number.
#
#Example 2:
#Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
#Output: "85"
#Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5.
#Then cost("85") = 7 + 5 = 12.
#
#Example 3:
#Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
#Output: "0"
#Explanation: It is impossible to paint any integer with total cost equal to
#target.
#
#Constraints:
#    cost.length == 9
#    1 <= cost[i], target <= 5000

from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        """
        DP to find maximum length number achievable with given target.
        Then reconstruct the number greedily using largest digits first.
        """
        # dp[t] = maximum number of digits achievable with cost t
        dp = [-1] * (target + 1)
        dp[0] = 0

        for t in range(1, target + 1):
            for i in range(9):
                c = cost[i]
                if t >= c and dp[t - c] >= 0:
                    dp[t] = max(dp[t], dp[t - c] + 1)

        if dp[target] < 0:
            return "0"

        # Reconstruct: greedily pick largest digits
        result = []
        t = target
        while t > 0:
            for digit in range(9, 0, -1):
                c = cost[digit - 1]
                if t >= c and dp[t - c] == dp[t] - 1:
                    result.append(str(digit))
                    t -= c
                    break

        return ''.join(result)


class SolutionString:
    def largestNumber(self, cost: List[int], target: int) -> str:
        """
        DP storing the actual string.
        Compare by length first, then lexicographically.
        """
        # dp[t] = largest number string with cost exactly t
        dp = [""] + ["#"] * target  # "#" represents impossible

        for t in range(1, target + 1):
            for digit in range(1, 10):
                c = cost[digit - 1]
                if t >= c and dp[t - c] != "#":
                    candidate = str(digit) + dp[t - c]
                    # Compare: longer is better, if same length, lexicographically larger
                    if (len(candidate) > len(dp[t]) or
                        (len(candidate) == len(dp[t]) and candidate > dp[t])):
                        if dp[t] == "#" or len(candidate) > len(dp[t]) or candidate > dp[t]:
                            dp[t] = candidate

        return dp[target] if dp[target] != "#" else "0"


class SolutionMemo:
    def largestNumber(self, cost: List[int], target: int) -> str:
        """Using memoization"""
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(t: int) -> int:
            """Return max digits achievable with cost t"""
            if t == 0:
                return 0
            if t < 0:
                return float('-inf')

            max_digits = float('-inf')
            for c in cost:
                max_digits = max(max_digits, 1 + dp(t - c))
            return max_digits

        max_len = dp(target)
        if max_len <= 0:
            return "0"

        # Reconstruct
        result = []
        t = target
        for _ in range(max_len):
            for digit in range(9, 0, -1):
                c = cost[digit - 1]
                if t >= c and dp(t - c) == max_len - len(result) - 1:
                    result.append(str(digit))
                    t -= c
                    break

        return ''.join(result)
