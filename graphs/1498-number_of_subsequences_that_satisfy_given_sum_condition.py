#1498. Number of Subsequences That Satisfy the Given Sum Condition
#Medium
#
#You are given an array of integers nums and an integer target.
#
#Return the number of non-empty subsequences of nums such that the sum of the
#minimum and maximum element on it is less or equal to target. Since the answer
#may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: nums = [3,5,6,7], target = 9
#Output: 4
#Explanation: There are 4 subsequences that satisfy the condition.
#[3] -> Min value + max value <= target (3 + 3 <= 9)
#[3,5] -> (3 + 5 <= 9)
#[3,5,6] -> (3 + 6 <= 9)
#[3,6] -> (3 + 6 <= 9)
#
#Example 2:
#Input: nums = [3,3,6,8], target = 10
#Output: 6
#Explanation: There are 6 subsequences that satisfy the condition. (nums can
#have repeated numbers).
#[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
#
#Example 3:
#Input: nums = [2,3,3,4,6,7], target = 12
#Output: 61
#Explanation: There are 63 non-empty subsequences, two of them do not satisfy
#the condition ([6,7], [7]).
#Number of valid subsequences (63 - 2 = 61).
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^6
#    1 <= target <= 10^6

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Sort array. For each left pointer, find rightmost valid right pointer.
        All elements between can be included or excluded (except left must be included).
        Count = 2^(right - left) for each valid pair.
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        result = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                # All subsequences with nums[left] as min and any subset of [left+1, right]
                # Number of such subsequences = 2^(right - left)
                result = (result + power[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return result


class SolutionBinarySearch:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Binary search for each element to find rightmost valid max.
        """
        import bisect

        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD

        result = 0

        for i in range(n):
            # Find largest j such that nums[i] + nums[j] <= target
            max_val = target - nums[i]
            if nums[i] > max_val:
                break  # nums[i] + nums[i] > target, no valid subsequence

            j = bisect.bisect_right(nums, max_val) - 1

            if j >= i:
                # Subsequences with nums[i] as min
                result = (result + power[j - i]) % MOD

        return result


class SolutionExplained:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Detailed explanation:

        After sorting, for a subsequence to have min=nums[i] and max=nums[j],
        we need i <= j and nums[i] + nums[j] <= target.

        For fixed i, find largest j where nums[i] + nums[j] <= target.
        Then any subset of elements in [i+1, j] can be added to the subsequence.
        Number of such subsets = 2^(j-i) (including empty set means nums[i] alone).
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2
        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 2) % MOD

        result = 0
        j = n - 1

        for i in range(n):
            # Shrink j while sum exceeds target
            while j >= i and nums[i] + nums[j] > target:
                j -= 1

            if j >= i:
                # Can form subsequences with nums[i] as minimum
                # Elements in range [i+1, j] can be freely included/excluded
                # That's 2^(j-i) subsequences
                result = (result + power[j - i]) % MOD

        return result
