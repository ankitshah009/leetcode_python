#992. Subarrays with K Different Integers
#Hard
#
#Given an integer array nums and an integer k, return the number of good subarrays of nums.
#
#A good array is an array where the number of different integers in that array is exactly k.
#
#For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
#A subarray is a contiguous part of an array.
#
#Example 1:
#Input: nums = [1,2,1,2,3], k = 2
#Output: 7
#Explanation: Subarrays formed with exactly 2 different integers:
#[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
#
#Example 2:
#Input: nums = [1,2,1,3,4], k = 3
#Output: 3
#Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
#
#Constraints:
#    1 <= nums.length <= 2 * 10^4
#    1 <= nums[i], k <= nums.length

from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Exactly k = at most k - at most (k-1)
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums, k):
        count = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(nums)):
            if count[nums[right]] == 0:
                k -= 1
            count[nums[right]] += 1

            while k < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    k += 1
                left += 1

            result += right - left + 1

        return result
