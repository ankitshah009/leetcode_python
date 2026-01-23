#1276. Number of Burgers with No Waste of Ingredients
#Medium
#
#Given two integers tomatoSlices and cheeseSlices. The ingredients of different
#burgers are as follows:
#    Jumbo Burger: 4 tomato slices and 1 cheese slice.
#    Small Burger: 2 tomato slices and 1 cheese slice.
#
#Return [total_jumbo, total_small] so that the number of remaining tomatoSlices
#equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not
#possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].
#
#Example 1:
#Input: tomatoSlices = 16, cheeseSlices = 7
#Output: [1,6]
#Explanation: To make one jumbo burger and 6 small burgers we need
#4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese.
#
#Example 2:
#Input: tomatoSlices = 17, cheeseSlices = 4
#Output: []
#Explanation: There will be no way to use all ingredients.
#
#Example 3:
#Input: tomatoSlices = 4, cheeseSlices = 17
#Output: []
#Explanation: Making 1 jumbo burger there will be 16 cheese slices left.
#
#Constraints:
#    0 <= tomatoSlices, cheeseSlices <= 10^7

from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        """
        System of equations:
        4*jumbo + 2*small = tomato
        jumbo + small = cheese

        Solving:
        4*jumbo + 2*small = tomato
        2*jumbo + 2*small = 2*cheese

        Subtracting:
        2*jumbo = tomato - 2*cheese
        jumbo = (tomato - 2*cheese) / 2

        small = cheese - jumbo
        """
        tomato, cheese = tomatoSlices, cheeseSlices

        # Check if jumbo is a valid non-negative integer
        if (tomato - 2 * cheese) < 0 or (tomato - 2 * cheese) % 2 != 0:
            return []

        jumbo = (tomato - 2 * cheese) // 2
        small = cheese - jumbo

        if small < 0:
            return []

        return [jumbo, small]


class SolutionExplicit:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        """More explicit validation"""
        t, c = tomatoSlices, cheeseSlices

        # From equations:
        # 4j + 2s = t
        # j + s = c
        # => 2j = t - 2c
        # => j = (t - 2c) / 2
        # => s = c - j = c - (t - 2c)/2 = (4c - t) / 2

        if (t - 2 * c) % 2 != 0:
            return []

        jumbo = (t - 2 * c) // 2
        small = c - jumbo

        if jumbo < 0 or small < 0:
            return []

        return [jumbo, small]
