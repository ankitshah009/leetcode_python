#918. Maximum Sum Circular Subarray
#Medium
#
#Given a circular integer array nums of length n, return the maximum possible
#sum of a non-empty subarray of nums.
#
#A circular array means the end of the array connects to the beginning. A
#subarray may only include each element of the fixed buffer nums at most once.
#
#Example 1:
#Input: nums = [1,-2,3,-2]
#Output: 3
#Explanation: Subarray [3] has maximum sum 3.
#
#Example 2:
#Input: nums = [5,-3,5]
#Output: 10
#Explanation: Subarray [5,5] wrapping around.
#
#Example 3:
#Input: nums = [-3,-2,-3]
#Output: -2
#Explanation: Subarray [-2] has maximum sum -2.
#
#Constraints:
#    n == nums.length
#    1 <= n <= 3 * 10^4
#    -3 * 10^4 <= nums[i] <= 3 * 10^4

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        Max circular = max(normal max subarray, total - min subarray)
        Edge case: if all negative, return max element.
        """
        total = 0
        max_sum = nums[0]
        min_sum = nums[0]
        cur_max = 0
        cur_min = 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)

            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)

            total += num

        # If all negative, max_sum is the answer
        # Otherwise, compare normal max with circular max
        if max_sum <= 0:
            return max_sum

        return max(max_sum, total - min_sum)


class SolutionExplicit:
    """More explicit Kadane"""

    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        def kadane_max(arr):
            max_ending = max_so_far = arr[0]
            for x in arr[1:]:
                max_ending = max(x, max_ending + x)
                max_so_far = max(max_so_far, max_ending)
            return max_so_far

        def kadane_min(arr):
            min_ending = min_so_far = arr[0]
            for x in arr[1:]:
                min_ending = min(x, min_ending + x)
                min_so_far = min(min_so_far, min_ending)
            return min_so_far

        max_normal = kadane_max(nums)
        min_subarray = kadane_min(nums)
        total = sum(nums)

        # All elements negative
        if total == min_subarray:
            return max_normal

        return max(max_normal, total - min_subarray)


class SolutionPrefixSum:
    """Using prefix sums with deque"""

    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        from collections import deque

        n = len(nums)
        # Duplicate array
        doubled = nums + nums

        # Prefix sums
        prefix = [0] * (2 * n + 1)
        for i in range(2 * n):
            prefix[i + 1] = prefix[i] + doubled[i]

        # Find max subarray of length at most n using monotonic deque
        result = nums[0]
        dq = deque([0])

        for i in range(1, 2 * n + 1):
            # Remove indices out of window
            while dq and dq[0] < i - n:
                dq.popleft()

            result = max(result, prefix[i] - prefix[dq[0]])

            # Maintain monotonic increasing deque
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)

        return result
