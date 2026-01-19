#220. Contains Duplicate III
#Hard
#
#You are given an integer array nums and two integers indexDiff and valueDiff.
#
#Find a pair of indices (i, j) such that:
#    i != j
#    abs(i - j) <= indexDiff
#    abs(nums[i] - nums[j]) <= valueDiff
#
#Return true if such pair exists or false otherwise.
#
#Example 1:
#Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
#Output: true
#Explanation: We can choose (i, j) = (0, 3).
#
#Example 2:
#Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
#Output: false
#
#Constraints:
#    2 <= nums.length <= 10^5
#    -10^9 <= nums[i] <= 10^9
#    1 <= indexDiff <= nums.length
#    0 <= valueDiff <= 10^9

from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Bucket approach: O(n) time
        if indexDiff <= 0 or valueDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size

            # Check current bucket
            if bucket_id in buckets:
                return True

            # Check adjacent buckets
            if bucket_id - 1 in buckets and num - buckets[bucket_id - 1] <= valueDiff:
                return True
            if bucket_id + 1 in buckets and buckets[bucket_id + 1] - num <= valueDiff:
                return True

            # Add to bucket
            buckets[bucket_id] = num

            # Remove old element outside window
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]

        return False

    # Balanced BST approach using SortedList: O(n log k)
    def containsNearbyAlmostDuplicateBST(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        sorted_list = SortedList()

        for i, num in enumerate(nums):
            # Find position where num would be inserted
            pos = sorted_list.bisect_left(num)

            # Check successor (element at pos)
            if pos < len(sorted_list) and sorted_list[pos] - num <= valueDiff:
                return True

            # Check predecessor (element at pos - 1)
            if pos > 0 and num - sorted_list[pos - 1] <= valueDiff:
                return True

            sorted_list.add(num)

            # Maintain window size
            if i >= indexDiff:
                sorted_list.remove(nums[i - indexDiff])

        return False
