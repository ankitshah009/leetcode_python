#1073. Adding Two Negabinary Numbers
#Medium
#
#Given two numbers arr1 and arr2 in base -2, return the result of adding
#them together.
#
#Each number is given in array format: as an array of 0s and 1s, from most
#significant bit to least significant bit.
#
#Return the result of the addition in the same format: as an array of 0s
#and 1s with no leading zeros.
#
#Example 1:
#Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
#Output: [1,0,0,0,0]
#Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
#
#Example 2:
#Input: arr1 = [0], arr2 = [0]
#Output: [0]
#
#Example 3:
#Input: arr1 = [0], arr2 = [1]
#Output: [1]
#
#Constraints:
#    1 <= arr1.length, arr2.length <= 1000
#    arr1[i] and arr2[i] are 0 or 1
#    arr1 and arr2 have no leading zeros

from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Add in base -2.
        Key: When carry is 2 at position i, it becomes -1 at position i+1.
        When carry is -1 at position i, add 1 and carry 1 to i+1.
        """
        result = []
        carry = 0
        i, j = len(arr1) - 1, len(arr2) - 1

        while i >= 0 or j >= 0 or carry:
            val = carry
            if i >= 0:
                val += arr1[i]
                i -= 1
            if j >= 0:
                val += arr2[j]
                j -= 1

            # val can be -1, 0, 1, 2, 3
            if val >= 2:
                result.append(val - 2)
                carry = -1  # -2 * (-1) = 2
            elif val == -1:
                result.append(1)
                carry = 1  # -2 * 1 + 1 = -1
            else:
                result.append(val)
                carry = 0

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result[::-1]


class SolutionConvert:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """Convert to decimal, add, convert back"""
        def to_decimal(arr):
            val = 0
            for i, bit in enumerate(reversed(arr)):
                val += bit * ((-2) ** i)
            return val

        def from_decimal(n):
            if n == 0:
                return [0]
            result = []
            while n:
                remainder = n % -2
                n //= -2
                if remainder < 0:
                    remainder += 2
                    n += 1
                result.append(remainder)
            return result[::-1]

        return from_decimal(to_decimal(arr1) + to_decimal(arr2))


class SolutionDetailed:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """More detailed carry handling"""
        result = []
        carry = 0

        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        max_len = max(len(arr1), len(arr2))

        for i in range(max_len + 2):  # Extra space for carry propagation
            val = carry
            if i < len(arr1):
                val += arr1[i]
            if i < len(arr2):
                val += arr2[i]

            # Handle different cases
            if val == 0:
                result.append(0)
                carry = 0
            elif val == 1:
                result.append(1)
                carry = 0
            elif val == 2:
                result.append(0)
                carry = -1
            elif val == 3:
                result.append(1)
                carry = -1
            elif val == -1:
                result.append(1)
                carry = 1

        # Remove trailing zeros (leading in reversed)
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result[::-1]
