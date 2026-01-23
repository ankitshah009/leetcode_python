#96. Unique Binary Search Trees
#Medium
#
#Given an integer n, return the number of structurally unique BST's (binary
#search trees) which has exactly n nodes of unique values from 1 to n.
#
#Example 1:
#Input: n = 3
#Output: 5
#
#Example 2:
#Input: n = 1
#Output: 1
#
#Constraints:
#    1 <= n <= 19

class Solution:
    def numTrees(self, n: int) -> int:
        """
        DP approach - Catalan numbers.
        G(n) = sum(G(i-1) * G(n-i)) for i = 1 to n
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for num_nodes in range(2, n + 1):
            for root in range(1, num_nodes + 1):
                left_count = root - 1
                right_count = num_nodes - root
                dp[num_nodes] += dp[left_count] * dp[right_count]

        return dp[n]


class SolutionCatalan:
    def numTrees(self, n: int) -> int:
        """
        Direct Catalan number formula.
        C(n) = (2n)! / ((n+1)! * n!)
        """
        from math import factorial
        return factorial(2 * n) // (factorial(n + 1) * factorial(n))


class SolutionCatalanIterative:
    def numTrees(self, n: int) -> int:
        """
        Catalan number with iterative computation.
        C(n) = C(n-1) * 2(2n-1) / (n+1)
        """
        catalan = 1
        for i in range(n):
            catalan = catalan * 2 * (2 * i + 1) // (i + 2)
        return catalan


class SolutionMemo:
    def numTrees(self, n: int) -> int:
        """
        Recursive with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def count(num_nodes: int) -> int:
            if num_nodes <= 1:
                return 1

            total = 0
            for root in range(1, num_nodes + 1):
                left = count(root - 1)
                right = count(num_nodes - root)
                total += left * right

            return total

        return count(n)


class SolutionRecursive:
    def numTrees(self, n: int) -> int:
        """
        Pure recursive (exponential, for understanding).
        """
        if n <= 1:
            return 1

        total = 0
        for root in range(1, n + 1):
            left = self.numTrees(root - 1)
            right = self.numTrees(n - root)
            total += left * right

        return total
