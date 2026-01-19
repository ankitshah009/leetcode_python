#264. Ugly Number II
#Medium
#
#An ugly number is a positive integer whose prime factors are limited to 2, 3,
#and 5.
#
#Given an integer n, return the nth ugly number.
#
#Example 1:
#Input: n = 10
#Output: 12
#Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10
#ugly numbers.
#
#Example 2:
#Input: n = 1
#Output: 1
#Explanation: 1 has no prime factors, therefore all of its prime factors are
#limited to 2, 3, and 5.
#
#Constraints:
#    1 <= n <= 1690

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Three pointers approach - O(n) time, O(n) space.
        Generate ugly numbers in order using three pointers.
        """
        ugly = [0] * n
        ugly[0] = 1

        # Pointers for 2, 3, 5 multiples
        p2 = p3 = p5 = 0

        for i in range(1, n):
            # Next candidates
            next2 = ugly[p2] * 2
            next3 = ugly[p3] * 3
            next5 = ugly[p5] * 5

            # Take minimum
            ugly[i] = min(next2, next3, next5)

            # Advance pointers (may advance multiple if there are ties)
            if ugly[i] == next2:
                p2 += 1
            if ugly[i] == next3:
                p3 += 1
            if ugly[i] == next5:
                p5 += 1

        return ugly[n - 1]


class SolutionHeap:
    """Min heap approach"""

    def nthUglyNumber(self, n: int) -> int:
        import heapq

        heap = [1]
        seen = {1}

        for _ in range(n):
            ugly = heapq.heappop(heap)

            for factor in [2, 3, 5]:
                new_ugly = ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return ugly


class SolutionDP:
    """DP with explicit minimum tracking"""

    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        i2 = i3 = i5 = 0

        for i in range(1, n):
            candidates = [dp[i2] * 2, dp[i3] * 3, dp[i5] * 5]
            dp[i] = min(candidates)

            # Increment all pointers that produced the minimum (handles duplicates)
            if dp[i] == candidates[0]:
                i2 += 1
            if dp[i] == candidates[1]:
                i3 += 1
            if dp[i] == candidates[2]:
                i5 += 1

        return dp[-1]
