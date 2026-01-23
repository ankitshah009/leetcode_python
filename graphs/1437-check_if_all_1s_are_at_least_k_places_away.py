#1437. Check If All 1's Are at Least Length K Places Away
#Easy
#
#Given an binary array nums and an integer k, return true if all 1's are at
#least k places away from each other, otherwise return false.
#
#Example 1:
#Input: nums = [1,0,0,0,1,0,0,1], k = 2
#Output: true
#Explanation: Each of the 1s are at least 2 places away from each other.
#
#Example 2:
#Input: nums = [1,0,0,1,0,1], k = 2
#Output: false
#Explanation: The second and third 1s are only one apart from each other.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= k <= nums.length
#    nums[i] is 0 or 1

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """
        Track position of last 1 seen.
        Check if distance to current 1 is at least k.
        """
        last_one = -k - 1  # Initialize to ensure first 1 passes

        for i, num in enumerate(nums):
            if num == 1:
                if i - last_one <= k:
                    return False
                last_one = i

        return True


class SolutionCount:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """Count zeros between consecutive 1s"""
        zeros_count = k  # Start with enough to pass first 1

        for num in nums:
            if num == 1:
                if zeros_count < k:
                    return False
                zeros_count = 0
            else:
                zeros_count += 1

        return True


class SolutionIndices:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """Collect indices of 1s, then check differences"""
        ones = [i for i, num in enumerate(nums) if num == 1]

        for i in range(1, len(ones)):
            if ones[i] - ones[i - 1] <= k:
                return False

        return True


class SolutionOneLiner:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """Pythonic approach using string operations"""
        # Convert to string, split by 1s, check lengths of 0-runs
        s = ''.join(map(str, nums))
        parts = s.split('1')

        # Middle parts (between 1s) must have length >= k
        return all(len(part) >= k for part in parts[1:-1])
