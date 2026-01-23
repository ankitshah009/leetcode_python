#786. K-th Smallest Prime Fraction
#Medium
#
#You are given a sorted integer array arr containing 1 and prime numbers, where
#all the integers of arr are unique. You are also given an integer k.
#
#For every i and j where 0 <= i < j < arr.length, we consider the fraction
#arr[i] / arr[j].
#
#Return the kth smallest fraction considered. Return your answer as an array
#of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
#
#Example 1:
#Input: arr = [1,2,3,5], k = 3
#Output: [2,5]
#Explanation: The fractions to be considered are:
#1/2, 1/3, 2/3, 1/5, 2/5, 3/5
#The third smallest fraction is 2/5.
#
#Example 2:
#Input: arr = [1,7], k = 1
#Output: [1,7]
#
#Constraints:
#    2 <= arr.length <= 1000
#    1 <= arr[i] <= 3 * 10^4
#    arr[0] == 1
#    arr[i] is a prime number for i > 0.
#    All the numbers of arr are unique and sorted in strictly increasing order.
#    1 <= k <= arr.length * (arr.length - 1) / 2

import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        """
        Min-heap with fractions sorted by numerator index for each denominator.
        """
        n = len(arr)
        # Heap: (fraction_value, numerator_index, denominator_index)
        heap = [(arr[0] / arr[j], 0, j) for j in range(1, n)]
        heapq.heapify(heap)

        for _ in range(k):
            val, i, j = heapq.heappop(heap)

            # Add next fraction with same denominator
            if i + 1 < j:
                heapq.heappush(heap, (arr[i + 1] / arr[j], i + 1, j))

        return [arr[i], arr[j]]


class SolutionBinarySearch:
    """Binary search on fraction value"""

    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)

        def count_less_equal(x):
            """Count fractions <= x and track the largest one."""
            count = 0
            best = (0, 1)  # (numerator, denominator)

            j = 1
            for i in range(n):
                while j < n and arr[i] / arr[j] > x:
                    j += 1
                count += n - j

                if j < n and arr[i] * best[1] > best[0] * arr[j]:
                    best = (arr[i], arr[j])

            return count, best

        left, right = 0, 1

        while True:
            mid = (left + right) / 2
            count, best = count_less_equal(mid)

            if count == k:
                return list(best)
            elif count < k:
                left = mid
            else:
                right = mid


class SolutionBruteForce:
    """Generate all fractions and sort (for small inputs)"""

    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        fractions = []
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                fractions.append((arr[i] / arr[j], arr[i], arr[j]))

        fractions.sort()
        return [fractions[k - 1][1], fractions[k - 1][2]]
