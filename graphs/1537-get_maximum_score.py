#1537. Get the Maximum Score
#Hard
#
#You are given two sorted arrays of distinct integers nums1 and nums2.
#
#A valid path is defined as follows:
#- Choose array nums1 or nums2 to traverse (from index 0).
#- Traverse the current array from left to right.
#- If you are reading any value that is present in nums1 and nums2 you are
#  allowed to change your path to the other array. (Only one repeated value is
#  considered in the valid path).
#
#The score is defined as the sum of unique values in a valid path.
#
#Return the maximum score you can obtain of all possible valid paths. Since the
#answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
#Output: 30
#Explanation: Valid paths:
#[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],
#[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10],
#Path [2,4,6,8,10] obtains the maximum score: 2 + 4 + 6 + 8 + 10 = 30.
#
#Example 2:
#Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
#Output: 109
#Explanation: Maximum value is: 1 + 3 + 5 + 100 = 109.
#
#Example 3:
#Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
#Output: 40
#Explanation: There are no common elements, so we take all from nums2.
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 10^5
#    1 <= nums1[i], nums2[i] <= 10^7
#    nums1 and nums2 are strictly increasing.

from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Two pointers: At each common element, take the max path sum so far.

        Between common elements (or start/end), we must choose one path.
        So we take the max of sums between consecutive common elements.
        """
        MOD = 10**9 + 7

        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        sum1, sum2 = 0, 0

        result = 0

        while i < n1 or j < n2:
            if i < n1 and (j >= n2 or nums1[i] < nums2[j]):
                sum1 += nums1[i]
                i += 1
            elif j < n2 and (i >= n1 or nums2[j] < nums1[i]):
                sum2 += nums2[j]
                j += 1
            else:
                # Common element: nums1[i] == nums2[j]
                # Take max of paths so far, add the common element
                result += max(sum1, sum2) + nums1[i]
                sum1 = sum2 = 0
                i += 1
                j += 1

        # Add remaining sums
        result += max(sum1, sum2)

        return result % MOD


class SolutionSegmented:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Find common elements and compute segment sums.
        """
        MOD = 10**9 + 7

        set2 = set(nums2)
        common = [x for x in nums1 if x in set2]

        if not common:
            # No intersection, take max of total sums
            return max(sum(nums1), sum(nums2)) % MOD

        # Compute segment sums
        def segment_sums(arr, splits):
            sums = []
            current_sum = 0
            j = 0
            for x in arr:
                if j < len(splits) and x == splits[j]:
                    sums.append(current_sum)
                    current_sum = 0
                    j += 1
                current_sum += x
            sums.append(current_sum)
            return sums

        segs1 = segment_sums(nums1, common)
        segs2 = segment_sums(nums2, common)

        # Combine: at each common point, take max of both paths
        result = 0
        for s1, s2 in zip(segs1, segs2):
            result += max(s1, s2)

        # Add common elements
        result += sum(common)

        return result % MOD


class SolutionDP:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        DP approach: Track max score ending at each position.
        """
        MOD = 10**9 + 7

        n1, n2 = len(nums1), len(nums2)

        # Map values to indices in nums2
        idx2 = {v: i for i, v in enumerate(nums2)}

        # dp1[i] = max score ending at nums1[i]
        # dp2[i] = max score ending at nums2[i]
        dp1 = [0] * (n1 + 1)
        dp2 = [0] * (n2 + 1)

        i, j = 0, 0
        while i < n1 or j < n2:
            if i < n1 and (j >= n2 or nums1[i] < nums2[j]):
                dp1[i + 1] = dp1[i] + nums1[i]
                i += 1
            elif j < n2 and (i >= n1 or nums2[j] < nums1[i]):
                dp2[j + 1] = dp2[j] + nums2[j]
                j += 1
            else:
                # Common element
                best = max(dp1[i], dp2[j]) + nums1[i]
                dp1[i + 1] = best
                dp2[j + 1] = best
                i += 1
                j += 1

        return max(dp1[n1], dp2[n2]) % MOD


class SolutionSimple:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Cleaner two-pointer solution.
        """
        MOD = 10**9 + 7

        i = j = 0
        sum1 = sum2 = 0
        m, n = len(nums1), len(nums2)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # Merge paths at common element
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1

        # Process remaining elements
        while i < m:
            sum1 += nums1[i]
            i += 1

        while j < n:
            sum2 += nums2[j]
            j += 1

        return max(sum1, sum2) % MOD
