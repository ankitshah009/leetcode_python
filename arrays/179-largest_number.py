#179. Largest Number
#Medium
#
#Given a list of non-negative integers nums, arrange them such that they form
#the largest number and return it.
#
#Since the result may be very large, you need to return a string instead of
#an integer.
#
#Example 1:
#Input: nums = [10, 2]
#Output: "210"
#
#Example 2:
#Input: nums = [3, 30, 34, 5, 9]
#Output: "9534330"
#
#Constraints:
#    1 <= nums.length <= 100
#    0 <= nums[i] <= 10^9

from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator: compare concatenations
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            return 0

        # Convert to strings
        strs = [str(num) for num in nums]

        # Sort with custom comparator
        strs.sort(key=cmp_to_key(compare))

        # Handle edge case of all zeros
        if strs[0] == '0':
            return '0'

        return ''.join(strs)


class SolutionCustomKey:
    """Using a custom key class"""

    def largestNumber(self, nums: List[int]) -> str:
        class LargerNumKey(str):
            def __lt__(x, y):
                return x + y > y + x

        strs = [str(num) for num in nums]
        strs.sort(key=LargerNumKey)

        result = ''.join(strs)
        return '0' if result[0] == '0' else result


class SolutionRepeat:
    """Using string repetition for comparison"""

    def largestNumber(self, nums: List[int]) -> str:
        # Repeat string enough times to compare properly
        # Max number has 10 digits, so repeat 10 times
        strs = [str(num) for num in nums]
        strs.sort(key=lambda x: x * 10, reverse=True)

        result = ''.join(strs)
        return '0' if result[0] == '0' else result
