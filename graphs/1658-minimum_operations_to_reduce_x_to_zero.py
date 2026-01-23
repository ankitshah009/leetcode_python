#1658. Minimum Operations to Reduce X to Zero
#Medium
#
#You are given an integer array nums and an integer x. In one operation, you can
#either remove the leftmost or the rightmost element from the array nums and
#subtract its value from x. Note that this modifies the array for future operations.
#
#Return the minimum number of operations to reduce x to exactly 0 if it is
#possible, otherwise, return -1.
#
#Example 1:
#Input: nums = [1,1,4,2,3], x = 5
#Output: 2
#Explanation: Remove 3 and 2 from the right. [1,1,4,2,3] -> [1,1,4]
#
#Example 2:
#Input: nums = [5,6,7,8,9], x = 4
#Output: -1
#
#Example 3:
#Input: nums = [3,2,20,1,1,3], x = 10
#Output: 5
#Explanation: Remove 3+1+1+3 from right and 2 from left. Total 5 operations.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^4
#    1 <= x <= 10^9

from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Find longest subarray with sum = total - x.
        Answer = n - length of that subarray.
        """
        n = len(nums)
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1
        if target == 0:
            return n

        # Sliding window for subarray with sum = target
        max_len = -1
        left = 0
        curr_sum = 0

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1


class SolutionPrefixSum:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Using prefix sum and hash map.
        """
        n = len(nums)
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1
        if target == 0:
            return n

        # prefix_sum -> index
        prefix_map = {0: -1}
        curr_sum = 0
        max_len = -1

        for i, num in enumerate(nums):
            curr_sum += num

            if curr_sum - target in prefix_map:
                max_len = max(max_len, i - prefix_map[curr_sum - target])

            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i

        return n - max_len if max_len != -1 else -1


class SolutionTwoPointer:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Two pointer from both ends.
        """
        n = len(nums)
        total = sum(nums)

        if total < x:
            return -1
        if total == x:
            return n

        # Start with all elements from left
        left_sum = total
        right = n
        min_ops = float('inf')

        for left in range(n + 1):
            if left > 0:
                left_sum -= nums[left - 1]

            # Shrink right side
            while right > left and left_sum < x:
                right -= 1
                left_sum += nums[right]

            if left_sum == x:
                # Operations = left + (n - right)
                min_ops = min(min_ops, left + n - right)

        return min_ops if min_ops != float('inf') else -1


class SolutionDP:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        DP approach (less efficient but conceptually different).
        """
        n = len(nums)

        # Compute prefix and suffix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        # Map suffix sum to min elements needed
        suffix_map = {}
        for j in range(n + 1):
            if suffix[j] not in suffix_map:
                suffix_map[suffix[j]] = n - j

        min_ops = float('inf')

        for i in range(n + 1):
            if prefix[i] > x:
                break

            remaining = x - prefix[i]
            if remaining in suffix_map:
                # Check no overlap
                right_start = n - suffix_map[remaining]
                if right_start >= i:
                    min_ops = min(min_ops, i + suffix_map[remaining])

        return min_ops if min_ops != float('inf') else -1
