#556. Next Greater Element III
#Medium
#
#Given a positive integer n, find the smallest integer which has exactly the same digits
#existing in the integer n and is greater in value than n. If no such positive integer exists,
#return -1.
#
#Note that the returned integer should fit in 32-bit signed integer, if there is a valid
#answer but it does not fit in 32-bit signed integer, return -1.
#
#Example 1:
#Input: n = 12
#Output: 21
#
#Example 2:
#Input: n = 21
#Output: -1
#
#Constraints:
#    1 <= n <= 2^31 - 1

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)

        # Find the first decreasing digit from right
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i < 0:
            return -1

        # Find the smallest digit larger than digits[i] to the right
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Swap
        digits[i], digits[j] = digits[j], digits[i]

        # Reverse the suffix
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int(''.join(digits))

        # Check 32-bit overflow
        return result if result <= 2**31 - 1 else -1
