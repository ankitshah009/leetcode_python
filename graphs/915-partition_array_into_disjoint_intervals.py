#915. Partition Array into Disjoint Intervals
#Medium
#
#Given an integer array nums, partition it into two (contiguous) subarrays left
#and right so that:
#- Every element in left is less than or equal to every element in right.
#- left and right are non-empty.
#- left has the smallest possible size.
#
#Return the length of left after such a partitioning.
#
#Example 1:
#Input: nums = [5,0,3,8,6]
#Output: 3
#Explanation: left = [5,0,3], right = [8,6]
#
#Example 2:
#Input: nums = [1,1,1,0,6,12]
#Output: 4
#Explanation: left = [1,1,1,0], right = [6,12]
#
#Constraints:
#    2 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^6
#    There is at least one valid answer.

class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        """
        Track max of left partition and overall max seen.
        When we find element smaller than left max, extend left partition.
        """
        n = len(nums)
        left_max = nums[0]
        overall_max = nums[0]
        partition_idx = 0

        for i in range(1, n):
            if nums[i] < left_max:
                # Must include this in left partition
                partition_idx = i
                left_max = overall_max
            else:
                overall_max = max(overall_max, nums[i])

        return partition_idx + 1


class SolutionTwoPass:
    """Precompute min suffix"""

    def partitionDisjoint(self, nums: list[int]) -> int:
        n = len(nums)

        # min_right[i] = min of nums[i:]
        min_right = [0] * n
        min_right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(nums[i], min_right[i + 1])

        # Find smallest left such that max(left) <= min(right)
        max_left = 0
        for i in range(n - 1):
            max_left = max(max_left, nums[i])
            if max_left <= min_right[i + 1]:
                return i + 1

        return n - 1


class SolutionBothArrays:
    """Precompute both max prefix and min suffix"""

    def partitionDisjoint(self, nums: list[int]) -> int:
        n = len(nums)

        max_left = [0] * n
        min_right = [0] * n

        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], nums[i])

        min_right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])

        for i in range(n - 1):
            if max_left[i] <= min_right[i + 1]:
                return i + 1

        return n - 1
