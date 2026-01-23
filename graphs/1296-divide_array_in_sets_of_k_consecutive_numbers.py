#1296. Divide Array in Sets of K Consecutive Numbers
#Medium
#
#Given an array of integers nums and a positive integer k, check whether it is
#possible to divide this array into sets of k consecutive numbers.
#
#Return true if it is possible. Otherwise, return false.
#
#Example 1:
#Input: nums = [1,2,3,3,4,4,5,6], k = 4
#Output: true
#Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
#
#Example 2:
#Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
#Output: true
#Explanation: Array can be divided into [1,2,3], [2,3,4], [3,4,5] and [9,10,11].
#
#Example 3:
#Input: nums = [1,2,3,4], k = 3
#Output: false
#Explanation: Each set must be exactly k = 3 consecutive numbers but we only have 4 elements.
#
#Constraints:
#    1 <= k <= nums.length <= 10^5
#    1 <= nums[i] <= 10^9

from typing import List
from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """
        Greedy: Start from smallest, form consecutive groups.
        Same as Hand of Straights (LC 846).
        """
        if len(nums) % k != 0:
            return False

        count = Counter(nums)

        for num in sorted(count):
            if count[num] > 0:
                # Need to start count[num] groups from this number
                need = count[num]
                for i in range(k):
                    if count[num + i] < need:
                        return False
                    count[num + i] -= need

        return True


class SolutionHeap:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """Using min heap for tracking minimums"""
        import heapq

        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for i in range(k):
                if count[first + i] == 0:
                    return False
                count[first + i] -= 1

                if count[first + i] == 0:
                    if first + i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True


class SolutionDeque:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """O(n) solution using deque to track open groups"""
        from collections import deque

        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        sorted_nums = sorted(count.keys())

        # opened[i] = number of groups that need nums starting at sorted_nums[i]
        opened = deque()
        prev_num = None
        open_count = 0

        for num in sorted_nums:
            # Close groups that should have ended
            if opened and prev_num is not None and num > prev_num + 1:
                return False

            # Extend existing groups
            if open_count > count[num]:
                return False

            # Start new groups
            new_groups = count[num] - open_count
            opened.append(new_groups)
            open_count = count[num]

            # Close completed groups
            if len(opened) == k:
                open_count -= opened.popleft()

            prev_num = num

        return open_count == 0
