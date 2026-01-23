#668. Kth Smallest Number in Multiplication Table
#Hard
#
#Nearly everyone has used the Multiplication Table. The multiplication table
#of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
#
#Given three integers m, n, and k, return the kth smallest element in the m x n
#multiplication table.
#
#Example 1:
#Input: m = 3, n = 3, k = 5
#Output: 3
#Explanation: The 5th smallest number is 3.
#
#Example 2:
#Input: m = 2, n = 3, k = 6
#Output: 6
#Explanation: The 6th smallest number is 6.
#
#Constraints:
#    1 <= m, n <= 3 * 10^4
#    1 <= k <= m * n

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        Binary search on the value.
        For each value x, count how many numbers in table are <= x.
        """
        def count_less_equal(x):
            """Count numbers in m x n table that are <= x"""
            count = 0
            for i in range(1, m + 1):
                # In row i: i, 2i, 3i, ...
                # Numbers <= x: x // i (but at most n)
                count += min(x // i, n)
            return count

        left, right = 1, m * n

        while left < right:
            mid = (left + right) // 2

            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left


class SolutionOptimized:
    """Optimized binary search with early termination"""

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_equal(x):
            count = 0
            for i in range(1, m + 1):
                if i > x:
                    break
                count += min(x // i, n)
            return count

        # Ensure m <= n for efficiency
        if m > n:
            m, n = n, m

        left, right = 1, m * n

        while left < right:
            mid = (left + right) // 2

            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left
