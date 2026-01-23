#1906. Minimum Absolute Difference Queries
#Medium
#
#The minimum absolute difference of an array a is defined as the minimum value
#of |a[i] - a[j]|, where 0 <= i < j < a.length and a[i] != a[j]. If all
#elements of a are the same, the minimum absolute difference is -1.
#
#You are given an integer array nums and the array queries where
#queries[i] = [l_i, r_i]. For each query i, compute the minimum absolute
#difference of the subarray nums[l_i...r_i] (inclusive).
#
#Return an array ans where ans[i] is the answer to the ith query.
#
#A subarray is a contiguous sequence of elements in an array.
#
#Example 1:
#Input: nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
#Output: [2,1,4,1]
#
#Example 2:
#Input: nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]
#Output: [-1,1,1,3]
#
#Constraints:
#    2 <= nums.length <= 10^5
#    1 <= nums[i] <= 100
#    1 <= queries.length <= 2 * 10^4
#    0 <= l_i < r_i < nums.length

from typing import List

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Prefix count for each value (1-100).
        For each query, find distinct values and compute min diff.
        """
        n = len(nums)
        MAX_VAL = 100

        # prefix[i][v] = count of value v in nums[0:i]
        prefix = [[0] * (MAX_VAL + 1) for _ in range(n + 1)]

        for i in range(n):
            for v in range(MAX_VAL + 1):
                prefix[i + 1][v] = prefix[i][v]
            prefix[i + 1][nums[i]] += 1

        result = []

        for l, r in queries:
            # Find values present in [l, r]
            present = []
            for v in range(1, MAX_VAL + 1):
                if prefix[r + 1][v] - prefix[l][v] > 0:
                    present.append(v)

            if len(present) <= 1:
                result.append(-1)
            else:
                min_diff = float('inf')
                for i in range(1, len(present)):
                    min_diff = min(min_diff, present[i] - present[i - 1])
                result.append(min_diff)

        return result


class SolutionOptimized:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Same approach with array instead of nested list.
        """
        n = len(nums)

        # For each value 1-100, store indices where it appears
        positions = [[] for _ in range(101)]
        for i, num in enumerate(nums):
            positions[num].append(i)

        import bisect

        def count_in_range(val, l, r):
            """Count occurrences of val in [l, r]."""
            pos = positions[val]
            left = bisect.bisect_left(pos, l)
            right = bisect.bisect_right(pos, r)
            return right - left

        result = []

        for l, r in queries:
            prev = -1
            min_diff = float('inf')

            for v in range(1, 101):
                if count_in_range(v, l, r) > 0:
                    if prev != -1:
                        min_diff = min(min_diff, v - prev)
                    prev = v

            result.append(min_diff if min_diff != float('inf') else -1)

        return result
