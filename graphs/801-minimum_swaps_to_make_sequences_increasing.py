#801. Minimum Swaps To Make Sequences Increasing
#Hard
#
#You are given two integer arrays of the same length nums1 and nums2. In one
#operation, you are allowed to swap nums1[i] with nums2[i].
#
#For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the
#element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
#
#Return the minimum number of needed operations to make nums1 and nums2 strictly
#increasing. The test cases are generated so that the given input always makes
#it possible.
#
#Example 1:
#Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
#Output: 1
#Explanation: Swap nums1[3] and nums2[3]. Then sequences are:
#nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4], both strictly increasing.
#
#Example 2:
#Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
#Output: 1
#
#Constraints:
#    2 <= nums1.length <= 10^5
#    nums2.length == nums1.length
#    0 <= nums1[i], nums2[i] <= 2 * 10^5

class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        """
        DP tracking two states:
        - keep[i]: min swaps if we don't swap at position i
        - swap[i]: min swaps if we swap at position i
        """
        n = len(nums1)

        # keep[i], swap[i] = min swaps ending at i
        keep = 0  # No swap at position 0
        swap = 1  # Swap at position 0

        for i in range(1, n):
            new_keep = float('inf')
            new_swap = float('inf')

            # Case 1: Both naturally increasing (no swap needed to maintain)
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                new_keep = min(new_keep, keep)  # No swap at i or i-1
                new_swap = min(new_swap, swap + 1)  # Swap at both i and i-1

            # Case 2: Swapping either i or i-1 needed
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                new_keep = min(new_keep, swap)  # Swap at i-1, not at i
                new_swap = min(new_swap, keep + 1)  # No swap at i-1, swap at i

            keep, swap = new_keep, new_swap

        return min(keep, swap)


class SolutionDP:
    """Explicit DP arrays"""

    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        keep = [float('inf')] * n
        swap = [float('inf')] * n

        keep[0] = 0
        swap[0] = 1

        for i in range(1, n):
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1

            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1] + 1)

        return min(keep[-1], swap[-1])
