#164. Maximum Gap
#Medium
#
#Given an integer array nums, return the maximum difference between two successive
#elements in its sorted form. If the array contains less than two elements, return 0.
#
#You must write an algorithm that runs in linear time and uses linear extra space.
#
#Example 1:
#Input: nums = [3,6,9,1]
#Output: 3
#Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9)
#has the maximum difference 3.
#
#Example 2:
#Input: nums = [10]
#Output: 0
#Explanation: The array contains less than 2 elements, therefore return 0.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^9

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        n = len(nums)
        min_val, max_val = min(nums), max(nums)

        if min_val == max_val:
            return 0

        # Bucket sort approach
        # Each bucket has size = (max - min) / (n - 1)
        # Maximum gap must be >= bucket_size
        # So max gap won't be within a bucket, but between buckets

        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        # Each bucket stores (min_in_bucket, max_in_bucket)
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        # Find maximum gap between consecutive non-empty buckets
        max_gap = 0
        prev_max = min_val

        for bucket_min, bucket_max in buckets:
            if bucket_min == float('inf'):
                continue  # Empty bucket
            max_gap = max(max_gap, bucket_min - prev_max)
            prev_max = bucket_max

        return max_gap

    # Radix sort approach
    def maximumGapRadix(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        # Radix sort
        max_val = max(nums)
        exp = 1

        while max_val // exp > 0:
            # Counting sort for current digit
            count = [0] * 10
            output = [0] * len(nums)

            for num in nums:
                digit = (num // exp) % 10
                count[digit] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(len(nums) - 1, -1, -1):
                digit = (nums[i] // exp) % 10
                output[count[digit] - 1] = nums[i]
                count[digit] -= 1

            nums = output
            exp *= 10

        # Find max gap in sorted array
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])

        return max_gap
