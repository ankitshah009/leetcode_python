#1199. Minimum Time to Build Blocks
#Hard
#
#You are given a list of blocks, where blocks[i] = t means that the i-th block
#needs t units of time to be built. A block can only be built by exactly one
#worker.
#
#A worker can either split into two workers (which costs split units of time)
#or build a block then go home. Both decisions cost time.
#
#The goal is to build all blocks in minimum time.
#
#Initially, there is only one worker.
#
#Return the minimum time needed to build all blocks.
#
#Example 1:
#Input: blocks = [1], split = 1
#Output: 1
#Explanation: One worker builds the one block in 1 unit of time.
#
#Example 2:
#Input: blocks = [1,2], split = 5
#Output: 7
#Explanation: One worker splits into 2 workers in 5 units of time, then each
#worker builds one block in parallel, resulting in 5 + max(1, 2) = 7.
#
#Example 3:
#Input: blocks = [1,2,3], split = 1
#Output: 4
#Explanation: Split into 2 workers (cost 1), one splits again (cost 1),
#then build blocks. Total = 1 + max(1 + max(1, 2), 3) = 4.
#
#Constraints:
#    1 <= blocks.length <= 1000
#    1 <= blocks[i] <= 10^5
#    1 <= split <= 100

from typing import List
import heapq

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        """
        Think of this as building a Huffman tree.
        Each block is a leaf, split cost is internal node cost.

        Key insight: Sort blocks, then greedily merge two smallest
        subtrees, adding split cost at each merge.

        This is like Huffman coding but instead of frequency * depth,
        we want min of (split + max(subtree times)).
        """
        if len(blocks) == 1:
            return blocks[0]

        # Use min heap
        heapq.heapify(blocks)

        while len(blocks) > 1:
            # Pop two smallest blocks
            a = heapq.heappop(blocks)
            b = heapq.heappop(blocks)

            # Merge: split cost + max of two (which is b since b >= a)
            merged = split + b
            heapq.heappush(blocks, merged)

        return blocks[0]


class SolutionDP:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        """
        DP approach with memoization.
        dp(i, workers) = min time to build blocks[i:] with given workers.
        """
        from functools import lru_cache

        blocks.sort(reverse=True)  # Sort descending for easier pruning
        n = len(blocks)

        @lru_cache(maxsize=None)
        def dp(idx, workers):
            # Base cases
            if idx == n:
                return 0
            if workers == 0:
                return float('inf')

            remaining = n - idx
            if workers >= remaining:
                # Enough workers, just take max block time
                return blocks[idx]

            # Option 1: Build block[idx] with one worker
            build = max(blocks[idx], dp(idx + 1, workers - 1))

            # Option 2: Split one worker (costs split time)
            split_cost = split + dp(idx, workers * 2)

            return min(build, split_cost)

        return dp(0, 1)


class SolutionBinarySearch:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        """
        Binary search on answer.
        For a given time T, check if it's achievable.
        """
        def can_finish(time, workers, idx):
            # Can we finish blocks[idx:] with given workers in given time?
            if idx == len(blocks):
                return True
            if workers == 0 or time <= 0:
                return False

            remaining = len(blocks) - idx

            # If enough workers, check if max block fits
            if workers >= remaining:
                return blocks[idx] <= time

            # Can build current block
            if blocks[idx] <= time:
                if can_finish(time, workers - 1, idx + 1):
                    return True

            # Can split if time allows
            if time > split:
                if can_finish(time - split, workers * 2, idx):
                    return True

            return False

        blocks.sort(reverse=True)

        # Binary search
        left, right = max(blocks), max(blocks) + split * len(blocks)

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid, 1, 0):
                right = mid
            else:
                left = mid + 1

        return left
