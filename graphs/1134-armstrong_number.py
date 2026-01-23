#1134. Armstrong Number
#Easy
#
#Given an integer n, return true if and only if it is an Armstrong number.
#
#The k-digit integer n is an Armstrong number if and only if the kth power
#of each digit sums to n.
#
#Example 1:
#Input: n = 153
#Output: true
#Explanation: 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
#
#Example 2:
#Input: n = 123
#Output: false
#Explanation: 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
#
#Constraints:
#    1 <= n <= 10^8

class Solution:
    def isArmstrong(self, n: int) -> bool:
        """Check if sum of digits^k equals n"""
        digits = [int(d) for d in str(n)]
        k = len(digits)
        return sum(d ** k for d in digits) == n


class SolutionMath:
    def isArmstrong(self, n: int) -> bool:
        """Without string conversion"""
        temp = n
        digits = []
        while temp > 0:
            digits.append(temp % 10)
            temp //= 10

        k = len(digits)
        return sum(d ** k for d in digits) == n
