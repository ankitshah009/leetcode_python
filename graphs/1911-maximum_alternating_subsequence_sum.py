#1911. Maximum Alternating Subsequence Sum
#Medium
#
#The alternating sum of a 0-indexed array is defined as the sum of the elements
#at even indices minus the sum of the elements at odd indices.
#
#For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
#
#Given an array nums, return the maximum alternating sum of any subsequence of
#nums (after reindexing the elements of the subsequence).
#
#A subsequence of an array is a new array generated from the original array by
#deleting some elements (possibly none) without changing the remaining
#elements' relative order.
#
#Example 1:
#Input: nums = [4,2,5,3]
#Output: 7
#
#Example 2:
#Input: nums = [5,6,7,8]
#Output: 8
#
#Example 3:
#Input: nums = [6,2,1,2,4,5]
#Output: 10
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^5

from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
        DP: track max sum ending with even/odd index element.
        """
        even = 0  # Max sum if last element is at even index
        odd = 0   # Max sum if last element is at odd index

        for num in nums:
            # Can add to even position (add num) or odd position (subtract num)
            new_even = max(even, odd + num)
            new_odd = max(odd, even - num)
            even, odd = new_even, new_odd

        return even


class SolutionGreedy:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
        Greedy: sum of all increasing steps + first element.

        For alternating sum, optimal is:
        a[0] - a[1] + a[2] - a[3] + ...
        = a[0] + (a[2] - a[1]) + (a[4] - a[3]) + ...

        We want to maximize positive differences.
        """
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                result += nums[i] - nums[i - 1]

        return result


class SolutionExplained:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
        Detailed DP explanation.

        For each element, we can:
        1. Not include it
        2. Include it at even position (add to sum)
        3. Include it at odd position (subtract from sum)

        even[i] = max alternating sum using nums[0:i+1] with last elem at even idx
        odd[i] = max alternating sum using nums[0:i+1] with last elem at odd idx

        Transitions:
        even[i] = max(even[i-1], odd[i-1] + nums[i])
        odd[i] = max(odd[i-1], even[i-1] - nums[i])
        """
        even = 0
        odd = float('-inf')  # Can't end at odd position initially

        for num in nums:
            even, odd = max(even, odd + num), max(odd, even - num)

        return even
