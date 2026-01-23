#1395. Count Number of Teams
#Medium
#
#There are n soldiers standing in a line. Each soldier is assigned a unique
#rating value.
#
#You have to form a team of 3 soldiers amongst them under the following rules:
#    Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j],
#    rating[k]).
#    A team is valid if: (rating[i] < rating[j] < rating[k]) or
#    (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
#
#Return the number of teams you can form given the conditions.
#(soldiers can be part of multiple teams).
#
#Example 1:
#Input: rating = [2,5,3,4,1]
#Output: 3
#Explanation: We can form three teams given the conditions:
#(2,3,4), (5,4,1), (5,3,1).
#
#Example 2:
#Input: rating = [2,1,3]
#Output: 0
#Explanation: We can't form any team given the conditions.
#
#Example 3:
#Input: rating = [1,2,3,4]
#Output: 4
#
#Constraints:
#    n == rating.length
#    3 <= n <= 1000
#    1 <= rating[i] <= 10^5
#    All the integers in rating are unique.

from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        For each middle element j, count:
        - left_smaller: elements before j that are smaller
        - right_larger: elements after j that are larger
        - left_larger: elements before j that are larger
        - right_smaller: elements after j that are smaller

        Teams = sum of (left_smaller * right_larger + left_larger * right_smaller)
        O(n^2) time, O(1) space.
        """
        n = len(rating)
        count = 0

        for j in range(1, n - 1):
            left_smaller = left_larger = 0
            right_smaller = right_larger = 0

            # Count elements on left
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_larger += 1

            # Count elements on right
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_larger += 1
                else:
                    right_smaller += 1

            # Increasing sequences through j
            count += left_smaller * right_larger
            # Decreasing sequences through j
            count += left_larger * right_smaller

        return count


class SolutionBruteForce:
    def numTeams(self, rating: List[int]) -> int:
        """O(n^3) brute force for comparison"""
        n = len(rating)
        count = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if (rating[i] < rating[j] < rating[k] or
                        rating[i] > rating[j] > rating[k]):
                        count += 1

        return count


class SolutionBIT:
    def numTeams(self, rating: List[int]) -> int:
        """
        Binary Indexed Tree for O(n log n) solution.
        Coordinate compress ratings, then use BIT to count.
        """
        n = len(rating)

        # Coordinate compression
        sorted_rating = sorted(set(rating))
        rank = {v: i + 1 for i, v in enumerate(sorted_rating)}
        compressed = [rank[r] for r in rating]
        max_rank = len(sorted_rating)

        class BIT:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (n + 1)

            def update(self, i, delta=1):
                while i <= self.n:
                    self.tree[i] += delta
                    i += i & (-i)

            def query(self, i):
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & (-i)
                return s

        # Precompute left_smaller and left_larger for each position
        left_smaller = [0] * n
        left_larger = [0] * n
        bit = BIT(max_rank)

        for i in range(n):
            left_smaller[i] = bit.query(compressed[i] - 1)
            left_larger[i] = i - left_smaller[i]
            bit.update(compressed[i])

        # Compute right_larger and right_smaller, accumulate result
        bit = BIT(max_rank)
        count = 0

        for i in range(n - 1, -1, -1):
            right_smaller = bit.query(compressed[i] - 1)
            right_larger = (n - 1 - i) - right_smaller

            count += left_smaller[i] * right_larger
            count += left_larger[i] * right_smaller

            bit.update(compressed[i])

        return count
