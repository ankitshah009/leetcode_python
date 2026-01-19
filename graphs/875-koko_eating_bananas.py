#875. Koko Eating Bananas
#Medium
#
#Koko loves to eat bananas. There are n piles of bananas, the ith pile has
#piles[i] bananas. The guards have gone and will come back in h hours.
#
#Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses
#some pile of bananas and eats k bananas from that pile. If the pile has less
#than k bananas, she eats all of them instead and will not eat any more bananas
#during this hour.
#
#Koko likes to eat slowly but still wants to finish eating all the bananas before
#the guards return.
#
#Return the minimum integer k such that she can eat all the bananas within h hours.
#
#Example 1:
#Input: piles = [3,6,7,11], h = 8
#Output: 4
#
#Example 2:
#Input: piles = [30,11,23,4,20], h = 5
#Output: 30
#
#Example 3:
#Input: piles = [30,11,23,4,20], h = 6
#Output: 23
#
#Constraints:
#    1 <= piles.length <= 10^4
#    piles.length <= h <= 10^9
#    1 <= piles[i] <= 10^9

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Binary search on eating speed"""

        def can_finish(k: int) -> bool:
            hours = sum((p + k - 1) // k for p in piles)  # Ceiling division
            return hours <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left


class SolutionCeil:
    """Using math.ceil for clarity"""

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum(math.ceil(p / k) for p in piles)

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left


class SolutionBisect:
    """Using bisect module"""

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import bisect

        def hours_needed(k):
            return sum((p + k - 1) // k for p in piles)

        # Find smallest k where hours_needed(k) <= h
        # This is equivalent to finding rightmost k where hours_needed(k) > h, then +1

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if hours_needed(mid) > h:
                left = mid + 1
            else:
                right = mid

        return left
