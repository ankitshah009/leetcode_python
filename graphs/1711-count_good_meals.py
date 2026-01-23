#1711. Count Good Meals
#Medium
#
#A good meal is a meal that contains exactly two different food items with a sum
#of deliciousness equal to a power of two.
#
#You can pick any two different foods to make a good meal.
#
#Given an array of integers deliciousness where deliciousness[i] is the
#deliciousness of the ith item of food, return the number of different good meals
#you can make from this list modulo 10^9 + 7.
#
#Note that items with different indices are considered different even if they
#have the same deliciousness value.
#
#Example 1:
#Input: deliciousness = [1,3,5,7,9]
#Output: 4
#
#Example 2:
#Input: deliciousness = [1,1,1,3,3,3,7]
#Output: 15
#
#Constraints:
#    1 <= deliciousness.length <= 10^5
#    0 <= deliciousness[i] <= 2^20

from typing import List
from collections import Counter

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        """
        Two sum approach - for each element, check if (power_of_2 - element) exists.
        """
        MOD = 10**9 + 7
        count = Counter()
        result = 0

        # Max possible sum is 2^21 (since max value is 2^20)
        powers = [1 << i for i in range(22)]

        for d in deliciousness:
            for power in powers:
                complement = power - d
                if complement in count:
                    result = (result + count[complement]) % MOD

            count[d] += 1

        return result


class SolutionTwoPass:
    def countPairs(self, deliciousness: List[int]) -> int:
        """
        Count frequency first, then count pairs.
        Need to be careful with double counting.
        """
        MOD = 10**9 + 7
        freq = Counter(deliciousness)
        result = 0
        seen = set()

        powers = [1 << i for i in range(22)]

        for d in freq:
            for power in powers:
                complement = power - d
                if complement in freq:
                    if d == complement:
                        # Pairs of same value: C(n, 2) = n * (n-1) / 2
                        if d not in seen:
                            result += freq[d] * (freq[d] - 1) // 2
                    elif complement not in seen:
                        # Pairs of different values
                        result += freq[d] * freq[complement]

            seen.add(d)

        return result % MOD


class SolutionBruteForce:
    def countPairs(self, deliciousness: List[int]) -> int:
        """
        Brute force - O(n^2) - for small inputs.
        """
        MOD = 10**9 + 7
        n = len(deliciousness)
        result = 0

        def is_power_of_two(x: int) -> bool:
            return x > 0 and (x & (x - 1)) == 0

        for i in range(n):
            for j in range(i + 1, n):
                if is_power_of_two(deliciousness[i] + deliciousness[j]):
                    result += 1

        return result % MOD
