#1387. Sort Integers by The Power Value
#Medium
#
#The power of an integer x is defined as the number of steps needed to transform
#x into 1 using the following steps:
#    if x is even then x = x / 2
#    if x is odd then x = 3 * x + 1
#
#For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1
#(3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).
#
#Given three integers lo, hi and k. The task is to sort all integers in the
#interval [lo, hi] by the power value in ascending order, if two or more integers
#have the same power value sort them by ascending order.
#
#Return the kth integer in the range [lo, hi] sorted by the power value.
#
#Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will
#transform into 1 using these steps and that the power of x is will fit in a
#32-bit signed integer.
#
#Example 1:
#Input: lo = 12, hi = 15, k = 2
#Output: 13
#Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
#The power of 13 is 9
#The power of 14 is 17
#The power of 15 is 17
#The interval sorted by the power value [12, 13, 14, 15]. For k = 2 answer is
#the second element which is 13.
#
#Example 2:
#Input: lo = 7, hi = 11, k = 4
#Output: 7
#Explanation: The power array for [7, 8, 9, 10, 11] is [16, 3, 19, 6, 14].
#The sorted array would be [8, 10, 11, 7, 9].
#
#Constraints:
#    1 <= lo <= hi <= 1000
#    1 <= k <= hi - lo + 1

from functools import lru_cache
import heapq

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        Compute power for each number and sort.
        Use memoization to avoid recomputing.
        """
        @lru_cache(maxsize=None)
        def get_power(n: int) -> int:
            if n == 1:
                return 0
            if n % 2 == 0:
                return 1 + get_power(n // 2)
            else:
                return 1 + get_power(3 * n + 1)

        # Create list of (power, number)
        nums = [(get_power(x), x) for x in range(lo, hi + 1)]

        # Sort by power, then by number
        nums.sort()

        return nums[k - 1][1]


class SolutionHeap:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """Use heap to find kth element (more efficient for small k)"""
        memo = {}

        def get_power(n: int) -> int:
            if n == 1:
                return 0
            if n in memo:
                return memo[n]

            if n % 2 == 0:
                result = 1 + get_power(n // 2)
            else:
                result = 1 + get_power(3 * n + 1)

            memo[n] = result
            return result

        # Use heap to get k smallest
        heap = [(get_power(x), x) for x in range(lo, hi + 1)]
        heapq.heapify(heap)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap)[1]


class SolutionIterative:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """Iterative power calculation"""
        def get_power(n: int) -> int:
            steps = 0
            while n != 1:
                if n % 2 == 0:
                    n //= 2
                else:
                    n = 3 * n + 1
                steps += 1
            return steps

        nums = sorted(range(lo, hi + 1), key=lambda x: (get_power(x), x))
        return nums[k - 1]
