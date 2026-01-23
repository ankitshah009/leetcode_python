#1365. How Many Numbers Are Smaller Than the Current Number
#Easy
#
#Given the array nums, for each nums[i] find out how many numbers in the array
#are smaller than it. That is, for each nums[i] you have to count the number
#of valid j's such that j != i and nums[j] < nums[i].
#
#Return the answer in an array.
#
#Example 1:
#Input: nums = [8,1,2,2,3]
#Output: [4,0,1,1,3]
#Explanation:
#For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
#For nums[1]=1 does not exist any smaller number than it.
#For nums[2]=2 there exist one smaller number than it (1).
#For nums[3]=2 there exist one smaller number than it (1).
#For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
#
#Example 2:
#Input: nums = [6,5,4,8]
#Output: [2,1,0,3]
#
#Example 3:
#Input: nums = [7,7,7,7]
#Output: [0,0,0,0]
#
#Constraints:
#    2 <= nums.length <= 500
#    0 <= nums[i] <= 100

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        Sort and use ranking.
        """
        # Create sorted version with original indices
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])

        result = [0] * len(nums)

        for rank, (orig_idx, val) in enumerate(sorted_nums):
            # Find first occurrence of this value in sorted order
            if rank == 0 or sorted_nums[rank - 1][1] < val:
                result[orig_idx] = rank
            else:
                # Same value as previous - use same count
                result[orig_idx] = result[sorted_nums[rank - 1][0]]

        return result


class SolutionCountingSort:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        Counting sort approach - O(n + k) where k is range of values.
        Since 0 <= nums[i] <= 100, this is efficient.
        """
        # Count occurrences
        count = [0] * 102

        for num in nums:
            count[num + 1] += 1

        # Cumulative sum gives count of smaller numbers
        for i in range(1, 102):
            count[i] += count[i - 1]

        return [count[num] for num in nums]


class SolutionBruteForce:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """O(n^2) brute force"""
        return [sum(1 for y in nums if y < x) for x in nums]
