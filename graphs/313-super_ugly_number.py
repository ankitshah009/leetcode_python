#313. Super Ugly Number
#Medium
#
#A super ugly number is a positive integer whose prime factors are in the array
#primes.
#
#Given an integer n and an array of integers primes, return the nth super ugly
#number.
#
#The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
#
#Example 1:
#Input: n = 12, primes = [2,7,13,19]
#Output: 32
#Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
#super ugly numbers given primes = [2,7,13,19].
#
#Example 2:
#Input: n = 1, primes = [2,3,5]
#Output: 1
#Explanation: 1 has no prime factors, therefore all of its prime factors are in
#the array primes = [2,3,5].
#
#Constraints:
#    1 <= n <= 10^5
#    1 <= primes.length <= 100
#    2 <= primes[i] <= 1000
#    primes[i] is guaranteed to be a prime number.
#    All the values of primes are unique and sorted in ascending order.

from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """Multi-pointer approach like Ugly Number II"""
        ugly = [1] * n
        k = len(primes)

        # Pointers for each prime
        pointers = [0] * k

        for i in range(1, n):
            # Calculate next candidates
            candidates = [primes[j] * ugly[pointers[j]] for j in range(k)]

            # Take minimum
            ugly[i] = min(candidates)

            # Advance all pointers that produced the minimum (handles duplicates)
            for j in range(k):
                if candidates[j] == ugly[i]:
                    pointers[j] += 1

        return ugly[n - 1]


class SolutionHeap:
    """Min heap approach"""

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Heap: (value, prime_index, ugly_index)
        heap = [(p, i, 0) for i, p in enumerate(primes)]
        heapq.heapify(heap)

        ugly = [1]

        while len(ugly) < n:
            val, prime_idx, ugly_idx = heapq.heappop(heap)

            # Avoid duplicates
            if val != ugly[-1]:
                ugly.append(val)

            # Push next multiple
            next_val = primes[prime_idx] * ugly[ugly_idx + 1] if ugly_idx + 1 < len(ugly) else primes[prime_idx] * val
            heapq.heappush(heap, (primes[prime_idx] * ugly[ugly_idx + 1] if ugly_idx + 1 < len(ugly) else float('inf'), prime_idx, ugly_idx + 1))

        return ugly[n - 1]


class SolutionSet:
    """Using set to avoid duplicates"""

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        seen = {1}
        heap = [(p, p, 0) for p in primes]  # (value, prime, index in ugly)
        heapq.heapify(heap)

        while len(ugly) < n:
            val, prime, idx = heapq.heappop(heap)

            if val not in seen:
                seen.add(val)
                ugly.append(val)

            # Next candidate for this prime
            if idx + 1 < len(ugly):
                next_val = prime * ugly[idx + 1]
                heapq.heappush(heap, (next_val, prime, idx + 1))

        return ugly[n - 1]
