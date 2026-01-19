#324. Wiggle Sort II
#Medium
#
#Given an integer array nums, reorder it such that
#nums[0] < nums[1] > nums[2] < nums[3]....
#
#You may assume the input array always has a valid answer.
#
#Example 1:
#Input: nums = [1,5,1,1,6,4]
#Output: [1,6,1,5,1,4]
#Explanation: [1,4,1,5,1,6] is also accepted.
#
#Example 2:
#Input: nums = [1,3,2,2,3,1]
#Output: [2,3,1,3,1,2]
#
#Constraints:
#    1 <= nums.length <= 5 * 10^4
#    0 <= nums[i] <= 5000
#    It is guaranteed that there will be an answer for the given input nums.
#
#Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?

from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Sort and interleave approach.
        Modify nums in-place.
        """
        n = len(nums)
        sorted_nums = sorted(nums)

        # Fill odd indices with larger half (reversed)
        # Fill even indices with smaller half (reversed)
        j = n - 1  # Larger half starts from end
        k = (n - 1) // 2  # Smaller half

        for i in range(1, n, 2):
            nums[i] = sorted_nums[j]
            j -= 1

        for i in range(0, n, 2):
            nums[i] = sorted_nums[k]
            k -= 1


class SolutionQuickSelect:
    """O(n) time using quickselect and virtual indexing"""

    def wiggleSort(self, nums: List[int]) -> None:
        import random

        n = len(nums)

        # Find median using quickselect
        def quickselect(arr, k):
            pivot = random.choice(arr)
            left = [x for x in arr if x < pivot]
            mid = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]

            if k < len(left):
                return quickselect(left, k)
            elif k < len(left) + len(mid):
                return pivot
            else:
                return quickselect(right, k - len(left) - len(mid))

        median = quickselect(nums[:], n // 2)

        # Virtual index mapping for wiggle pattern
        def new_index(i):
            return (1 + 2 * i) % (n | 1)

        # Three-way partition around median
        i, j, k = 0, 0, n - 1

        while j <= k:
            if nums[new_index(j)] > median:
                nums[new_index(i)], nums[new_index(j)] = nums[new_index(j)], nums[new_index(i)]
                i += 1
                j += 1
            elif nums[new_index(j)] < median:
                nums[new_index(j)], nums[new_index(k)] = nums[new_index(k)], nums[new_index(j)]
                k -= 1
            else:
                j += 1


class SolutionSimple:
    """Simple approach with sorting"""

    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2

        # Split into two halves
        small = nums[:half][::-1]
        large = nums[half:][::-1]

        # Interleave
        for i in range(n):
            if i % 2 == 0:
                nums[i] = small[i // 2]
            else:
                nums[i] = large[i // 2]
