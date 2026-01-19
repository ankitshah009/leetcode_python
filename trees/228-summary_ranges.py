#228. Summary Ranges
#Easy
#
#You are given a sorted unique integer array nums.
#
#A range [a,b] is the set of all integers from a to b (inclusive).
#
#Return the smallest sorted list of ranges that cover all the numbers in the
#array exactly. That is, each element of nums is covered by exactly one of the
#ranges, and there is no integer x such that x is in one of the ranges but not
#in nums.
#
#Each range [a,b] in the list should be output as:
#    "a->b" if a != b
#    "a" if a == b
#
#Example 1:
#Input: nums = [0,1,2,4,5,7]
#Output: ["0->2","4->5","7"]
#
#Example 2:
#Input: nums = [0,2,3,4,6,8,9]
#Output: ["0","2->4","6","8->9"]
#
#Constraints:
#    0 <= nums.length <= 20
#    -2^31 <= nums[i] <= 2^31 - 1
#    All the values of nums are unique.
#    nums is sorted in ascending order.

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(1, len(nums) + 1):
            # End of array or gap found
            if i == len(nums) or nums[i] != nums[i-1] + 1:
                end = nums[i-1]

                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")

                if i < len(nums):
                    start = nums[i]

        return result


class SolutionTwoPointers:
    """Two pointers approach"""

    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]

            # Find end of current range
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]

            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")

            i += 1

        return result


class SolutionGroupby:
    """Using itertools groupby"""

    def summaryRanges(self, nums: List[int]) -> List[str]:
        from itertools import groupby

        if not nums:
            return []

        result = []

        # Group consecutive numbers
        def key_func(pair):
            index, val = pair
            return val - index

        for _, group in groupby(enumerate(nums), key=key_func):
            group_list = list(group)
            start = group_list[0][1]
            end = group_list[-1][1]

            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")

        return result
