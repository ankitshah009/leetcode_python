#1995. Count Special Quadruplets
#Easy
#
#Given a 0-indexed integer array nums, return the number of distinct quadruplets
#(a, b, c, d) such that:
#- nums[a] + nums[b] + nums[c] == nums[d], and
#- a < b < c < d
#
#Example 1:
#Input: nums = [1,2,3,6]
#Output: 1
#Explanation: The only quadruplet is (0, 1, 2, 3): 1 + 2 + 3 == 6.
#
#Example 2:
#Input: nums = [3,3,6,4,5]
#Output: 0
#
#Example 3:
#Input: nums = [1,1,1,3,5]
#Output: 4
#
#Constraints:
#    4 <= nums.length <= 50
#    1 <= nums[i] <= 100

from typing import List
from collections import defaultdict

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        O(n^3) brute force with index constraints.
        """
        n = len(nums)
        count = 0

        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                for c in range(b + 1, n - 1):
                    target = nums[a] + nums[b] + nums[c]
                    for d in range(c + 1, n):
                        if nums[d] == target:
                            count += 1

        return count


class SolutionHashMap:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        O(n^2) using hashmap.
        Transform: nums[a] + nums[b] + nums[c] = nums[d]
                => nums[a] + nums[b] = nums[d] - nums[c]
        """
        n = len(nums)
        count = 0
        diff_count = defaultdict(int)

        # Start from the end
        for c in range(n - 2, 1, -1):
            # Add all nums[d] - nums[c+1] to hashmap
            for d in range(c + 1, n):
                diff_count[nums[d] - nums[c + 1]] += 1

            # Check all pairs (a, b)
            for a in range(c):
                for b in range(a + 1, c):
                    count += diff_count[nums[a] + nums[b]]

        return count


class SolutionOptimized:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        Another O(n^2) approach.
        nums[a] + nums[b] = nums[d] - nums[c]
        """
        n = len(nums)
        count = 0
        sum_count = defaultdict(int)

        # Iterate b from right to left
        for b in range(n - 3, 0, -1):
            # Add all (nums[d] - nums[c]) where c = b + 1
            c = b + 1
            for d in range(c + 1, n):
                sum_count[nums[d] - nums[c]] += 1

            # Count valid (a, b) pairs
            for a in range(b):
                count += sum_count[nums[a] + nums[b]]

        return count


class SolutionMemo:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        With precomputed pair sums.
        """
        n = len(nums)
        count = 0

        # For each c, d pair, check how many a, b pairs sum to nums[d] - nums[c]
        pair_sums = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                pair_sums[nums[i] + nums[j]].append((i, j))

        for c in range(n - 1):
            for d in range(c + 1, n):
                target = nums[d] - nums[c]
                if target < 0:
                    continue

                # Count (a, b) pairs with sum = target where b < c
                for a, b in pair_sums.get(target, []):
                    if b < c:
                        count += 1

        return count
