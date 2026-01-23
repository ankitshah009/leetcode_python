#719. Find K-th Smallest Pair Distance
#Hard
#
#The distance of a pair of integers a and b is defined as the absolute
#difference between a and b.
#
#Given an integer array nums and an integer k, return the kth smallest distance
#among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
#
#Example 1:
#Input: nums = [1,3,1], k = 1
#Output: 0
#Explanation: Here are all the pairs:
#(1,3) -> 2
#(1,1) -> 0
#(3,1) -> 2
#Then the 1st smallest distance pair is (1,1), and its distance is 0.
#
#Example 2:
#Input: nums = [1,1,1], k = 2
#Output: 0
#
#Example 3:
#Input: nums = [1,6,1], k = 3
#Output: 5
#
#Constraints:
#    n == nums.length
#    2 <= n <= 10^4
#    0 <= nums[i] <= 10^6
#    1 <= k <= n * (n - 1) / 2

class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        """
        Binary search on distance + count pairs with distance <= mid.
        """
        nums.sort()
        n = len(nums)

        def count_pairs(max_dist):
            # Count pairs with distance <= max_dist
            count = 0
            left = 0

            for right in range(n):
                while nums[right] - nums[left] > max_dist:
                    left += 1
                count += right - left

            return count

        # Binary search on distance
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            if count_pairs(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left


class SolutionBinarySearchBisect:
    """Using bisect for pair counting"""

    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        import bisect

        nums.sort()
        n = len(nums)

        def count_pairs(max_dist):
            count = 0
            for i in range(n):
                # Find rightmost index with nums[j] - nums[i] <= max_dist
                j = bisect.bisect_right(nums, nums[i] + max_dist) - 1
                count += j - i  # Pairs (i, i+1), ..., (i, j)
            return count

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if count_pairs(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left


class SolutionBucketSort:
    """Bucket sort approach for small distance range"""

    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_dist = nums[-1] - nums[0]

        # Count occurrences of each distance
        count = [0] * (max_dist + 1)

        for i in range(n):
            for j in range(i + 1, n):
                count[nums[j] - nums[i]] += 1

        # Find kth smallest
        total = 0
        for dist in range(max_dist + 1):
            total += count[dist]
            if total >= k:
                return dist

        return max_dist
