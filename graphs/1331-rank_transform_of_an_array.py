#1331. Rank Transform of an Array
#Easy
#
#Given an array of integers arr, replace each element with its rank.
#
#The rank represents how large the element is. The rank has the following rules:
#    Rank is an integer starting from 1.
#    The larger the element, the larger the rank. If two elements are equal,
#    their rank must be the same.
#    Rank should be as small as possible.
#
#Example 1:
#Input: arr = [40,10,20,30]
#Output: [4,1,2,3]
#Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
#
#Example 2:
#Input: arr = [100,100,100]
#Output: [1,1,1]
#Explanation: Same elements share the same rank.
#
#Example 3:
#Input: arr = [37,12,28,9,100,56,80,5,12]
#Output: [5,3,4,2,8,6,7,1,3]
#
#Constraints:
#    0 <= arr.length <= 10^5
#    -10^9 <= arr[i] <= 10^9

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Sort unique values and assign ranks.
        """
        # Get sorted unique values
        sorted_unique = sorted(set(arr))

        # Create value to rank mapping
        rank = {val: i + 1 for i, val in enumerate(sorted_unique)}

        # Replace each element with its rank
        return [rank[x] for x in arr]


class SolutionSortWithIndex:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """Sort with original indices"""
        if not arr:
            return []

        # Sort (value, index) pairs
        sorted_pairs = sorted(enumerate(arr), key=lambda x: x[1])

        result = [0] * len(arr)
        rank = 1

        for i, (orig_idx, val) in enumerate(sorted_pairs):
            if i > 0 and val > sorted_pairs[i - 1][1]:
                rank = i + 1
            result[orig_idx] = rank

        return result
