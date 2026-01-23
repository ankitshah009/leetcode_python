#66. Plus One
#Easy
#
#You are given a large integer represented as an integer array digits, where each
#digits[i] is the ith digit of the integer. The digits are ordered from most
#significant to least significant in left-to-right order. The large integer does
#not contain any leading 0's.
#
#Increment the large integer by one and return the resulting array of digits.
#
#Example 1:
#Input: digits = [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Incrementing by one gives 123 + 1 = 124.
#
#Example 2:
#Input: digits = [4,3,2,1]
#Output: [4,3,2,2]
#
#Example 3:
#Input: digits = [9]
#Output: [1,0]
#
#Constraints:
#    1 <= digits.length <= 100
#    0 <= digits[i] <= 9
#    digits does not contain any leading 0's.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Simulate addition with carry.
        """
        n = len(digits)
        carry = 1

        for i in range(n - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10

            if carry == 0:
                return digits

        # Still have carry
        return [1] + digits


class SolutionRecursive:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Recursive approach.
        """
        if not digits:
            return [1]

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]


class SolutionInteger:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Convert to integer and back (for small numbers).
        """
        num = int(''.join(map(str, digits))) + 1
        return [int(d) for d in str(num)]


class SolutionFindNonNine:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Find rightmost non-9 digit.
        """
        # Find rightmost non-9
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # All digits were 9
        return [1] + digits
