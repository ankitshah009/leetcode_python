#1720. Decode XORed Array
#Easy
#
#There is a hidden integer array arr that consists of n non-negative integers.
#
#It was encoded into another integer array encoded of length n - 1, such that
#encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then
#encoded = [1,2,3].
#
#You are given the encoded array. You are also given an integer first, that is
#the first element of arr, i.e., arr[0].
#
#Return the original array arr. It can be proved that the answer exists and is
#unique.
#
#Example 1:
#Input: encoded = [1,2,3], first = 1
#Output: [1,0,2,1]
#
#Example 2:
#Input: encoded = [6,2,7,3], first = 4
#Output: [4,2,0,7,4]
#
#Constraints:
#    2 <= n <= 10^4
#    encoded.length == n - 1
#    0 <= encoded[i] <= 10^5
#    0 <= first <= 10^5

from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        XOR property: if a ^ b = c, then b = a ^ c.
        arr[i+1] = arr[i] ^ encoded[i]
        """
        result = [first]

        for enc in encoded:
            result.append(result[-1] ^ enc)

        return result


class SolutionInPlace:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        Decode by modifying encoded array (saves space).
        """
        n = len(encoded)
        arr = [0] * (n + 1)
        arr[0] = first

        for i in range(n):
            arr[i + 1] = arr[i] ^ encoded[i]

        return arr


class SolutionReduce:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        Using reduce (functional style).
        """
        from functools import reduce
        from itertools import accumulate
        from operator import xor

        return list(accumulate(encoded, xor, initial=first))
