#532. K-diff Pairs in an Array
#Medium
#
#Given an array of integers nums and an integer k, return the number of unique
#k-diff pairs in the array.
#
#A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
#- 0 <= i, j < nums.length
#- i != j
#- |nums[i] - nums[j]| == k
#
#Notice that |val| denotes the absolute value of val.
#
#Example 1:
#Input: nums = [3,1,4,1,5], k = 2
#Output: 2
#Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
#
#Example 2:
#Input: nums = [1,2,3,4,5], k = 1
#Output: 4
#
#Example 3:
#Input: nums = [1,3,1,5,4], k = 0
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -10^7 <= nums[i] <= 10^7
#    0 <= k <= 10^7

from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """Using hash map"""
        count = Counter(nums)
        result = 0

        for num in count:
            if k > 0 and num + k in count:
                result += 1
            elif k == 0 and count[num] > 1:
                result += 1

        return result


class SolutionTwoPointers:
    """Two pointers on sorted array"""

    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = 1
        result = 0

        while left < n and right < n:
            if left == right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                result += 1
                left += 1
                # Skip duplicates
                while left < n and nums[left] == nums[left - 1]:
                    left += 1

        return result


class SolutionSet:
    """Using two sets"""

    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        seen = set()
        pairs = set()

        for num in nums:
            if num - k in seen:
                pairs.add((num - k, num))
            if num + k in seen:
                pairs.add((num, num + k))
            seen.add(num)

        return len(pairs)
