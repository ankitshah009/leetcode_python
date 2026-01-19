#560. Subarray Sum Equals K
#Medium
#
#Given an array of integers nums and an integer k, return the total number of subarrays whose
#sum equals to k.
#
#A subarray is a contiguous non-empty sequence of elements within an array.
#
#Example 1:
#Input: nums = [1,1,1], k = 2
#Output: 2
#
#Example 2:
#Input: nums = [1,2,3], k = 3
#Output: 2
#
#Constraints:
#    1 <= nums.length <= 2 * 10^4
#    -1000 <= nums[i] <= 1000
#    -10^7 <= k <= 10^7

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        for num in nums:
            prefix_sum += num

            # Check if prefix_sum - k exists
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] += 1

        return count
