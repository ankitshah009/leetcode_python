#982. Triples with Bitwise AND Equal To Zero
#Hard
#
#Given an integer array nums, return the number of AND triples.
#
#An AND triple is a triple of indices (i, j, k) such that:
#- 0 <= i < nums.length
#- 0 <= j < nums.length
#- 0 <= k < nums.length
#- nums[i] & nums[j] & nums[k] == 0
#
#Example 1:
#Input: nums = [2,1,3]
#Output: 12
#Explanation: We could choose the following i, j, k triples:
#(i=0, j=0, k=1), (i=0, j=1, k=0), (i=0, j=1, k=1), (i=0, j=1, k=2),
#(i=0, j=2, k=1), (i=1, j=0, k=0), (i=1, j=0, k=1), (i=1, j=0, k=2),
#(i=1, j=1, k=0), (i=1, j=2, k=0), (i=2, j=0, k=1), (i=2, j=1, k=0)
#
#Example 2:
#Input: nums = [0,0,0]
#Output: 27
#
#Constraints:
#    1 <= nums.length <= 1000
#    0 <= nums[i] < 2^16

from collections import Counter

class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        """
        Precompute all pairwise ANDs, then count triples.
        """
        # Count frequency of each pairwise AND
        pair_and = Counter()
        for a in nums:
            for b in nums:
                pair_and[a & b] += 1

        # Count triples where (a & b) & c == 0
        result = 0
        for ab, count in pair_and.items():
            for c in nums:
                if ab & c == 0:
                    result += count

        return result


class SolutionOptimized:
    """Optimized with subset enumeration"""

    def countTriplets(self, nums: list[int]) -> int:
        MAX_VAL = 1 << 16

        # Count frequency of each AND pair
        pair_count = [0] * MAX_VAL
        for a in nums:
            for b in nums:
                pair_count[a & b] += 1

        result = 0
        for c in nums:
            # Need ab & c == 0, i.e., ab must be subset of ~c
            complement = (~c) & (MAX_VAL - 1)

            # Enumerate all subsets of complement
            subset = complement
            while subset:
                result += pair_count[subset]
                subset = (subset - 1) & complement

            result += pair_count[0]

        return result


class SolutionBruteForce:
    """Brute force O(n^3)"""

    def countTriplets(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if nums[i] & nums[j] & nums[k] == 0:
                        count += 1

        return count
