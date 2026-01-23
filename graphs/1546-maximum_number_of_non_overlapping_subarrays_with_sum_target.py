#1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
#Medium
#
#Given an array nums and an integer target, return the maximum number of
#non-empty non-overlapping subarrays such that the sum of values in each
#subarray is equal to target.
#
#Example 1:
#Input: nums = [1,1,1,1,1], target = 2
#Output: 2
#Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals
#to target(2).
#
#Example 2:
#Input: nums = [-1,3,5,1,4,2,-9], target = 6
#Output: 2
#Explanation: There are 3 subarrays with sum equal to 6.
#([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
#
#Example 3:
#Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
#Output: 3
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4
#    0 <= target <= 10^6

from typing import List

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """
        Greedy approach: Find subarrays ending as early as possible.

        Use prefix sum with hash set.
        When we find a valid subarray, reset and start fresh.
        """
        count = 0
        prefix_sum = 0
        seen = {0}  # Set of prefix sums we've seen

        for num in nums:
            prefix_sum += num

            if prefix_sum - target in seen:
                # Found a valid subarray ending here
                count += 1
                # Reset - start fresh from next position
                prefix_sum = 0
                seen = {0}
            else:
                seen.add(prefix_sum)

        return count


class SolutionDP:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """
        DP approach: dp[i] = max subarrays using nums[0:i]
        """
        n = len(nums)

        # Map from prefix_sum to the index where it was achieved
        prefix_map = {0: 0}
        prefix_sum = 0

        # dp[i] = max non-overlapping subarrays in nums[0:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_sum += nums[i - 1]

            # Inherit from previous
            dp[i] = dp[i - 1]

            # Check if we can end a subarray here
            need = prefix_sum - target
            if need in prefix_map:
                j = prefix_map[need]
                dp[i] = max(dp[i], dp[j] + 1)

            prefix_map[prefix_sum] = i

        return dp[n]


class SolutionGreedyExplained:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """
        Greedy with explanation.

        Key insight: When we find a valid subarray ending at position i,
        it's always optimal to take it (greedy choice).

        After taking a subarray, we reset because:
        - Any subarray starting before our taken one would overlap
        - We want to maximize count, so taking early is best
        """
        count = 0
        current_sum = 0
        prefix_sums = {0}

        for num in nums:
            current_sum += num

            # Check if subarray ending here has sum = target
            if current_sum - target in prefix_sums:
                count += 1
                # Greedy: take this subarray and reset
                current_sum = 0
                prefix_sums = {0}
            else:
                prefix_sums.add(current_sum)

        return count


class SolutionDict:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """
        Using dict to track last occurrence.
        """
        n = len(nums)
        last_end = -1  # End of last taken subarray
        count = 0

        prefix = {0: -1}
        current = 0

        for i in range(n):
            current += nums[i]

            need = current - target
            if need in prefix and prefix[need] >= last_end:
                count += 1
                last_end = i

            prefix[current] = i

        return count
