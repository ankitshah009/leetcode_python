#1492. The kth Factor of n
#Medium
#
#You are given two positive integers n and k. A factor of an integer n is
#defined as an integer i where n % i == 0.
#
#Consider a list of all factors of n sorted in ascending order, return the kth
#factor in this list or return -1 if n has less than k factors.
#
#Example 1:
#Input: n = 12, k = 3
#Output: 3
#Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
#
#Example 2:
#Input: n = 7, k = 2
#Output: 7
#Explanation: Factors list is [1, 7], the 2nd factor is 7.
#
#Example 3:
#Input: n = 4, k = 4
#Output: -1
#Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should
#return -1.
#
#Constraints:
#    1 <= k <= n <= 1000

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Iterate from 1 to n, count factors.
        """
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        return -1


class SolutionSqrt:
    def kthFactor(self, n: int, k: int) -> int:
        """
        O(sqrt(n)): factors come in pairs (i, n/i).
        Find factors <= sqrt(n), then factors > sqrt(n) in reverse.
        """
        import math

        factors = []

        # Find factors <= sqrt(n)
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                if len(factors) == k:
                    return i

        # Number of small factors found
        small_count = len(factors)

        # Check if sqrt(n) is a perfect square (avoid duplicates)
        sqrt_n = int(math.sqrt(n))
        if sqrt_n * sqrt_n == n:
            small_count -= 1  # Don't count sqrt(n) twice

        # Large factors are n/i for small factors, in reverse order
        # Total factors = small_count + (number of large factors)
        # Large factors: n/factors[-1], n/factors[-2], ..., n/factors[0]
        # But we need to skip sqrt(n) if it's a perfect square

        large_idx = small_count - (1 if sqrt_n * sqrt_n == n else 0) - 1

        for i in range(large_idx, -1, -1):
            small_count += 1
            if small_count == k:
                return n // factors[i]

        return -1


class SolutionList:
    def kthFactor(self, n: int, k: int) -> int:
        """Collect all factors, return k-th"""
        factors = [i for i in range(1, n + 1) if n % i == 0]
        return factors[k - 1] if k <= len(factors) else -1


class SolutionHeap:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Use heap to find k-th smallest factor.
        O(sqrt(n) log k) time.
        """
        import heapq
        import math

        # Max heap to keep k smallest factors
        heap = []

        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                # Add i
                heapq.heappush(heap, -i)
                if len(heap) > k:
                    heapq.heappop(heap)

                # Add n/i if different
                if i != n // i:
                    heapq.heappush(heap, -(n // i))
                    if len(heap) > k:
                        heapq.heappop(heap)

        if len(heap) < k:
            return -1

        return -heap[0]


class SolutionOptimized:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Optimized sqrt approach with early termination.
        """
        count = 0
        i = 1

        # Check factors <= sqrt(n)
        while i * i < n:
            if n % i == 0:
                count += 1
                if count == k:
                    return i
            i += 1

        # Now check factors >= sqrt(n) in descending order
        # These are n/j for j from sqrt(n) down to 1
        j = i
        if j * j == n:
            # j is exactly sqrt(n)
            if n % j == 0:
                count += 1
                if count == k:
                    return j
            j -= 1

        while j >= 1:
            if n % j == 0:
                count += 1
                if count == k:
                    return n // j
            j -= 1

        return -1
