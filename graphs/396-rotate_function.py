#396. Rotate Function
#Medium
#
#You are given an integer array nums of length n.
#
#Assume arrk to be an array obtained by rotating nums by k positions
#clock-wise. We define the rotation function F on nums as follow:
#
#F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
#
#Return the maximum value of F(0), F(1), ..., F(n-1).
#
#Example 1:
#Input: nums = [4,3,2,6]
#Output: 26
#Explanation:
#F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
#F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
#F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
#F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
#So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
#
#Example 2:
#Input: nums = [100]
#Output: 0
#
#Constraints:
#    n == nums.length
#    1 <= n <= 10^5
#    -100 <= nums[i] <= 100

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        Mathematical approach.
        F(k) - F(k-1) = sum(nums) - n * nums[n-k]

        So: F(k) = F(k-1) + sum(nums) - n * nums[n-k]
        """
        n = len(nums)
        total = sum(nums)

        # Calculate F(0)
        f = sum(i * num for i, num in enumerate(nums))
        max_f = f

        for k in range(1, n):
            # F(k) = F(k-1) + sum - n * nums[n-k]
            f = f + total - n * nums[n - k]
            max_f = max(max_f, f)

        return max_f


class SolutionBruteForce:
    """Brute force O(n^2) - for reference"""

    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        max_f = float('-inf')

        for k in range(n):
            f = sum(i * nums[(i - k) % n] for i in range(n))
            max_f = max(max_f, f)

        return max_f


class SolutionDetailed:
    """More detailed derivation"""

    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        Derivation:
        F(0) = 0*A[0] + 1*A[1] + 2*A[2] + ... + (n-1)*A[n-1]
        F(1) = 0*A[n-1] + 1*A[0] + 2*A[1] + ... + (n-1)*A[n-2]

        F(1) - F(0) = A[0] + A[1] + ... + A[n-2] - (n-1)*A[n-1]
                    = (A[0] + A[1] + ... + A[n-1]) - n*A[n-1]
                    = sum - n*A[n-1]

        General: F(k) = F(k-1) + sum - n*A[n-k]
        """
        n = len(nums)
        if n == 0:
            return 0

        total_sum = sum(nums)
        f_prev = sum(i * nums[i] for i in range(n))
        max_f = f_prev

        for k in range(1, n):
            f_curr = f_prev + total_sum - n * nums[n - k]
            max_f = max(max_f, f_curr)
            f_prev = f_curr

        return max_f
