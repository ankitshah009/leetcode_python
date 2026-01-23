#1561. Maximum Number of Coins You Can Get
#Medium
#
#There are 3n piles of coins of varying size, you and your friends will take
#piles of coins as follows:
#- In each step, you will choose any 3 piles of coins (not necessarily consecutive).
#- Of your choice, Alice will pick the pile with the maximum number of coins.
#- You will pick the next pile with the maximum number of coins.
#- Your friend Bob will pick the last pile.
#- Repeat until there are no more piles of coins.
#
#Given an array of integers piles where piles[i] is the number of coins in the
#ith pile.
#
#Return the maximum number of coins you can have.
#
#Example 1:
#Input: piles = [2,4,1,2,7,8]
#Output: 9
#Explanation: Choose the triplet (2, 7, 8), Alice picks 8, you pick 7, Bob picks 2.
#Choose the triplet (1, 2, 4), Alice picks 4, you pick 2, Bob picks 1.
#You get 7 + 2 = 9 coins in total.
#
#Example 2:
#Input: piles = [2,4,5]
#Output: 4
#
#Example 3:
#Input: piles = [9,8,7,6,5,1,2,3,4]
#Output: 18
#
#Constraints:
#    3 <= piles.length <= 10^5
#    piles.length % 3 == 0
#    1 <= piles[i] <= 10^4

from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        """
        Greedy: Give Bob the smallest piles, and for each remaining pair,
        Alice gets the larger, you get the smaller.

        Strategy:
        1. Sort piles in descending order
        2. Give Bob the smallest n/3 piles
        3. From remaining 2n/3 piles, you get every other one (the second largest)
        """
        piles.sort(reverse=True)
        n = len(piles) // 3

        # You pick the second element in each triplet
        # From sorted array: positions 1, 3, 5, ... (every other starting from 1)
        return sum(piles[i] for i in range(1, 2 * n, 2))


class SolutionAscending:
    def maxCoins(self, piles: List[int]) -> int:
        """
        Sort ascending and select from the end.
        """
        piles.sort()
        n = len(piles) // 3

        # Skip first n (Bob's piles)
        # From remaining, pick every other (you get second largest in each pair)
        result = 0
        for i in range(n, len(piles), 2):
            result += piles[i]

        return result


class SolutionSlicing:
    def maxCoins(self, piles: List[int]) -> int:
        """
        Using slice notation.
        """
        piles.sort()
        n = len(piles) // 3

        # Skip n smallest, then take every other element
        return sum(piles[n::2])


class SolutionExplained:
    def maxCoins(self, piles: List[int]) -> int:
        """
        Explanation of the greedy strategy.

        We want to maximize our coins. Alice always takes the max.
        Bob takes the min. We take the middle.

        Optimal: Always give Bob the smallest piles available.
        This leaves the largest piles for Alice and us.

        After sorting descendingly: [large, ..., small]
        Each round: Alice takes piles[0], you take piles[1], Bob takes smallest remaining

        So you get: piles[1], piles[3], piles[5], ... for n rounds
        """
        piles.sort(reverse=True)
        n = len(piles) // 3

        total = 0
        for round_num in range(n):
            # In round i, you get the element at position 2*i + 1
            your_index = 2 * round_num + 1
            total += piles[your_index]

        return total


class SolutionOneLiner:
    def maxCoins(self, piles: List[int]) -> int:
        """One-liner solution."""
        return sum(sorted(piles)[len(piles) // 3::2])
