#823. Binary Trees With Factors
#Medium
#
#Given an array of unique integers, arr, where each integer arr[i] is strictly
#greater than 1.
#
#We make a binary tree using these integers, and each number may be used for
#any number of times. Each non-leaf node's value should be equal to the product
#of the values of its children.
#
#Return the number of binary trees we can make. The answer may be too large so
#return the answer modulo 10^9 + 7.
#
#Example 1:
#Input: arr = [2,4]
#Output: 3
#Explanation: We can make these trees: [2], [4], [4, 2, 2]
#
#Example 2:
#Input: arr = [2,4,5,10]
#Output: 7
#Explanation: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]
#
#Constraints:
#    1 <= arr.length <= 1000
#    2 <= arr[i] <= 10^9
#    All the values of arr are unique.

class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        """
        DP: dp[x] = number of trees with root x.
        Sort and process from smallest to largest.
        """
        MOD = 10**9 + 7

        arr.sort()
        n = len(arr)
        arr_set = set(arr)
        idx = {v: i for i, v in enumerate(arr)}

        # dp[i] = number of trees with arr[i] as root
        dp = [1] * n  # Each element alone is a tree

        for i in range(n):
            for j in range(i):
                # arr[j] is potential left child
                if arr[i] % arr[j] == 0:
                    right = arr[i] // arr[j]
                    if right in arr_set:
                        # Trees = dp[j] * dp[right_idx]
                        dp[i] = (dp[i] + dp[j] * dp[idx[right]]) % MOD

        return sum(dp) % MOD


class SolutionDict:
    """Using dictionary for dp"""

    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        arr.sort()
        arr_set = set(arr)
        dp = {}  # dp[x] = number of trees with root x

        for x in arr:
            dp[x] = 1  # Just the node itself

            for y in arr:
                if y >= x:
                    break
                if x % y == 0 and x // y in dp:
                    dp[x] = (dp[x] + dp[y] * dp[x // y]) % MOD

        return sum(dp.values()) % MOD


class SolutionOptimized:
    """Optimized with sqrt check"""

    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        arr.sort()
        dp = {x: 1 for x in arr}
        arr_set = set(arr)

        for x in arr:
            for y in arr:
                if y * y > x:
                    break
                if x % y == 0:
                    z = x // y
                    if z in arr_set:
                        if y == z:
                            dp[x] = (dp[x] + dp[y] * dp[z]) % MOD
                        else:
                            dp[x] = (dp[x] + 2 * dp[y] * dp[z]) % MOD

        return sum(dp.values()) % MOD
