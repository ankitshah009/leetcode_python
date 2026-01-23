#1703. Minimum Adjacent Swaps for K Consecutive Ones
#Hard
#
#You are given an integer array nums and an integer k. nums comprises only 0's
#and 1's. In one move, you can choose two adjacent indices and swap their values.
#
#Return the minimum number of moves required so that nums has k consecutive 1's.
#
#Example 1:
#Input: nums = [1,0,0,1,0,1], k = 2
#Output: 1
#
#Example 2:
#Input: nums = [1,0,0,0,0,0,1,1], k = 3
#Output: 5
#
#Example 3:
#Input: nums = [1,1,0,1], k = 2
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 10^5
#    nums[i] is 0 or 1.
#    1 <= k <= sum(nums)

from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        """
        Use positions of 1s and sliding window with prefix sum.
        Key insight: Move all k ones to center position, calculate cost.
        Transform positions to account for inherent spacing.
        """
        # Get positions of all 1s
        ones = [i for i, x in enumerate(nums) if x == 1]

        # Transform: pos[i] - i removes the inherent spacing
        # This converts to: minimum moves to make k elements consecutive at indices
        for i in range(len(ones)):
            ones[i] -= i

        # Now find minimum sum of distances to median in sliding window of size k
        # Use prefix sum for efficient computation
        n = len(ones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + ones[i]

        min_cost = float('inf')

        for i in range(n - k + 1):
            # Window from i to i+k-1
            mid = i + k // 2

            # Cost = sum of distances to median
            # Left part: median * count - sum
            # Right part: sum - median * count
            left_count = mid - i
            right_count = i + k - 1 - mid

            left_sum = prefix[mid] - prefix[i]
            right_sum = prefix[i + k] - prefix[mid + 1]

            cost = (ones[mid] * left_count - left_sum) + (right_sum - ones[mid] * right_count)

            min_cost = min(min_cost, cost)

        return min_cost


class SolutionAlternate:
    def minMoves(self, nums: List[int], k: int) -> int:
        """
        Alternative formulation using prefix sums.
        """
        # Positions of 1s
        pos = [i for i, x in enumerate(nums) if x == 1]

        # Adjust for minimum consecutive positions
        adj = [pos[i] - i for i in range(len(pos))]

        # Prefix sum of adjusted positions
        prefix = [0]
        for x in adj:
            prefix.append(prefix[-1] + x)

        result = float('inf')

        for i in range(len(pos) - k + 1):
            mid = i + k // 2
            median = adj[mid]

            # Sum of distances from median
            left_sum = median * (mid - i) - (prefix[mid] - prefix[i])
            right_sum = (prefix[i + k] - prefix[mid + 1]) - median * (i + k - 1 - mid)

            result = min(result, left_sum + right_sum)

        return result
