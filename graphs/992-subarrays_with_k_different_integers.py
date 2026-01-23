#992. Subarrays with K Different Integers
#Hard
#
#Given an integer array nums and an integer k, return the number of good
#subarrays of nums.
#
#A good subarray is a subarray where the number of different integers is exactly k.
#
#Example 1:
#Input: nums = [1,2,1,2,3], k = 2
#Output: 7
#Explanation: Subarrays with exactly 2 distinct: [1,2], [2,1], [1,2], [2,3],
#[1,2,1], [2,1,2], [1,2,1,2].
#
#Example 2:
#Input: nums = [1,2,1,3,4], k = 3
#Output: 3
#
#Constraints:
#    1 <= nums.length <= 2 * 10^4
#    1 <= nums[i], k <= nums.length

from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        exactly(k) = atMost(k) - atMost(k-1)
        """
        def atMost(k):
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

        return atMost(k) - atMost(k - 1)


class SolutionTwoPointers:
    """Two pointers tracking range"""

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        result = 0

        # left1: leftmost position with k distinct
        # left2: leftmost position with k-1 distinct
        left1 = left2 = 0
        distinct1 = distinct2 = 0

        for right in range(n):
            # Update left1 (at most k distinct)
            if count.get(nums[right], 0) == 0:
                distinct1 += 1
            count[nums[right]] = count.get(nums[right], 0) + 1

            while distinct1 > k:
                count[nums[left1]] -= 1
                if count[nums[left1]] == 0:
                    distinct1 -= 1
                left1 += 1

            # Update left2 (at most k-1 distinct)
            # ... (complex, easier to use atMost approach)

        return result


class SolutionExplicit:
    """More explicit sliding window"""

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def count_at_most_k(nums, k):
            n = len(nums)
            count = {}
            left = 0
            result = 0

            for right in range(n):
                count[nums[right]] = count.get(nums[right], 0) + 1

                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1

                result += right - left + 1

            return result

        return count_at_most_k(nums, k) - count_at_most_k(nums, k - 1)
