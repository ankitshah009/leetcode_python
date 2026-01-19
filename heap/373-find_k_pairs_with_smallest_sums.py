#373. Find K Pairs with Smallest Sums
#Medium
#
#You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
#
#Define a pair (u, v) which consists of one element from the first array and one element from the second array.
#
#Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
#
#Example 1:
#Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
#Output: [[1,2],[1,4],[1,6]]
#Explanation: The first 3 pairs are: [1,2], [1,4], [1,6]. Note that 7+2=9 is larger than 1+6=7.
#
#Example 2:
#Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
#Output: [[1,1],[1,1]]
#Explanation: The first 2 pairs are: [1,1], [1,1] (from both arrays).
#
#Example 3:
#Input: nums1 = [1,2], nums2 = [3], k = 3
#Output: [[1,3],[2,3]]
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 10^5
#    -10^9 <= nums1[i], nums2[i] <= 10^9
#    nums1 and nums2 both are sorted in non-decreasing order.
#    1 <= k <= 10^4
#    k <= nums1.length * nums2.length

import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        result = []
        # (sum, i, j) where i is index in nums1, j is index in nums2
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = {(0, 0)}

        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            # Add next candidates
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return result
