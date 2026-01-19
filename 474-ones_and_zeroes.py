#474. Ones and Zeroes
#Medium
#
#You are given an array of binary strings strs and two integers m and n.
#
#Return the size of the largest subset of strs such that there are at most m 0's and n 1's
#in the subset.
#
#A set x is a subset of a set y if all elements of x are also elements of y.
#
#Example 1:
#Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
#Output: 4
#Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"},
#so the answer is 4.
#
#Example 2:
#Input: strs = ["10","0","1"], m = 1, n = 1
#Output: 2
#Explanation: The largest subset is {"0", "1"}, so the answer is 2.
#
#Constraints:
#    1 <= strs.length <= 600
#    1 <= strs[i].length <= 100
#    strs[i] consists only of digits '0' and '1'.
#    1 <= m, n <= 100

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 2D knapsack problem
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            # Iterate backwards to avoid using same string twice
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
