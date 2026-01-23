#1015. Smallest Integer Divisible by K
#Medium
#
#Given a positive integer k, you need to find the length of the smallest
#positive integer n such that n is divisible by k, and n only contains the
#digit 1.
#
#Return the length of n. If there is no such n, return -1.
#
#Note: n may not fit in a 64-bit signed integer.
#
#Example 1:
#Input: k = 1
#Output: 1
#Explanation: The smallest answer is n = 1, which has length 1.
#
#Example 2:
#Input: k = 2
#Output: -1
#Explanation: There is no such positive integer n divisible by 2.
#
#Example 3:
#Input: k = 3
#Output: 3
#Explanation: The smallest answer is n = 111, which has length 3.
#
#Constraints:
#    1 <= k <= 10^5

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        Track remainders. If k is even or divisible by 5, impossible.
        """
        # Numbers ending in 1 can never be divisible by 2 or 5
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length

        return -1


class SolutionWithSet:
    """Track seen remainders to detect cycle"""

    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        seen = set()
        remainder = 0
        length = 0

        while True:
            remainder = (remainder * 10 + 1) % k
            length += 1

            if remainder == 0:
                return length

            if remainder in seen:
                return -1

            seen.add(remainder)


class SolutionExplained:
    """With mathematical explanation"""

    def smallestRepunitDivByK(self, k: int) -> int:
        """
        Key insight:
        - If k is even, 111...1 is odd, so never divisible
        - If k divisible by 5, remainder of 111...1 / 5 is always 1
        - Otherwise, by pigeonhole, remainder must repeat within k iterations
        - If we find 0 before cycle, that's the answer
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1

        # Build 111...1 mod k iteratively: n = n*10 + 1
        n_mod_k = 0

        for length in range(1, k + 1):
            n_mod_k = (n_mod_k * 10 + 1) % k

            if n_mod_k == 0:
                return length

        # By pigeonhole, if not found in k iterations, won't find
        return -1
