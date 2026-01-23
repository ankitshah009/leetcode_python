#1447. Simplified Fractions
#Medium
#
#Given an integer n, return a list of all simplified fractions between 0 and 1
#(exclusive) such that the denominator is less-than-or-equal-to n. You can return
#the answer in any order.
#
#Example 1:
#Input: n = 2
#Output: ["1/2"]
#Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
#
#Example 2:
#Input: n = 3
#Output: ["1/2","1/3","2/3"]
#
#Example 3:
#Input: n = 4
#Output: ["1/2","1/3","1/4","2/3","3/4"]
#Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".
#
#Constraints:
#    1 <= n <= 100

from typing import List
from math import gcd

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        """
        Generate all fractions numerator/denominator where:
        - denominator from 2 to n
        - numerator from 1 to denominator-1
        - gcd(numerator, denominator) == 1 (simplified)
        """
        result = []

        for denom in range(2, n + 1):
            for numer in range(1, denom):
                if gcd(numer, denom) == 1:
                    result.append(f"{numer}/{denom}")

        return result


class SolutionSet:
    def simplifiedFractions(self, n: int) -> List[str]:
        """Using set to avoid duplicates (though gcd check is better)"""
        seen = set()
        result = []

        for denom in range(2, n + 1):
            for numer in range(1, denom):
                g = gcd(numer, denom)
                simplified = (numer // g, denom // g)

                if simplified not in seen:
                    seen.add(simplified)
                    result.append(f"{simplified[0]}/{simplified[1]}")

        return result


class SolutionExplicit:
    def simplifiedFractions(self, n: int) -> List[str]:
        """With explicit GCD calculation"""
        def compute_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        result = []
        for d in range(2, n + 1):
            for num in range(1, d):
                if compute_gcd(num, d) == 1:
                    result.append(f"{num}/{d}")

        return result
