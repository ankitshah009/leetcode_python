#260. Single Number III
#Medium
#
#Given an integer array nums, in which exactly two elements appear only once
#and all the other elements appear exactly twice. Find the two elements that
#appear only once. You can return the answer in any order.
#
#You must write an algorithm that runs in linear runtime complexity and uses
#only constant extra space.
#
#Example 1:
#Input: nums = [1,2,1,3,2,5]
#Output: [3,5]
#Explanation: [5, 3] is also a valid answer.
#
#Example 2:
#Input: nums = [-1,0]
#Output: [-1,0]
#
#Example 3:
#Input: nums = [0,1]
#Output: [1,0]
#
#Constraints:
#    2 <= nums.length <= 3 * 10^4
#    -2^31 <= nums[i] <= 2^31 - 1
#    Each integer in nums will appear twice, only two integers will appear once.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Bit manipulation approach.
        1. XOR all numbers: result is a XOR b (the two unique numbers)
        2. Find any set bit in the XOR (use rightmost: x & -x)
        3. Divide numbers into two groups based on that bit
        4. XOR each group to get the two unique numbers
        """
        # Step 1: XOR of all numbers gives a ^ b
        xor_all = 0
        for num in nums:
            xor_all ^= num

        # Step 2: Find rightmost set bit (this bit differs between a and b)
        # x & -x isolates the rightmost set bit
        rightmost_bit = xor_all & (-xor_all)

        # Step 3 & 4: Divide and XOR
        num1 = num2 = 0
        for num in nums:
            if num & rightmost_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


class SolutionCounter:
    """Using Counter - O(n) space"""

    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        return [num for num, count in counts.items() if count == 1]


class SolutionSet:
    """Using set operations - O(n) space"""

    def singleNumber(self, nums: List[int]) -> List[int]:
        seen_once = set()

        for num in nums:
            if num in seen_once:
                seen_once.remove(num)
            else:
                seen_once.add(num)

        return list(seen_once)
