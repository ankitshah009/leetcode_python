#962. Maximum Width Ramp
#Medium
#
#A ramp in an integer array nums is a pair (i, j) for which i < j and
#nums[i] <= nums[j]. The width of such a ramp is j - i.
#
#Return the maximum width of a ramp in nums. If there is no ramp, return 0.
#
#Example 1:
#Input: nums = [6,0,8,2,1,5]
#Output: 4
#Explanation: The maximum width ramp is (i, j) = (1, 5): nums[1] = 0, nums[5] = 5.
#
#Example 2:
#Input: nums = [9,8,1,0,1,9,4,0,4,1]
#Output: 7
#Explanation: The maximum width ramp is (i, j) = (2, 9): nums[2] = 1, nums[9] = 1.
#
#Constraints:
#    2 <= nums.length <= 5 * 10^4
#    0 <= nums[i] <= 5 * 10^4

class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        """
        Monotonic decreasing stack for candidates.
        """
        n = len(nums)
        stack = []  # Monotonic decreasing stack of indices

        # Build stack of candidate starting points
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # Iterate from right, pop valid pairs
        max_width = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())

        return max_width


class SolutionSort:
    """Sort by value, track min index"""

    def maxWidthRamp(self, nums: list[int]) -> int:
        n = len(nums)
        # Sort indices by value
        indices = sorted(range(n), key=lambda i: nums[i])

        max_width = 0
        min_index = n

        for i in indices:
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)

        return max_width


class SolutionBinarySearch:
    """Binary search on sorted candidates"""

    def maxWidthRamp(self, nums: list[int]) -> int:
        import bisect

        n = len(nums)
        # candidates: (value, index) sorted by value descending
        candidates = []  # Stores (index) with decreasing values
        max_width = 0

        for i in range(n - 1, -1, -1):
            # Binary search for largest index with value >= nums[i]
            # We want nums[j] >= nums[i] where j > i
            pos = bisect.bisect_left(candidates, (nums[i], -1), key=lambda x: (nums[x], -x))
            if pos < len(candidates):
                max_width = max(max_width, candidates[pos] - i)

            # Add current index to candidates (maintaining decreasing value order)
            if not candidates or nums[i] > nums[candidates[-1]]:
                candidates.append(i)

        return max_width
