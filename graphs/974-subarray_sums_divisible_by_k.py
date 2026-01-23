#974. Subarray Sums Divisible by K
#Medium
#
#Given an integer array nums and an integer k, return the number of non-empty
#subarrays that have a sum divisible by k.
#
#A subarray is a contiguous part of an array.
#
#Example 1:
#Input: nums = [4,5,0,-2,-3,1], k = 5
#Output: 7
#Explanation: There are 7 subarrays with sum divisible by k = 5:
#[4,5,0,-2,-3,1], [5], [5,0], [5,0,-2,-3], [0], [0,-2,-3], [-2,-3]
#
#Example 2:
#Input: nums = [5], k = 9
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 3 * 10^4
#    -10^4 <= nums[i] <= 10^4
#    2 <= k <= 10^4

from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """
        Count prefix sums with same remainder mod k.
        """
        count = defaultdict(int)
        count[0] = 1  # Empty prefix

        result = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            result += count[remainder]
            count[remainder] += 1

        return result


class SolutionArray:
    """Using array instead of dict"""

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = [0] * k
        count[0] = 1

        result = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            result += count[prefix_sum]
            count[prefix_sum] += 1

        return result


class SolutionCombinations:
    """Count combinations at the end"""

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = [0] * k
        prefix_sum = 0

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count[prefix_sum] += 1

        # Empty prefix has remainder 0
        count[0] += 1

        # For each remainder, count pairs: C(n, 2) = n*(n-1)/2
        result = 0
        for c in count:
            result += c * (c - 1) // 2

        return result
