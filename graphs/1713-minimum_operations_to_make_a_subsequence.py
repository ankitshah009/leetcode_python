#1713. Minimum Operations to Make a Subsequence
#Hard
#
#You are given an array target that consists of distinct integers and another
#integer array arr that can have duplicates.
#
#In one operation, you can insert any integer at any position in arr. For
#example, if arr = [1,4,1,2], you can add 3 in the middle and it becomes
#[1,4,3,1,2]. Note that you can insert the integer at the very beginning or end.
#
#Return the minimum number of operations needed to make target a subsequence of
#arr.
#
#Example 1:
#Input: target = [5,1,3], arr = [9,4,2,3,4]
#Output: 2
#
#Example 2:
#Input: target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
#Output: 3
#
#Constraints:
#    1 <= target.length, arr.length <= 10^5
#    1 <= target[i], arr[i] <= 10^9
#    target contains no duplicates.

from typing import List
import bisect

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        """
        Convert to LIS problem.
        Map target values to indices, then find LIS in arr (using target indices).
        Answer = len(target) - LIS length.
        """
        # Map target values to their indices
        pos = {val: i for i, val in enumerate(target)}

        # Convert arr to sequence of target indices (skip values not in target)
        indices = [pos[x] for x in arr if x in pos]

        # Find LIS of indices using binary search (O(n log n))
        lis = []
        for idx in indices:
            i = bisect.bisect_left(lis, idx)
            if i == len(lis):
                lis.append(idx)
            else:
                lis[i] = idx

        return len(target) - len(lis)


class SolutionDetailed:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        """
        More detailed implementation of the same approach.
        """
        # Create value to index mapping for target
        target_index = {}
        for i, val in enumerate(target):
            target_index[val] = i

        # Filter arr to only include values from target, convert to indices
        mapped = []
        for val in arr:
            if val in target_index:
                mapped.append(target_index[val])

        # Find LIS length using binary search
        def lis_length(nums: List[int]) -> int:
            tails = []  # tails[i] = smallest ending value for LIS of length i+1

            for num in nums:
                pos = bisect.bisect_left(tails, num)
                if pos == len(tails):
                    tails.append(num)
                else:
                    tails[pos] = num

            return len(tails)

        # Minimum insertions = elements not in longest common subsequence
        lcs_length = lis_length(mapped)
        return len(target) - lcs_length


class SolutionNaiveLCS:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        """
        Direct LCS - O(n*m) - too slow for large inputs but shows the idea.
        """
        m, n = len(target), len(arr)

        # dp[i][j] = LCS length of target[:i] and arr[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if target[i - 1] == arr[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return m - dp[m][n]
