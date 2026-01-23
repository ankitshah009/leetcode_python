#1131. Maximum of Absolute Value Expression
#Medium
#
#Given two arrays of integers with equal lengths, return the maximum value of:
#
#|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
#
#where the maximum is taken over all 0 <= i, j < arr1.length.
#
#Example 1:
#Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
#Output: 13
#
#Example 2:
#Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
#Output: 20
#
#Constraints:
#    2 <= arr1.length == arr2.length <= 40000
#    -10^6 <= arr1[i], arr2[i] <= 10^6

from typing import List

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Expand absolute values: 2^3 = 8 combinations of signs.
        |a-b| + |c-d| + |e-f| = max over signs of ±(a-b) ± (c-d) ± (e-f)

        For each sign combination, track max and min of (±arr1[i] ± arr2[i] ± i)
        """
        n = len(arr1)
        result = 0

        # 8 sign combinations: (±1, ±1, ±1)
        for s1 in [1, -1]:
            for s2 in [1, -1]:
                for s3 in [1, -1]:
                    max_val = float('-inf')
                    min_val = float('inf')

                    for i in range(n):
                        val = s1 * arr1[i] + s2 * arr2[i] + s3 * i
                        max_val = max(max_val, val)
                        min_val = min(min_val, val)

                    result = max(result, max_val - min_val)

        return result


class SolutionSimplified:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Simplified: only need 4 combinations due to symmetry.
        """
        n = len(arr1)
        result = 0

        for p, q in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            vals = [p * arr1[i] + q * arr2[i] + i for i in range(n)]
            result = max(result, max(vals) - min(vals))

        return result


class SolutionBruteForce:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """O(n^2) brute force for verification"""
        n = len(arr1)
        result = 0

        for i in range(n):
            for j in range(n):
                val = abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j)
                result = max(result, val)

        return result
