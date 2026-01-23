#1354. Construct Target Array With Multiple Sums
#Hard
#
#You are given an array target of n integers. From a starting array arr
#consisting of n 1's, you may perform the following procedure:
#    let x be the sum of all elements currently in your array.
#    choose index i, such that 0 <= i < n and set the value of arr at index i to x.
#    You may repeat this procedure as many times as needed.
#
#Return true if it is possible to construct the target array from arr,
#otherwise, return false.
#
#Example 1:
#Input: target = [9,3,5]
#Output: true
#Explanation: Start with arr = [1, 1, 1]
#[1, 1, 1], sum = 3 choose index 1
#[1, 3, 1], sum = 5 choose index 2
#[1, 3, 5], sum = 9 choose index 0
#[9, 3, 5] Done
#
#Example 2:
#Input: target = [1,1,1,2]
#Output: false
#Explanation: Impossible to create target array from [1,1,1,1].
#
#Example 3:
#Input: target = [8,5]
#Output: true
#
#Constraints:
#    n == target.length
#    1 <= n <= 5 * 10^4
#    1 <= target[i] <= 10^9

from typing import List
import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """
        Work backwards: the largest element was the last one replaced.
        It was replaced with the sum, so previous value = largest - rest_sum.
        Use max heap to always process the largest.
        """
        total = sum(target)
        max_heap = [-x for x in target]  # Max heap using negation
        heapq.heapify(max_heap)

        while True:
            largest = -heapq.heappop(max_heap)

            # If largest is 1, all elements are 1
            if largest == 1:
                return True

            rest_sum = total - largest

            # Edge cases
            if rest_sum == 0:
                return False  # Only one element, can't be > 1
            if rest_sum == 1:
                return True  # Can always reach [1, 1, ..., 1]
            if largest <= rest_sum:
                return False

            # Compute previous value using modulo to speed up
            # previous = largest - k * rest_sum for some k, where previous >= 1
            previous = largest % rest_sum

            if previous == 0:
                # largest is a multiple of rest_sum
                # Can only work if rest_sum is 1
                if rest_sum == 1:
                    return True
                return False

            total = total - largest + previous
            heapq.heappush(max_heap, -previous)


class SolutionSimple:
    def isPossible(self, target: List[int]) -> bool:
        """Simpler version without modulo optimization (TLE for large inputs)"""
        total = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        while -max_heap[0] > 1:
            largest = -heapq.heappop(max_heap)
            rest_sum = total - largest

            if rest_sum == 0 or largest <= rest_sum:
                return False

            previous = largest - rest_sum
            total = rest_sum + previous

            heapq.heappush(max_heap, -previous)

        return True
