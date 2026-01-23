#873. Length of Longest Fibonacci Subsequence
#Medium
#
#A sequence x1, x2, ..., xn is Fibonacci-like if:
#- n >= 3
#- xi + xi+1 == xi+2 for all i + 2 <= n
#
#Given a strictly increasing array arr of positive integers forming a sequence,
#return the length of the longest Fibonacci-like subsequence of arr. If one does
#not exist, return 0.
#
#A subsequence is derived from another sequence arr by deleting any number of
#elements (including none) from arr, without changing the order of the remaining
#elements.
#
#Example 1:
#Input: arr = [1,2,3,4,5,6,7,8]
#Output: 5
#Explanation: The longest subsequence that is Fibonacci-like: [1,2,3,5,8].
#
#Example 2:
#Input: arr = [1,3,7,11,12,14,18]
#Output: 3
#Explanation: [1,11,12], [3,11,14], [7,11,18] are length 3.
#
#Constraints:
#    3 <= arr.length <= 1000
#    1 <= arr[i] < arr[i + 1] <= 10^9

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        """
        DP: dp[i][j] = length of Fibonacci sequence ending with arr[i], arr[j]
        """
        n = len(arr)
        index = {v: i for i, v in enumerate(arr)}

        # dp[j][k] = length ending with arr[j], arr[k]
        dp = {}
        max_len = 0

        for k in range(n):
            for j in range(k):
                # Looking for arr[i] where arr[i] + arr[j] = arr[k]
                target = arr[k] - arr[j]

                if target < arr[j] and target in index:
                    i = index[target]
                    length = dp.get((i, j), 2) + 1
                    dp[(j, k)] = length
                    max_len = max(max_len, length)

        return max_len if max_len >= 3 else 0


class SolutionSet:
    """Using set for O(n^2) lookup"""

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        arr_set = set(arr)
        max_len = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b = arr[i], arr[j]
                length = 2

                while a + b in arr_set:
                    a, b = b, a + b
                    length += 1

                max_len = max(max_len, length)

        return max_len if max_len >= 3 else 0


class SolutionBruteForce:
    """Try all pairs as starting point"""

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        arr_set = set(arr)
        n = len(arr)
        max_len = 0

        for i in range(n):
            for j in range(i + 1, n):
                x, y = arr[j], arr[i] + arr[j]
                length = 2

                while y in arr_set:
                    x, y = y, x + y
                    length += 1

                if length > max_len:
                    max_len = length

        return max_len if max_len >= 3 else 0
