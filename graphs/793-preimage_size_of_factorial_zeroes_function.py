#793. Preimage Size of Factorial Zeroes Function
#Hard
#
#Let f(x) be the number of zeroes at the end of x!.
#
#Given an integer k, return the number of non-negative integers x have the
#property that f(x) = k.
#
#Example 1:
#Input: k = 0
#Output: 5
#Explanation: 0!, 1!, 2!, 3!, and 4! end in k = 0 zeroes.
#
#Example 2:
#Input: k = 5
#Output: 0
#Explanation: There is no x such that x! ends in k = 5 zeroes.
#
#Example 3:
#Input: k = 3
#Output: 5
#
#Constraints:
#    0 <= k <= 10^9

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        """
        Binary search to find range of x where f(x) = k.
        Key insight: f(x) is non-decreasing and increases by 1
        most of the time, but skips values at powers of 5.
        Answer is either 0 or 5.
        """
        def trailing_zeros(n):
            """Count trailing zeros in n!"""
            count = 0
            while n >= 5:
                n //= 5
                count += n
            return count

        def first_with_k_zeros(k):
            """Find smallest x with at least k trailing zeros"""
            left, right = 0, 5 * k + 1
            while left < right:
                mid = (left + right) // 2
                if trailing_zeros(mid) < k:
                    left = mid + 1
                else:
                    right = mid
            return left

        # If we can find an x with exactly k zeros, answer is 5
        # Otherwise answer is 0
        x = first_with_k_zeros(k)
        return 5 if trailing_zeros(x) == k else 0


class SolutionBinarySearchBoth:
    """Binary search for both boundaries"""

    def preimageSizeFZF(self, k: int) -> int:
        def zeros(n):
            count = 0
            while n >= 5:
                n //= 5
                count += n
            return count

        def lower_bound(k):
            lo, hi = 0, 5 * (k + 1)
            while lo < hi:
                mid = (lo + hi) // 2
                if zeros(mid) < k:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        return lower_bound(k + 1) - lower_bound(k)
