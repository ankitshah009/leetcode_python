#88. Merge Sorted Array
#Easy
#
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
#and two integers m and n, representing the number of elements in nums1 and nums2
#respectively.
#
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
#The final sorted array should not be returned by the function, but instead be
#stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
#where the first m elements denote the elements that should be merged, and the
#last n elements are set to 0 and should be ignored. nums2 has a length of n.
#
#Example 1:
#Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]
#
#Example 2:
#Input: nums1 = [1], m = 1, nums2 = [], n = 0
#Output: [1]
#
#Constraints:
#    nums1.length == m + n
#    nums2.length == n
#    0 <= m, n <= 200
#    1 <= m + n <= 200
#    -10^9 <= nums1[i], nums2[j] <= 10^9

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Three pointers from the end - O(m + n) time, O(1) space.
        """
        p1 = m - 1
        p2 = n - 1
        write = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1


class SolutionForward:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Forward merge with copy - O(m + n) time, O(m) space.
        """
        # Copy nums1 elements
        nums1_copy = nums1[:m]

        p1 = p2 = 0
        write = 0

        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1[write] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[write] = nums2[p2]
                p2 += 1
            write += 1

        # Copy remaining
        while p1 < m:
            nums1[write] = nums1_copy[p1]
            p1 += 1
            write += 1

        while p2 < n:
            nums1[write] = nums2[p2]
            p2 += 1
            write += 1


class SolutionSort:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Simple approach - copy and sort.
        O((m+n) log(m+n)) time.
        """
        nums1[m:] = nums2
        nums1.sort()


class SolutionHeap:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Using heap (for educational purpose).
        """
        import heapq

        heap = nums1[:m] + nums2
        heapq.heapify(heap)

        for i in range(m + n):
            nums1[i] = heapq.heappop(heap)
