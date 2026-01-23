#4. Median of Two Sorted Arrays
#Hard
#
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return
#the median of the two sorted arrays.
#
#The overall run time complexity should be O(log (m+n)).
#
#Example 1:
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
#
#Example 2:
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#Constraints:
#    nums1.length == m
#    nums2.length == n
#    0 <= m <= 1000
#    0 <= n <= 1000
#    1 <= m + n <= 2000
#    -10^6 <= nums1[i], nums2[i] <= 10^6

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search on smaller array - O(log(min(m,n))).
        """
        # Ensure nums1 is smaller
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half_len - partition1

            # Edge cases
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]

            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found correct partition
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        return 0.0


class SolutionMerge:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Merge and find median - O(m+n) time.
        """
        merged = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return merged[n // 2]


class SolutionKthElement:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find kth element approach.
        """
        def find_kth(a, b, k):
            if len(a) > len(b):
                a, b = b, a
            if not a:
                return b[k]
            if k == 0:
                return min(a[0], b[0])

            i = min(len(a) - 1, k // 2)
            j = min(len(b) - 1, k // 2)

            if a[i] <= b[j]:
                return find_kth(a[i + 1:], b, k - i - 1)
            else:
                return find_kth(a, b[j + 1:], k - j - 1)

        total = len(nums1) + len(nums2)

        if total % 2 == 1:
            return find_kth(nums1, nums2, total // 2)
        else:
            return (find_kth(nums1, nums2, total // 2 - 1) +
                    find_kth(nums1, nums2, total // 2)) / 2
