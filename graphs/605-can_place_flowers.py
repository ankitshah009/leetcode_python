#605. Can Place Flowers
#Easy
#
#You have a long flowerbed in which some of the plots are planted, and some are not.
#However, flowers cannot be planted in adjacent plots.
#
#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and
#1 means not empty, and an integer n, return true if n new flowers can be planted
#in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#
#Example 1:
#Input: flowerbed = [1,0,0,0,1], n = 1
#Output: true
#
#Example 2:
#Input: flowerbed = [1,0,0,0,1], n = 2
#Output: false
#
#Constraints:
#    1 <= flowerbed.length <= 2 * 10^4
#    flowerbed[i] is 0 or 1.
#    There are no two adjacent flowers in flowerbed.
#    0 <= n <= flowerbed.length

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Greedy - place flowers whenever possible"""
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True

        return count >= n


class SolutionNoModify:
    """Without modifying input array"""

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        prev = 0

        for i in range(length):
            if flowerbed[i] == 0:
                next_val = flowerbed[i + 1] if i < length - 1 else 0

                if prev == 0 and next_val == 0:
                    count += 1
                    prev = 1  # Mark as planted
                else:
                    prev = 0
            else:
                prev = 1

        return count >= n


class SolutionConsecutiveZeros:
    """Count consecutive zeros approach"""

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Add zeros at boundaries for easier calculation
        fb = [0] + flowerbed + [0]
        count = 0
        zeros = 0

        for i in range(len(fb)):
            if fb[i] == 0:
                zeros += 1
            else:
                # Number of flowers that can fit in consecutive zeros
                count += max(0, (zeros - 1) // 2)
                zeros = 0

        # Handle trailing zeros
        count += max(0, (zeros - 1) // 2)

        return count >= n
