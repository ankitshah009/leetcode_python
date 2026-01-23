#1060. Missing Element in Sorted Array
#Medium
#
#Given an integer array nums which is sorted in ascending order and all of
#its elements are unique and given also an integer k, return the kth missing
#number starting from the leftmost number of the array.
#
#Example 1:
#Input: nums = [4,7,9,10], k = 1
#Output: 5
#Explanation: The first missing number is 5.
#
#Example 2:
#Input: nums = [4,7,9,10], k = 3
#Output: 8
#Explanation: The missing numbers are [5,6,8,...], hence the third missing
#number is 8.
#
#Example 3:
#Input: nums = [1,2,4], k = 3
#Output: 6
#Explanation: The missing numbers are [3,5,6,7,...], hence the third missing
#number is 6.
#
#Constraints:
#    1 <= nums.length <= 5 * 10^4
#    1 <= nums[i] <= 10^7
#    nums is sorted in ascending order, and all the elements are unique.
#    1 <= k <= 10^8

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        """
        Binary search on number of missing elements.
        missing_count(i) = nums[i] - nums[0] - i
        """
        def missing_count(idx):
            # Number of missing elements before nums[idx]
            return nums[idx] - nums[0] - idx

        n = len(nums)

        # If k is larger than all missing in array
        if k > missing_count(n - 1):
            return nums[-1] + k - missing_count(n - 1)

        # Binary search for the index where missing count >= k
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if missing_count(mid) < k:
                left = mid + 1
            else:
                right = mid

        # Answer is between nums[left-1] and nums[left]
        # k - missing_count(left-1) more after nums[left-1]
        return nums[left - 1] + k - missing_count(left - 1)


class SolutionLinear:
    def missingElement(self, nums: List[int], k: int) -> int:
        """Linear scan - O(n) time"""
        for i in range(len(nums) - 1):
            missing_between = nums[i + 1] - nums[i] - 1
            if missing_between >= k:
                return nums[i] + k
            k -= missing_between

        # k missing numbers after the last element
        return nums[-1] + k


class SolutionSimple:
    def missingElement(self, nums: List[int], k: int) -> int:
        """Simple binary search formulation"""
        def missing(idx):
            return nums[idx] - nums[0] - idx

        n = len(nums)
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if missing(mid) < k:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo - 1] + k - missing(lo - 1)
