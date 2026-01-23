#1835. Find XOR Sum of All Pairs Bitwise AND
#Hard
#
#The XOR sum of a list is the bitwise XOR of all its elements. If the list only
#contains one element, then its XOR sum will be equal to this element.
#
#You are given two 0-indexed arrays arr1 and arr2 that consist only of
#non-negative integers.
#
#Consider the list containing the result of arr1[i] AND arr2[j] (bitwise AND)
#for every (i, j) pair where 0 <= i < arr1.length and 0 <= j < arr2.length.
#
#Return the XOR sum of the aforementioned list.
#
#Example 1:
#Input: arr1 = [1,2,3], arr2 = [6,5]
#Output: 0
#
#Example 2:
#Input: arr1 = [12], arr2 = [4]
#Output: 4
#
#Constraints:
#    1 <= arr1.length, arr2.length <= 10^5
#    0 <= arr1[i], arr2[j] <= 10^9

from typing import List
from functools import reduce
from operator import xor

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Key insight: XOR(a AND b for all a,b) = (XOR of arr1) AND (XOR of arr2)

        Proof:
        For each bit position, count how many pairs have that bit set.
        A pair (a, b) has bit k set in (a AND b) iff both a and b have bit k set.

        If c1 = count of arr1 elements with bit k set
        And c2 = count of arr2 elements with bit k set
        Then c1 * c2 pairs have bit k set.

        XOR of all results has bit k set iff c1 * c2 is odd
        iff c1 is odd AND c2 is odd
        iff (XOR of arr1) has bit k set AND (XOR of arr2) has bit k set
        """
        xor1 = reduce(xor, arr1)
        xor2 = reduce(xor, arr2)
        return xor1 & xor2


class SolutionExplicit:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Explicit loop version.
        """
        xor1 = 0
        for num in arr1:
            xor1 ^= num

        xor2 = 0
        for num in arr2:
            xor2 ^= num

        return xor1 & xor2


class SolutionBruteForce:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Brute force O(n*m) for verification on small inputs.
        """
        result = 0
        for a in arr1:
            for b in arr2:
                result ^= (a & b)
        return result
