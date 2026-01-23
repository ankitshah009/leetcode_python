#1248. Count Number of Nice Subarrays
#Medium
#
#Given an array of integers nums and an integer k. A continuous subarray is
#called nice if there are k odd numbers on it.
#
#Return the number of nice sub-arrays.
#
#Example 1:
#Input: nums = [1,1,2,1,1], k = 3
#Output: 2
#Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
#
#Example 2:
#Input: nums = [2,4,6], k = 1
#Output: 0
#Explanation: There are no odd numbers in the array.
#
#Example 3:
#Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
#Output: 16
#
#Constraints:
#    1 <= nums.length <= 50000
#    1 <= nums[i] <= 10^5
#    1 <= k <= nums.length

from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Transform: Replace even with 0, odd with 1.
        Problem becomes: count subarrays with sum = k.
        Use prefix sum and hash map.
        """
        count = defaultdict(int)
        count[0] = 1  # Empty prefix has 0 odd numbers

        prefix = 0
        result = 0

        for num in nums:
            prefix += num % 2  # 1 if odd, 0 if even

            # Subarrays ending here with exactly k odd numbers
            if prefix - k in count:
                result += count[prefix - k]

            count[prefix] += 1

        return result


class SolutionSlidingWindow:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        atMost(k) - atMost(k-1) gives exactly k.
        """
        def at_most(k):
            count = 0
            left = 0
            odd = 0

            for right in range(len(nums)):
                odd += nums[right] % 2

                while odd > k:
                    odd -= nums[left] % 2
                    left += 1

                count += right - left + 1

            return count

        return at_most(k) - at_most(k - 1)


class SolutionThreePointers:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Three pointers approach.
        For each right, find range of valid lefts.
        """
        n = len(nums)
        result = 0
        odd = 0
        left = 0
        count = 0  # Count of even numbers at start of current window

        for right in range(n):
            if nums[right] % 2 == 1:
                odd += 1
                count = 0  # Reset count when new odd is added

            while odd == k:
                if nums[left] % 2 == 1:
                    odd -= 1
                count += 1
                left += 1

            result += count

        return result
