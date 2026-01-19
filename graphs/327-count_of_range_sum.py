#327. Count of Range Sum
#Hard
#
#Given an integer array nums and two integers lower and upper, return the
#number of range sums that lie in [lower, upper] inclusive.
#
#Range sum S(i, j) is defined as the sum of the elements in nums between
#indices i and j inclusive, where i <= j.
#
#Example 1:
#Input: nums = [-2,5,-1], lower = -2, upper = 2
#Output: 3
#Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their
#respective sums are: -2, -1, 2.
#
#Example 2:
#Input: nums = [0], lower = 0, upper = 0
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -2^31 <= nums[i] <= 2^31 - 1
#    -10^5 <= lower <= upper <= 10^5
#    The answer is guaranteed to fit in a 32-bit integer.

from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Merge sort approach.
        For range sum S(i,j) = prefix[j+1] - prefix[i]
        We need: lower <= prefix[j+1] - prefix[i] <= upper
        Which means: prefix[j+1] - upper <= prefix[i] <= prefix[j+1] - lower
        """
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, left_count = merge_sort(arr[:mid])
            right, right_count = merge_sort(arr[mid:])

            count = left_count + right_count

            # Count valid pairs
            j = k = 0
            for r in right:
                # Find range [j, k) in left where lower <= r - left[i] <= upper
                while j < len(left) and r - left[j] > upper:
                    j += 1
                while k < len(left) and r - left[k] >= lower:
                    k += 1
                count += k - j

            # Merge
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, count

        _, result = merge_sort(prefix)
        return result


class SolutionBIT:
    """Binary Indexed Tree approach"""

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        sorted_prefix = SortedList()
        count = 0

        for p in prefix:
            # Count prefix sums in range [p - upper, p - lower]
            left = sorted_prefix.bisect_left(p - upper)
            right = sorted_prefix.bisect_right(p - lower)
            count += right - left

            sorted_prefix.add(p)

        return count


class SolutionBruteForce:
    """Brute force O(n^2) - for reference"""

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if lower <= total <= upper:
                    count += 1

        return count
