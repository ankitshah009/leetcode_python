#645. Set Mismatch
#Easy
#
#You have a set of integers s, which originally contains all the numbers from 1 to n.
#Unfortunately, due to some error, one of the numbers in s got duplicated to another
#number in the set, which results in repetition of one number and loss of another number.
#
#You are given an integer array nums representing the data status of this set after
#the error.
#
#Find the number that occurs twice and the number that is missing and return them
#in the form of an array.
#
#Example 1:
#Input: nums = [1,2,2,4]
#Output: [2,3]
#
#Example 2:
#Input: nums = [1,1]
#Output: [1,2]
#
#Constraints:
#    2 <= nums.length <= 10^4
#    1 <= nums[i] <= nums.length

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """Using set and sum"""
        n = len(nums)
        total = n * (n + 1) // 2
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))

        duplicate = actual_sum - unique_sum
        missing = total - unique_sum

        return [duplicate, missing]


class SolutionMarking:
    """In-place marking"""

    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        missing = -1

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                duplicate = abs(num)
            else:
                nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]


class SolutionXOR:
    """XOR approach"""

    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # XOR all numbers and indices
        xor_all = 0
        for i in range(n):
            xor_all ^= nums[i] ^ (i + 1)

        # xor_all = duplicate ^ missing

        # Find rightmost set bit
        rightmost_bit = xor_all & (-xor_all)

        # Partition into two groups
        a = b = 0
        for i in range(n):
            if nums[i] & rightmost_bit:
                a ^= nums[i]
            else:
                b ^= nums[i]

            if (i + 1) & rightmost_bit:
                a ^= (i + 1)
            else:
                b ^= (i + 1)

        # Determine which is duplicate and which is missing
        for num in nums:
            if num == a:
                return [a, b]

        return [b, a]


class SolutionCount:
    """Using count array"""

    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n + 1)

        for num in nums:
            count[num] += 1

        duplicate = missing = -1
        for i in range(1, n + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i

        return [duplicate, missing]
