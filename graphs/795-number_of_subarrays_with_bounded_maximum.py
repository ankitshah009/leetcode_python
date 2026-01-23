#795. Number of Subarrays with Bounded Maximum
#Medium
#
#Given an integer array nums and two integers left and right, return the number
#of contiguous non-empty subarrays such that the value of the maximum array
#element in that subarray is in the range [left, right].
#
#The test cases are generated so that the answer will fit in a 32-bit integer.
#
#Example 1:
#Input: nums = [2,1,4,3], left = 2, right = 3
#Output: 3
#Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
#
#Example 2:
#Input: nums = [2,9,2,5,6], left = 2, right = 8
#Output: 7
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^9
#    0 <= left <= right <= 10^9

class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        """
        Count subarrays with max <= right minus subarrays with max < left.
        """
        def count_at_most(bound):
            """Count subarrays where all elements <= bound"""
            count = 0
            length = 0
            for num in nums:
                if num <= bound:
                    length += 1
                else:
                    length = 0
                count += length
            return count

        return count_at_most(right) - count_at_most(left - 1)


class SolutionDirect:
    """Direct counting approach"""

    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        result = 0
        start = -1  # Start of valid window
        last_valid = -1  # Last index where left <= nums[i] <= right

        for i, num in enumerate(nums):
            if num > right:
                # Reset window
                start = i
                last_valid = i
            elif num >= left:
                # num is in [left, right]
                last_valid = i

            # All subarrays ending at i starting from (start+1) to last_valid
            if last_valid > start:
                result += last_valid - start

        return result


class SolutionTwoPointer:
    """Two pointer with explicit window"""

    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        n = len(nums)
        result = 0
        j = -1  # Last index with value > right
        k = -1  # Last index with value >= left

        for i in range(n):
            if nums[i] > right:
                j = i
            if nums[i] >= left:
                k = i

            # Subarrays ending at i with max in [left, right]
            # Must start after j and include at least one element >= left
            result += max(0, k - j)

        return result
