#1802. Maximum Value at a Given Index in a Bounded Array
#Medium
#
#You are given three positive integers: n, index, and maxSum.
#
#You want to construct an array nums (0-indexed) that satisfies the following:
#- nums.length == n
#- nums[i] is a positive integer where 0 <= i < n.
#- abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
#- The sum of all elements of nums does not exceed maxSum.
#- nums[index] is maximized.
#
#Return nums[index] of the constructed array.
#
#Example 1:
#Input: n = 4, index = 2, maxSum = 6
#Output: 2
#
#Example 2:
#Input: n = 6, index = 1, maxSum = 10
#Output: 3
#
#Constraints:
#    1 <= n <= maxSum <= 10^9
#    0 <= index < n

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Binary search on the answer.
        For a peak value v at index, calculate minimum sum needed.
        """
        def calc_sum(length: int, peak: int) -> int:
            """Calculate minimum sum for a side with given length and peak."""
            if length == 0:
                return 0
            if peak >= length:
                # Full arithmetic sequence: peak + (peak-1) + ... + (peak-length+1)
                return length * peak - length * (length - 1) // 2
            else:
                # Partial: 1 + 2 + ... + peak + (length - peak) * 1
                return peak * (peak + 1) // 2 + (length - peak)

        def get_min_sum(peak: int) -> int:
            """Calculate minimum array sum with peak at index."""
            left_len = index
            right_len = n - index - 1

            # Sum on left side (peak going down to left)
            left_sum = calc_sum(left_len, peak - 1)
            # Sum on right side (peak going down to right)
            right_sum = calc_sum(right_len, peak - 1)

            return left_sum + peak + right_sum

        left, right = 1, maxSum

        while left < right:
            mid = (left + right + 1) // 2
            if get_min_sum(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1

        return left


class SolutionMath:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        Alternative calculation using arithmetic sum formula.
        """
        def min_sum_with_peak(v: int) -> int:
            left = index
            right = n - index - 1

            total = v  # The peak itself

            # Left side
            if v - 1 >= left:
                total += (v - 1 + v - left) * left // 2
            else:
                total += v * (v - 1) // 2 + (left - v + 1)

            # Right side
            if v - 1 >= right:
                total += (v - 1 + v - right) * right // 2
            else:
                total += v * (v - 1) // 2 + (right - v + 1)

            return total

        lo, hi = 1, maxSum
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if min_sum_with_peak(mid) <= maxSum:
                lo = mid
            else:
                hi = mid - 1

        return lo
