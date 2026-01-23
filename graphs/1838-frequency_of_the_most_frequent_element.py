#1838. Frequency of the Most Frequent Element
#Medium
#
#The frequency of an element is the number of times it occurs in an array.
#
#You are given an integer array nums and an integer k. In one operation, you
#can choose an index of nums and increment the element at that index by 1.
#
#Return the maximum possible frequency of an element after performing at most k
#operations.
#
#Example 1:
#Input: nums = [1,2,4], k = 5
#Output: 3
#Explanation: Increment 1 twice and 2 once to make nums = [4,4,4].
#
#Example 2:
#Input: nums = [1,4,8,13], k = 5
#Output: 2
#
#Example 3:
#Input: nums = [3,9,6], k = 2
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^5
#    1 <= k <= 10^5

from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Sliding window: after sorting, try to make all elements in window
        equal to the rightmost element.
        """
        nums.sort()
        n = len(nums)

        left = 0
        total = 0
        max_freq = 1

        for right in range(n):
            total += nums[right]

            # Cost to make all elements in [left, right] equal to nums[right]
            # = nums[right] * window_size - sum of window
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq


class SolutionBinarySearch:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Binary search on frequency.
        """
        nums.sort()
        n = len(nums)

        # Prefix sum for fast range sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def can_achieve(freq: int) -> bool:
            """Check if we can achieve frequency 'freq'."""
            for i in range(freq - 1, n):
                # Window [i - freq + 1, i]
                left = i - freq + 1
                window_sum = prefix[i + 1] - prefix[left]
                # Cost to make all equal to nums[i]
                cost = nums[i] * freq - window_sum
                if cost <= k:
                    return True
            return False

        # Binary search on answer
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_achieve(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo


class SolutionSimple:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Simplified sliding window tracking window sum.
        """
        nums.sort()
        left = 0
        window_sum = 0
        result = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            # Shrink window if cost exceeds k
            while nums[right] * (right - left + 1) > window_sum + k:
                window_sum -= nums[left]
                left += 1

            result = max(result, right - left + 1)

        return result
