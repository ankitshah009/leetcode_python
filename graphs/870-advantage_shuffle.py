#870. Advantage Shuffle
#Medium
#
#You are given two integer arrays nums1 and nums2 both of the same length. The
#advantage of nums1 with respect to nums2 is the number of indices i for which
#nums1[i] > nums2[i].
#
#Return any permutation of nums1 that maximizes its advantage with respect to nums2.
#
#Example 1:
#Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
#Output: [2,11,7,15]
#
#Example 2:
#Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
#Output: [24,32,8,12]
#
#Constraints:
#    1 <= nums1.length <= 10^5
#    nums2.length == nums1.length
#    0 <= nums1[i], nums2[i] <= 10^9

from collections import deque

class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Greedy: for each nums2 element (largest to smallest),
        assign smallest nums1 element that beats it.
        """
        n = len(nums1)
        nums1_sorted = sorted(nums1)

        # Sort nums2 indices by value (descending)
        indices = sorted(range(n), key=lambda i: nums2[i], reverse=True)

        result = [0] * n
        left, right = 0, n - 1

        for i in indices:
            # Can largest remaining nums1 beat nums2[i]?
            if nums1_sorted[right] > nums2[i]:
                result[i] = nums1_sorted[right]
                right -= 1
            else:
                # Use smallest (will lose anyway)
                result[i] = nums1_sorted[left]
                left += 1

        return result


class SolutionDeque:
    """Using deque for both ends"""

    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_dq = deque(sorted(nums1))

        # (value, original_index) sorted by value descending
        nums2_indexed = sorted(enumerate(nums2), key=lambda x: x[1], reverse=True)

        result = [0] * len(nums1)

        for i, val in nums2_indexed:
            if nums1_dq[-1] > val:
                result[i] = nums1_dq.pop()
            else:
                result[i] = nums1_dq.popleft()

        return result


class SolutionAssignment:
    """Track assignments explicitly"""

    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        from collections import defaultdict

        sorted1 = sorted(nums1)
        sorted2_idx = sorted(range(len(nums2)), key=lambda i: nums2[i])

        result = [0] * len(nums1)
        remaining = []  # nums1 values that couldn't beat anyone
        j = 0

        for num1 in sorted1:
            # Find smallest nums2 that num1 can beat
            while j < len(sorted2_idx) and result[sorted2_idx[j]] != 0:
                j += 1

            if j < len(sorted2_idx) and num1 > nums2[sorted2_idx[j]]:
                result[sorted2_idx[j]] = num1
            else:
                remaining.append(num1)

        # Fill remaining positions
        for i in range(len(result)):
            if result[i] == 0:
                result[i] = remaining.pop()

        return result
