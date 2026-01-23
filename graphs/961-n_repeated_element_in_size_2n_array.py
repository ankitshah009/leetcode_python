#961. N-Repeated Element in Size 2N Array
#Easy
#
#You are given an integer array nums with the following properties:
#- nums.length == 2 * n.
#- nums contains n + 1 unique elements.
#- Exactly one element of nums is repeated n times.
#
#Return the element that is repeated n times.
#
#Example 1:
#Input: nums = [1,2,3,3]
#Output: 3
#
#Example 2:
#Input: nums = [2,1,2,5,3,2]
#Output: 2
#
#Example 3:
#Input: nums = [5,1,5,2,5,3,5,4]
#Output: 5
#
#Constraints:
#    2 <= n <= 5000
#    nums.length == 2 * n
#    0 <= nums[i] <= 10^4
#    nums contains n + 1 unique elements, one repeated n times.

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        """
        Use set to find first duplicate.
        """
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        return -1


class SolutionCounter:
    """Using Counter"""

    def repeatedNTimes(self, nums: list[int]) -> int:
        from collections import Counter

        count = Counter(nums)
        n = len(nums) // 2

        for num, cnt in count.items():
            if cnt == n:
                return num

        return -1


class SolutionCompare:
    """Check nearby elements"""

    def repeatedNTimes(self, nums: list[int]) -> int:
        # If repeated n times in 2n array, must appear in adjacent positions
        # or with gap of at most 2
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]

        for i in range(n - 2):
            if nums[i] == nums[i + 2]:
                return nums[i]

        # Must be in positions 0 and n-1
        return nums[0]


class SolutionRandom:
    """Random sampling"""

    def repeatedNTimes(self, nums: list[int]) -> int:
        import random

        while True:
            i, j = random.sample(range(len(nums)), 2)
            if nums[i] == nums[j]:
                return nums[i]
