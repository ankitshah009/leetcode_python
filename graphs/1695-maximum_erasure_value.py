#1695. Maximum Erasure Value
#Medium
#
#You are given an array of positive integers nums and want to erase a subarray
#containing unique elements. The score you get by erasing the subarray is equal
#to the sum of its elements.
#
#Return the maximum score you can get by erasing exactly one subarray.
#
#A subarray is a contiguous sequence of elements.
#
#Example 1:
#Input: nums = [4,2,4,5,6]
#Output: 17
#Explanation: The optimal subarray is [2,4,5,6].
#
#Example 2:
#Input: nums = [5,2,1,2,5,2,1,2,5]
#Output: 8
#Explanation: The optimal subarray is [5,2,1] or [1,2,5].
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^4

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Sliding window with set to track unique elements.
        """
        seen = set()
        max_sum = 0
        curr_sum = 0
        left = 0

        for right, num in enumerate(nums):
            while num in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            seen.add(num)
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum


class SolutionDict:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Using dictionary to track last index of each element.
        """
        last_index = {}
        max_sum = 0
        curr_sum = 0
        left = 0

        for right, num in enumerate(nums):
            if num in last_index and last_index[num] >= left:
                # Remove elements from left to last occurrence
                while left <= last_index[num]:
                    curr_sum -= nums[left]
                    left += 1

            last_index[num] = right
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum


class SolutionPrefixSum:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Prefix sum with index tracking.
        """
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        last_seen = {}
        max_sum = 0
        left = 0

        for right in range(n):
            num = nums[right]

            if num in last_seen and last_seen[num] >= left:
                left = last_seen[num] + 1

            last_seen[num] = right
            current_sum = prefix[right + 1] - prefix[left]
            max_sum = max(max_sum, current_sum)

        return max_sum


class SolutionArray:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Using array for seen tracking (faster for small value range).
        """
        seen = [False] * 10001
        max_sum = 0
        curr_sum = 0
        left = 0

        for num in nums:
            while seen[num]:
                seen[nums[left]] = False
                curr_sum -= nums[left]
                left += 1

            seen[num] = True
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum


class SolutionCompact:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Compact sliding window.
        """
        s, left, ans, total = set(), 0, 0, 0
        for num in nums:
            while num in s:
                s.remove(nums[left])
                total -= nums[left]
                left += 1
            s.add(num)
            total += num
            ans = max(ans, total)
        return ans
