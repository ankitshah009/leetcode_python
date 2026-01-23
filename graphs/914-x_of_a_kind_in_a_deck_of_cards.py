#914. X of a Kind in a Deck of Cards
#Easy
#
#You are given an integer array deck where deck[i] represents the number written
#on the i-th card. Partition the cards into one or more groups such that:
#- Each group has exactly x cards where x > 1
#- All cards in each group have the same integer written on them.
#
#Return true if such partition is possible, or false otherwise.
#
#Example 1:
#Input: deck = [1,2,3,4,4,3,2,1]
#Output: true
#Explanation: Groups of [1,1],[2,2],[3,3],[4,4]
#
#Example 2:
#Input: deck = [1,1,1,2,2,2,3,3]
#Output: false
#
#Example 3:
#Input: deck = [1,1,2,2,2,2]
#Output: true
#Explanation: Groups of [1,1],[2,2],[2,2]
#
#Constraints:
#    1 <= deck.length <= 10^4
#    0 <= deck[i] < 10^4

from math import gcd
from functools import reduce
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        """
        Find GCD of all counts. If GCD >= 2, partition is possible.
        """
        counts = Counter(deck)
        g = reduce(gcd, counts.values())
        return g >= 2


class SolutionExplicit:
    """More explicit GCD calculation"""

    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        from collections import Counter

        counts = Counter(deck)
        values = list(counts.values())

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        g = values[0]
        for v in values[1:]:
            g = gcd(g, v)

        return g >= 2


class SolutionTryAll:
    """Try all possible group sizes"""

    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        from collections import Counter

        counts = Counter(deck)
        n = len(deck)

        for x in range(2, n + 1):
            if n % x == 0:
                if all(c % x == 0 for c in counts.values()):
                    return True

        return False
