#779. K-th Symbol in Grammar
#Medium
#
#We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
#Now in every subsequent row, we look at the previous row and replace each
#occurrence of 0 with 01, and each occurrence of 1 with 10.
#
#For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row
#is 0110.
#
#Given two integer n and k, return the kth (1-indexed) symbol in the nth row of
#a table of n rows.
#
#Example 1:
#Input: n = 1, k = 1
#Output: 0
#Explanation: row 1: 0
#
#Example 2:
#Input: n = 2, k = 1
#Output: 0
#Explanation: row 1: 0, row 2: 01
#
#Example 3:
#Input: n = 2, k = 2
#Output: 1
#Explanation: row 1: 0, row 2: 01
#
#Constraints:
#    1 <= n <= 30
#    1 <= k <= 2^(n-1)

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Recursive: k-th symbol in row n depends on ceiling(k/2) in row n-1.
        If k is odd, same as parent. If k is even, flipped from parent.
        """
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1) // 2)

        if k % 2 == 1:
            return parent
        else:
            return 1 - parent


class SolutionBitCount:
    """Count 1 bits in (k-1) - determines number of flips"""

    def kthGrammar(self, n: int, k: int) -> int:
        # The k-th symbol (1-indexed) equals the parity of 1-bits in (k-1)
        return bin(k - 1).count('1') % 2


class SolutionIterative:
    """Iterative version"""

    def kthGrammar(self, n: int, k: int) -> int:
        result = 0

        while k > 1:
            if k % 2 == 0:
                result ^= 1
            k = (k + 1) // 2

        return result


class SolutionXOR:
    """XOR-based approach"""

    def kthGrammar(self, n: int, k: int) -> int:
        # Each row is: previous_row + complement(previous_row)
        # k-th position (1-indexed) in row n:
        # - If k <= 2^(n-2): same as position k in row n-1
        # - If k > 2^(n-2): complement of position (k - 2^(n-2)) in row n-1

        flips = 0
        size = 1 << (n - 1)  # 2^(n-1)

        while size > 1:
            half = size // 2
            if k > half:
                flips += 1
                k -= half
            size = half

        return flips % 2
