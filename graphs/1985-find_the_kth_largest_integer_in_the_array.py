#1985. Find the Kth Largest Integer in the Array
#Medium
#
#You are given an array of strings nums and an integer k. Each string in nums
#represents an integer without leading zeros.
#
#Return the string that represents the kth largest integer in nums.
#
#Note: Duplicate numbers should be counted distinctly. For example, if nums is
#["1","2","2"], "2" is the first largest integer, "2" is the second-largest
#integer, and "1" is the third-largest integer.
#
#Example 1:
#Input: nums = ["3","6","7","10"], k = 4
#Output: "3"
#
#Example 2:
#Input: nums = ["2","21","12","1"], k = 3
#Output: "2"
#
#Example 3:
#Input: nums = ["0","0"], k = 2
#Output: "0"
#
#Constraints:
#    1 <= k <= nums.length <= 10^4
#    1 <= nums[i].length <= 100
#    nums[i] consists of only digits.
#    nums[i] will not have any leading zeros.

from typing import List
import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        Sort with custom comparator for numeric string comparison.
        """
        def compare_key(s: str) -> tuple:
            return (len(s), s)  # Longer strings are larger; then lexicographic

        nums.sort(key=compare_key, reverse=True)
        return nums[k - 1]


class SolutionConvert:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        Convert to integers for comparison.
        """
        nums.sort(key=int, reverse=True)
        return nums[k - 1]


class SolutionHeap:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        Use min heap of size k.
        """
        def compare_key(s: str) -> tuple:
            return (len(s), s)

        heap = []

        for num in nums:
            key = compare_key(num)

            if len(heap) < k:
                heapq.heappush(heap, (key, num))
            elif key > heap[0][0]:
                heapq.heapreplace(heap, (key, num))

        return heap[0][1]


class SolutionQuickSelect:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        QuickSelect approach (average O(n)).
        """
        import random

        def compare(a: str, b: str) -> int:
            """Returns positive if a > b, negative if a < b, 0 if equal."""
            if len(a) != len(b):
                return len(a) - len(b)
            if a > b:
                return 1
            elif a < b:
                return -1
            return 0

        def partition(left: int, right: int) -> int:
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            store_idx = left
            for i in range(left, right):
                if compare(nums[i], pivot) > 0:  # nums[i] > pivot
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            return store_idx

        left, right = 0, len(nums) - 1
        target = k - 1

        while left <= right:
            pivot_idx = partition(left, right)

            if pivot_idx == target:
                return nums[pivot_idx]
            elif pivot_idx < target:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1

        return nums[target]
