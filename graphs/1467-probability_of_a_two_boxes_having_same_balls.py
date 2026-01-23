#1467. Probability of a Two Boxes Having The Same Number of Distinct Balls
#Hard
#
#Given 2n balls of k distinct colors. You will be given an integer array balls
#of size k where balls[i] is the number of balls of color i.
#
#All the balls will be shuffled uniformly at random, then we will distribute
#the first n balls to the first box and the remaining n balls to the other box.
#
#Please note that the two boxes are considered different. For example, if we
#have two balls of colors a and b, and two boxes [] and (), then the distribution
#[a] (b) is considered different than the distribution [b] (a).
#
#Return the probability that the two boxes have the same number of distinct balls.
#Answers within 10^-5 of the actual value will be accepted as correct.
#
#Example 1:
#Input: balls = [1,1]
#Output: 1.00000
#Explanation: Only 2 ways to divide the balls equally:
#- A ball of color 1 to box 1 and a ball of color 2 to box 2
#- A ball of color 2 to box 1 and a ball of color 1 to box 2
#In both ways, the number of distinct balls in each box is equal.
#
#Example 2:
#Input: balls = [2,1,1]
#Output: 0.66667
#Explanation: We have the set of balls [1, 1, 2, 3]
#- [1,1 / 2,3], [1,2 / 1,3], [1,3 / 1,2] have same distinct count of 2
#- [1,2,3 / 1] has 3 vs 1 distinct count
#
#Example 3:
#Input: balls = [1,2,1,2]
#Output: 0.60000
#
#Constraints:
#    1 <= balls.length <= 8
#    1 <= balls[i] <= 6
#    sum(balls) is even.

from typing import List
from functools import lru_cache
from math import factorial, comb

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        """
        Use recursion to enumerate all valid distributions.
        Count permutations where distinct counts are equal.
        """
        k = len(balls)
        n = sum(balls) // 2  # Each box gets n balls

        # Multinomial coefficient: n! / (n1! * n2! * ... * nk!)
        def multinomial(counts: List[int]) -> int:
            result = factorial(sum(counts))
            for c in counts:
                result //= factorial(c)
            return result

        total_ways = 0
        valid_ways = 0

        def backtrack(idx: int, box1: List[int], box2: List[int], sum1: int, sum2: int):
            nonlocal total_ways, valid_ways

            if idx == k:
                if sum1 == n and sum2 == n:
                    # Count permutations for this distribution
                    ways = multinomial(box1) * multinomial(box2)
                    total_ways += ways

                    # Count distinct colors in each box
                    distinct1 = sum(1 for x in box1 if x > 0)
                    distinct2 = sum(1 for x in box2 if x > 0)

                    if distinct1 == distinct2:
                        valid_ways += ways
                return

            # Pruning: can't complete if already exceeded
            remaining = sum(balls[idx:])
            if sum1 > n or sum2 > n:
                return
            if sum1 + remaining < n or sum2 + remaining < n:
                return

            # Try all ways to split balls[idx] between boxes
            for give1 in range(balls[idx] + 1):
                give2 = balls[idx] - give1
                box1.append(give1)
                box2.append(give2)
                backtrack(idx + 1, box1, box2, sum1 + give1, sum2 + give2)
                box1.pop()
                box2.pop()

        backtrack(0, [], [], 0, 0)

        return valid_ways / total_ways if total_ways > 0 else 0


class SolutionMemo:
    def getProbability(self, balls: List[int]) -> float:
        """
        Memoized DFS solution.
        State: (idx, diff, distinct_diff) where diff = sum1 - sum2
        """
        k = len(balls)
        n = sum(balls) // 2

        @lru_cache(maxsize=None)
        def dp(idx: int, diff: int, distinct_diff: int) -> tuple:
            """Returns (total_ways, valid_ways)"""
            if idx == k:
                if diff == 0:
                    valid = 1 if distinct_diff == 0 else 0
                    return (1, valid)
                return (0, 0)

            # Pruning
            remaining = sum(balls[i] for i in range(idx, k))
            if abs(diff) > remaining:
                return (0, 0)

            total = 0
            valid = 0

            for give1 in range(balls[idx] + 1):
                give2 = balls[idx] - give1
                new_diff = diff + give1 - give2

                # Track distinct difference
                dd = distinct_diff
                if give1 > 0 and give2 == 0:
                    dd += 1  # Color only in box1
                elif give1 == 0 and give2 > 0:
                    dd -= 1  # Color only in box2
                # If both > 0, no change to distinct difference

                t, v = dp(idx + 1, new_diff, dd)
                coef = comb(balls[idx], give1)
                total += coef * t
                valid += coef * v

            return (total, valid)

        total_ways, valid_ways = dp(0, 0, 0)
        return valid_ways / total_ways if total_ways > 0 else 0
