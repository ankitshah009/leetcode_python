#1508. Range Sum of Sorted Subarray Sums
#Medium
#
#You are given the array nums consisting of n positive integers. You computed
#the sum of all non-empty continuous subarrays from the array and then sorted
#them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
#
#Return the sum of the numbers from index left to index right (indexed from 1),
#inclusive, in the new array. Since the answer can be a huge number return it
#modulo 10^9 + 7.
#
#Example 1:
#Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
#Output: 13
#Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting
#them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10].
#The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13.
#
#Example 2:
#Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
#Output: 6
#Explanation: The given array is the same as example 1. We have the new array
#[1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to
#ri = 4 is 3 + 3 = 6.
#
#Example 3:
#Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
#Output: 50
#
#Constraints:
#    n == nums.length
#    1 <= nums.length <= 1000
#    1 <= nums[i] <= 100
#    1 <= left <= right <= n * (n + 1) / 2

from typing import List
import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        Generate all subarray sums, sort, and sum range [left-1, right).
        O(n^2 log n) time.
        """
        MOD = 10**9 + 7

        # Generate all subarray sums
        sums = []
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                sums.append(total)

        # Sort
        sums.sort()

        # Sum from left-1 to right-1 (inclusive)
        return sum(sums[left - 1:right]) % MOD


class SolutionHeap:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        Use min-heap to generate sums in sorted order.
        O(n^2 log n) time but more memory efficient.
        """
        MOD = 10**9 + 7

        # Min-heap: (sum, end_index)
        # Each entry represents subarray nums[start:end+1]
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)

        result = 0

        for k in range(1, right + 1):
            current_sum, end = heapq.heappop(heap)

            if k >= left:
                result = (result + current_sum) % MOD

            # Extend the subarray if possible
            if end + 1 < n:
                heapq.heappush(heap, (current_sum + nums[end + 1], end + 1))

        return result


class SolutionBinarySearch:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        Binary search approach for very large arrays.
        Find k-th smallest sum using binary search + two pointers.
        """
        MOD = 10**9 + 7

        def count_and_sum(target: int) -> tuple:
            """Count sums <= target and their total sum"""
            count = 0
            total = 0
            window_sum = 0
            prefix_sum = 0

            j = 0
            for i in range(n):
                while j < n and window_sum + nums[j] <= target:
                    window_sum += nums[j]
                    prefix_sum += nums[j] * (j - i + 1)
                    j += 1

                count += j - i
                total += prefix_sum

                if j > i:
                    window_sum -= nums[i]
                    prefix_sum -= window_sum + nums[i]

            return count, total

        def sum_of_first_k(k: int) -> int:
            """Sum of k smallest subarray sums"""
            # Binary search for the k-th smallest sum
            lo, hi = min(nums), sum(nums)

            while lo < hi:
                mid = (lo + hi) // 2
                count, _ = count_and_sum(mid)
                if count < k:
                    lo = mid + 1
                else:
                    hi = mid

            # lo is now the k-th smallest (or the value of k-th smallest group)
            count, total = count_and_sum(lo - 1)
            # Add (k - count) copies of lo
            return total + lo * (k - count)

        return (sum_of_first_k(right) - sum_of_first_k(left - 1)) % MOD


class SolutionPrefixSum:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        Using prefix sums for subarray sum calculation.
        """
        MOD = 10**9 + 7

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Generate all subarray sums using prefix difference
        sums = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                sums.append(prefix[j] - prefix[i])

        sums.sort()

        return sum(sums[left - 1:right]) % MOD
