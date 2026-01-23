#1130. Minimum Cost Tree From Leaf Values
#Medium
#
#Given an array arr of positive integers, consider all binary trees such that:
#    Each node has either 0 or 2 children;
#    The values of arr correspond to the values of each leaf in an in-order
#    traversal of the tree.
#    The value of each non-leaf node is equal to the product of the largest
#    leaf value in its left and right subtree, respectively.
#
#Among all possible binary trees considered, return the smallest possible
#sum of the values of each non-leaf node. It is guaranteed this sum fits
#into a 32-bit integer.
#
#A node is a leaf if and only if it has zero children.
#
#Example 1:
#Input: arr = [6,2,4]
#Output: 32
#Explanation: There are two possible trees. The first has a non-leaf node sum 36,
#and the second has non-leaf node sum 32.
#
#Example 2:
#Input: arr = [4,11]
#Output: 44
#
#Constraints:
#    2 <= arr.length <= 40
#    1 <= arr[i] <= 15
#    It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 2^31).

from typing import List
from functools import lru_cache

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        Greedy with monotonic stack.
        Remove the smaller neighbor each time to minimize cost.
        """
        result = 0
        stack = [float('inf')]

        for val in arr:
            while stack[-1] <= val:
                mid = stack.pop()
                result += mid * min(stack[-1], val)
            stack.append(val)

        while len(stack) > 2:
            result += stack.pop() * stack[-1]

        return result


class SolutionDP:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        Interval DP: dp[i][j] = min cost for arr[i:j+1]
        """
        n = len(arr)

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == j:
                return 0

            result = float('inf')
            for k in range(i, j):
                left_max = max(arr[i:k+1])
                right_max = max(arr[k+1:j+1])
                cost = left_max * right_max + dp(i, k) + dp(k + 1, j)
                result = min(result, cost)

            return result

        return dp(0, n - 1)


class SolutionIterativeDP:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """Bottom-up interval DP"""
        n = len(arr)
        INF = float('inf')

        # Precompute max for each range
        max_val = [[0] * n for _ in range(n)]
        for i in range(n):
            max_val[i][i] = arr[i]
            for j in range(i + 1, n):
                max_val[i][j] = max(max_val[i][j-1], arr[j])

        dp = [[INF] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    cost = max_val[i][k] * max_val[k+1][j]
                    cost += dp[i][k] + dp[k+1][j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n-1]
