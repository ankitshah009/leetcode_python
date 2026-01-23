#1005. Maximize Sum Of Array After K Negations
#Easy
#
#Given an integer array nums and an integer k, modify the array in the following
#way: choose an index i and replace nums[i] with -nums[i]. You should apply this
#process exactly k times. You may choose the same index i multiple times.
#
#Return the largest possible sum of the array after modifying it in this way.
#
#Example 1:
#Input: nums = [4,2,3], k = 1
#Output: 5
#Explanation: Negate nums[1], array becomes [4,-2,3].
#
#Example 2:
#Input: nums = [3,-1,0,2], k = 3
#Output: 6
#
#Example 3:
#Input: nums = [2,-3,-1,5,-4], k = 2
#Output: 13
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -100 <= nums[i] <= 100
#    1 <= k <= 10^4

import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        """
        Greedy: negate smallest (most negative) each time.
        """
        heapq.heapify(nums)

        for _ in range(k):
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, -smallest)

        return sum(nums)


class SolutionSort:
    """Sort-based approach"""

    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()

        # Flip negatives first
        i = 0
        while k > 0 and i < len(nums) and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1

        # If k is odd, flip the smallest absolute value
        if k % 2 == 1:
            min_idx = min(range(len(nums)), key=lambda x: nums[x])
            nums[min_idx] = -nums[min_idx]

        return sum(nums)


class SolutionCount:
    """Count-based for bounded values"""

    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        count = [0] * 201  # Values from -100 to 100

        for num in nums:
            count[num + 100] += 1

        # Flip negatives
        for i in range(100):  # -100 to -1
            if count[i] > 0:
                flips = min(k, count[i])
                count[i] -= flips
                count[200 - i] += flips  # Move to positive
                k -= flips

        # If k odd, flip smallest
        if k % 2 == 1:
            for i in range(201):
                if count[i] > 0:
                    count[i] -= 1
                    count[200 - i] += 1
                    break

        return sum((i - 100) * count[i] for i in range(201))
