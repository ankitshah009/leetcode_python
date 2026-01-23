#575. Distribute Candies
#Easy
#
#Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed
#that she started to gain weight, so she visited a doctor.
#
#The doctor advised Alice to only eat n / 2 of the candies she has (n is always
#even). Alice likes her candies very much, and she wants to eat the maximum number
#of different types of candies while still following the doctor's advice.
#
#Given the integer array candyType of length n, return the maximum number of
#different types of candies she can eat if she only eats n / 2 of them.
#
#Example 1:
#Input: candyType = [1,1,2,2,3,3]
#Output: 3
#Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types,
#she can eat one of each type.
#
#Example 2:
#Input: candyType = [1,1,2,3]
#Output: 2
#
#Example 3:
#Input: candyType = [6,6,6,6]
#Output: 1
#
#Constraints:
#    n == candyType.length
#    2 <= n <= 10^4
#    n is even.
#    -10^5 <= candyType[i] <= 10^5

from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        """
        Maximum types = min(unique_types, n/2)
        """
        unique_types = len(set(candyType))
        max_candies = len(candyType) // 2
        return min(unique_types, max_candies)


class SolutionExplicit:
    """More explicit approach"""

    def distributeCandies(self, candyType: List[int]) -> int:
        # Count unique candy types
        types = set()
        for candy in candyType:
            types.add(candy)

        # Can eat at most n/2 candies
        allowed = len(candyType) // 2

        # Take as many unique types as possible, up to allowed
        return min(len(types), allowed)
