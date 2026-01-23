#1725. Number Of Rectangles That Can Form The Largest Square
#Easy
#
#You are given an array rectangles where rectangles[i] = [li, wi] represents the
#ith rectangle of length li and width wi.
#
#You can cut a square from any rectangle if the side length of the square is at
#most the minimum of the rectangle's length and width. For example, if you have
#a rectangle [4,6], you can cut a square with a side length of at most 4.
#
#Let maxLen be the side length of the largest square you can obtain from any of
#the given rectangles.
#
#Return the number of rectangles that can make a square with a side length of
#maxLen.
#
#Example 1:
#Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
#Output: 3
#
#Example 2:
#Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
#Output: 3
#
#Constraints:
#    1 <= rectangles.length <= 1000
#    rectangles[i].length == 2
#    1 <= li, wi <= 10^9

from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        """
        Find max square size, count rectangles that can form it.
        """
        max_square = 0
        count = 0

        for l, w in rectangles:
            square = min(l, w)
            if square > max_square:
                max_square = square
                count = 1
            elif square == max_square:
                count += 1

        return count


class SolutionTwoPass:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        """
        Two pass approach - find max, then count.
        """
        squares = [min(l, w) for l, w in rectangles]
        max_square = max(squares)
        return squares.count(max_square)


class SolutionCounter:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        """
        Using Counter.
        """
        from collections import Counter

        squares = [min(l, w) for l, w in rectangles]
        counter = Counter(squares)
        max_square = max(counter.keys())
        return counter[max_square]
