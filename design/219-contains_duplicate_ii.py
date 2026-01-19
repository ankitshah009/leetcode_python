#219. Contains Duplicate II
#Easy
#
#Given an integer array nums and an integer k, return true if there are two
#distinct indices i and j in the array such that nums[i] == nums[j] and
#abs(i - j) <= k.
#
#Example 1:
#Input: nums = [1,2,3,1], k = 3
#Output: true
#
#Example 2:
#Input: nums = [1,0,1,1], k = 1
#Output: true
#
#Example 3:
#Input: nums = [1,2,3,1,2,3], k = 2
#Output: false
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^9 <= nums[i] <= 10^9
#    0 <= k <= 10^5

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """Hash map storing last seen index"""
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i

        return False


class SolutionSlidingWindow:
    """Sliding window using set - O(n) time, O(k) space"""

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)

            # Maintain window size of k
            if len(window) > k:
                window.remove(nums[i - k])

        return False


class SolutionDeque:
    """Using deque for sliding window"""

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import deque

        if k == 0:
            return False

        window = deque()
        window_set = set()

        for num in nums:
            if num in window_set:
                return True

            window.append(num)
            window_set.add(num)

            if len(window) > k:
                removed = window.popleft()
                window_set.remove(removed)

        return False
