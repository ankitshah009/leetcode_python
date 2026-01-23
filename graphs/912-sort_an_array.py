#912. Sort an Array
#Medium
#
#Given an array of integers nums, sort the array in ascending order and return
#it. You must solve the problem without using any built-in functions in O(nlogn)
#time complexity and with the smallest space complexity possible.
#
#Example 1:
#Input: nums = [5,2,3,1]
#Output: [1,2,3,5]
#
#Example 2:
#Input: nums = [5,1,1,2,0,0]
#Output: [0,0,1,1,2,5]
#
#Constraints:
#    1 <= nums.length <= 5 * 10^4
#    -5 * 10^4 <= nums[i] <= 5 * 10^4

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        Merge sort implementation.
        """
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


class SolutionQuickSort:
    """Randomized QuickSort"""

    def sortArray(self, nums: list[int]) -> list[int]:
        import random

        def quicksort(arr: list[int], lo: int, hi: int):
            if lo >= hi:
                return

            # Random pivot to avoid worst case
            pivot_idx = random.randint(lo, hi)
            arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
            pivot = arr[hi]

            i = lo
            for j in range(lo, hi):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[hi] = arr[hi], arr[i]

            quicksort(arr, lo, i - 1)
            quicksort(arr, i + 1, hi)

        quicksort(nums, 0, len(nums) - 1)
        return nums


class SolutionHeapSort:
    """Heap Sort"""

    def sortArray(self, nums: list[int]) -> list[int]:
        def heapify(arr: list[int], n: int, i: int):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(nums)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # Extract elements
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)

        return nums


class SolutionCountingSort:
    """Counting sort for bounded integers"""

    def sortArray(self, nums: list[int]) -> list[int]:
        min_val, max_val = min(nums), max(nums)
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            count[num - min_val] += 1

        result = []
        for i, c in enumerate(count):
            result.extend([i + min_val] * c)

        return result
