#321. Create Maximum Number
#Hard
#
#You are given two integer arrays nums1 and nums2 of lengths m and n
#respectively. nums1 and nums2 represent the digits of two numbers. You are
#also given an integer k.
#
#Create the maximum number of length k <= m + n from digits of the two numbers.
#The relative order of the digits from the same array must be preserved.
#
#Return an array of the k digits representing the answer.
#
#Example 1:
#Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
#Output: [9,8,6,5,3]
#
#Example 2:
#Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
#Output: [6,7,6,0,4]
#
#Example 3:
#Input: nums1 = [3,9], nums2 = [8,9], k = 3
#Output: [9,8,9]
#
#Constraints:
#    m == nums1.length
#    n == nums2.length
#    1 <= m, n <= 500
#    0 <= nums1[i], nums2[i] <= 9
#    1 <= k <= m + n

from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        """
        Strategy:
        1. Pick i digits from nums1, k-i digits from nums2
        2. Get maximum subsequence of length i from nums1
        3. Get maximum subsequence of length k-i from nums2
        4. Merge the two subsequences to get maximum
        5. Try all valid i values and return the best
        """
        def max_subsequence(nums, length):
            """Get maximum subsequence of given length using monotonic stack"""
            if length == 0:
                return []
            if length >= len(nums):
                return nums[:]

            stack = []
            drop = len(nums) - length  # Number of elements we can drop

            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)

            return stack[:length]

        def merge(seq1, seq2):
            """Merge two sequences to get lexicographically largest result"""
            result = []
            i = j = 0

            while i < len(seq1) or j < len(seq2):
                # Compare remaining sequences lexicographically
                if seq1[i:] > seq2[j:]:
                    result.append(seq1[i])
                    i += 1
                else:
                    result.append(seq2[j])
                    j += 1

            return result

        m, n = len(nums1), len(nums2)
        best = []

        # Try all possible splits
        for i in range(max(0, k - n), min(k, m) + 1):
            seq1 = max_subsequence(nums1, i)
            seq2 = max_subsequence(nums2, k - i)
            merged = merge(seq1, seq2)

            if merged > best:
                best = merged

        return best


class SolutionDetailed:
    """More detailed implementation with helper functions"""

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums, k):
            """Pick k digits from nums to form maximum number"""
            stack = []
            to_drop = len(nums) - k

            for num in nums:
                while to_drop and stack and stack[-1] < num:
                    stack.pop()
                    to_drop -= 1
                stack.append(num)

            return stack[:k]

        def greater(nums1, i, nums2, j):
            """Check if nums1[i:] > nums2[j:] lexicographically"""
            while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                i += 1
                j += 1
            return j == len(nums2) or (i < len(nums1) and nums1[i] > nums2[j])

        def merge(nums1, nums2):
            """Merge two arrays to get maximum"""
            result = []
            i = j = 0

            while i < len(nums1) and j < len(nums2):
                if greater(nums1, i, nums2, j):
                    result.append(nums1[i])
                    i += 1
                else:
                    result.append(nums2[j])
                    j += 1

            result.extend(nums1[i:])
            result.extend(nums2[j:])
            return result

        m, n = len(nums1), len(nums2)
        result = [0] * k

        for i in range(k + 1):
            j = k - i
            if i > m or j > n:
                continue

            candidate = merge(pick_max(nums1, i), pick_max(nums2, j))
            if candidate > result:
                result = candidate

        return result
