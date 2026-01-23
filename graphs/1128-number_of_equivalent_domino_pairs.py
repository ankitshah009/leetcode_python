#1128. Number of Equivalent Domino Pairs
#Easy
#
#Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j]
#= [c, d] if and only if either (a == c and b == d), or (a == d and b == c)
#- that is, one domino can be rotated to be equal to another domino.
#
#Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
#and dominoes[i] is equivalent to dominoes[j].
#
#Example 1:
#Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
#Output: 1
#
#Example 2:
#Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
#Output: 3
#
#Constraints:
#    1 <= dominoes.length <= 4 * 10^4
#    dominoes[i].length == 2
#    1 <= dominoes[i][j] <= 9

from typing import List
from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        Normalize each domino (min, max), count pairs.
        """
        count = Counter()
        result = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            result += count[key]
            count[key] += 1

        return result


class SolutionMath:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """Count groups, then C(n,2) for each"""
        count = Counter()

        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            count[key] += 1

        # C(n, 2) = n * (n-1) / 2
        return sum(c * (c - 1) // 2 for c in count.values())


class SolutionNumeric:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """Use numeric key for faster hashing"""
        count = [0] * 100  # key = 10*min + max

        result = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            key = 10 * a + b
            result += count[key]
            count[key] += 1

        return result
