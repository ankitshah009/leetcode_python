#713. Subarray Product Less Than K
#Medium
#
#Given an array of integers nums and an integer k, return the number of
#contiguous subarrays where the product of all the elements in the subarray
#is strictly less than k.
#
#Example 1:
#Input: nums = [10,5,2,6], k = 100
#Output: 8
#Explanation: The 8 subarrays that have product less than 100 are:
#[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
#Note that [10, 5, 2] is not included as the product of 100 is not strictly
#less than k.
#
#Example 2:
#Input: nums = [1,2,3], k = 0
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 3 * 10^4
#    1 <= nums[i] <= 1000
#    0 <= k <= 10^6

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        """
        Sliding window: maintain window with product < k.
        Each position adds (right - left + 1) new subarrays.
        """
        if k <= 1:
            return 0

        count = 0
        product = 1
        left = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            # All subarrays ending at right with start in [left, right]
            count += right - left + 1

        return count


class SolutionBinarySearch:
    """Binary search with prefix log-sums"""

    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        import math
        import bisect

        if k <= 1:
            return 0

        log_k = math.log(k)
        n = len(nums)

        # Prefix log sums
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + math.log(num))

        count = 0
        for i in range(n):
            # Find rightmost j where prefix[j+1] - prefix[i] < log_k
            target = prefix[i] + log_k
            j = bisect.bisect_left(prefix, target, i + 1, n + 1) - 1
            count += max(0, j - i)

        return count


class SolutionExplicit:
    """More explicit sliding window"""

    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        count = 0
        product = 1
        left = 0

        for right in range(n):
            product *= nums[right]

            # Shrink window until product < k
            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            # Count subarrays ending at right
            if left <= right:
                count += right - left + 1
            elif product < k:  # left > right but single element valid
                count += 1

        return count
