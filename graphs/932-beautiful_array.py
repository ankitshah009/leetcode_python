#932. Beautiful Array
#Medium
#
#An array nums of length n is beautiful if:
#- nums is a permutation of the integers in the range [1, n].
#- For every 0 <= i < j < n, there is no index k with i < k < j where
#  2 * nums[k] == nums[i] + nums[j].
#
#Return any beautiful array nums of length n. It is guaranteed that one exists.
#
#Example 1:
#Input: n = 4
#Output: [2,1,4,3]
#
#Example 2:
#Input: n = 5
#Output: [3,1,2,5,4]
#
#Constraints:
#    1 <= n <= 1000

class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        """
        Divide and conquer: odds on left, evens on right.
        Key insight: odd + even != 2*anything (since sum is odd)
        """
        # Start with [1]
        result = [1]

        while len(result) < n:
            # Expand: add odds (2x-1) and evens (2x)
            result = [2 * x - 1 for x in result] + [2 * x for x in result]

        # Filter to keep only values <= n
        return [x for x in result if x <= n]


class SolutionRecursive:
    """Recursive divide and conquer"""

    def beautifulArray(self, n: int) -> list[int]:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def build(n: int) -> tuple:
            if n == 1:
                return (1,)

            # Recursively build for odds and evens
            odds = build((n + 1) // 2)  # Ceil half
            evens = build(n // 2)  # Floor half

            # Transform: odds stay odd, evens stay even
            return tuple(2 * x - 1 for x in odds) + tuple(2 * x for x in evens)

        result = list(build(n))
        return [x for x in result if x <= n]


class SolutionExplicit:
    """With explicit explanation"""

    def beautifulArray(self, n: int) -> list[int]:
        """
        Properties of beautiful arrays:
        1. If A is beautiful, then 2*A-1 is beautiful (all odds)
        2. If A is beautiful, then 2*A is beautiful (all evens)
        3. Concatenating two beautiful arrays (odds, evens) is beautiful
           because odd + even = odd, which can't equal 2*k for any k
        """
        arr = [1]

        while len(arr) < n:
            # Transform to odds and evens, then concatenate
            odds = [2 * x - 1 for x in arr]
            evens = [2 * x for x in arr]
            arr = odds + evens

        return [x for x in arr if x <= n]
