#287. Find the Duplicate Number
#Medium
#
#Given an array of integers nums containing n + 1 integers where each integer
#is in the range [1, n] inclusive.
#
#There is only one repeated number in nums, return this repeated number.
#
#You must solve the problem without modifying the array nums and uses only
#constant extra space.
#
#Example 1:
#Input: nums = [1,3,4,2,2]
#Output: 2
#
#Example 2:
#Input: nums = [3,1,3,4,2]
#Output: 3
#
#Constraints:
#    1 <= n <= 10^5
#    nums.length == n + 1
#    1 <= nums[i] <= n
#    All the integers in nums appear only once except for precisely one integer
#    which appears two or more times.
#
#Follow up:
#    How can we prove that at least one duplicate number must exist in nums?
#    Can you solve the problem in linear runtime complexity?

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's Cycle Detection (Tortoise and Hare).
        Treat array as linked list where value points to next index.
        O(n) time, O(1) space.
        """
        # Phase 1: Find intersection point in cycle
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance to cycle (duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


class SolutionBinarySearch:
    """
    Binary search on value range.
    O(n log n) time, O(1) space.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            # Count numbers <= mid
            count = sum(1 for num in nums if num <= mid)

            # If count > mid, duplicate is in [left, mid]
            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left


class SolutionBitManipulation:
    """
    Bit manipulation approach.
    Compare bit counts between nums and [1, n].
    O(n log n) time, O(1) space.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        duplicate = 0

        for bit in range(32):
            mask = 1 << bit

            # Count set bits in nums
            nums_count = sum(1 for num in nums if num & mask)

            # Count set bits in [1, n]
            expected_count = sum(1 for num in range(1, n + 1) if num & mask)

            if nums_count > expected_count:
                duplicate |= mask

        return duplicate


class SolutionMarking:
    """
    Marking visited (modifies array - not allowed by problem).
    O(n) time, O(1) space but modifies input.
    """

    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]

        return -1
