#891. Sum of Subsequence Widths
#Hard
#
#The width of a sequence is the difference between the maximum and minimum
#elements in the sequence.
#
#Given an array of integers nums, return the sum of the widths of all the
#non-empty subsequences of nums. Since the answer may be very large, return it
#modulo 10^9 + 7.
#
#A subsequence is a sequence that can be derived from an array by deleting some
#or no elements without changing the order of the remaining elements.
#
#Example 1:
#Input: nums = [2,1,3]
#Output: 6
#Explanation: Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
#Widths are 0, 0, 0, 1, 1, 2, 2. Sum = 6.
#
#Example 2:
#Input: nums = [2]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^5

class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        """
        Sort the array. For element at index i:
        - It's the max in 2^i subsequences (choosing any subset from left)
        - It's the min in 2^(n-1-i) subsequences (choosing any subset from right)
        Contribution = nums[i] * (2^i - 2^(n-1-i))
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        result = 0
        for i in range(n):
            # As max: contributes nums[i] * 2^i
            # As min: contributes -nums[i] * 2^(n-1-i)
            result = (result + nums[i] * (pow2[i] - pow2[n - 1 - i])) % MOD

        return result


class SolutionOptimized:
    """Optimized computation"""

    def sumSubseqWidths(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        result = 0
        p = 1  # 2^i

        for i in range(n):
            result = (result + nums[i] * p - nums[n - 1 - i] * p) % MOD
            p = (p * 2) % MOD

        return result
