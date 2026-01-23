#1362. Closest Divisors
#Medium
#
#Given an integer num, find the closest two integers in absolute difference
#whose product equals num + 1 or num + 2.
#
#Return the two integers in any order.
#
#Example 1:
#Input: num = 8
#Output: [3,3]
#Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
#
#Example 2:
#Input: num = 123
#Output: [5,25]
#
#Example 3:
#Input: num = 999
#Output: [40,25]
#
#Constraints:
#    1 <= num <= 10^9

from typing import List
import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        """
        Find divisors closest to sqrt(n) for both num+1 and num+2.
        """
        def find_closest_pair(n):
            # Start from sqrt and go down
            for i in range(int(math.sqrt(n)), 0, -1):
                if n % i == 0:
                    return [i, n // i]
            return [1, n]

        pair1 = find_closest_pair(num + 1)
        pair2 = find_closest_pair(num + 2)

        if abs(pair1[0] - pair1[1]) <= abs(pair2[0] - pair2[1]):
            return pair1
        return pair2


class SolutionCombined:
    def closestDivisors(self, num: int) -> List[int]:
        """Check both num+1 and num+2 simultaneously"""
        for i in range(int(math.sqrt(num + 2)), 0, -1):
            if (num + 1) % i == 0:
                return [i, (num + 1) // i]
            if (num + 2) % i == 0:
                return [i, (num + 2) // i]

        return [1, num + 1]
