#1589. Maximum Sum Obtained of Any Permutation
#Medium
#
#We have an array of integers, nums, and an array of requests where
#requests[i] = [starti, endi]. The ith request asks for the sum of
#nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi].
#Both starti and endi are 0-indexed.
#
#Return the maximum total sum of all requests among all permutations of nums.
#
#Since the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
#Output: 19
#Explanation: One permutation of nums is [2,1,3,4,5] with the following result:
#requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
#requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
#Total sum: 8 + 3 = 11.
#A better permutation is [2,5,4,3,1]:
#requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 3 = 12
#requests[1] -> nums[0] + nums[1] = 2 + 5 = 7
#Total sum: 12 + 7 = 19.
#
#Example 2:
#Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
#Output: 11
#
#Example 3:
#Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
#Output: 47
#
#Constraints:
#    n == nums.length
#    1 <= n <= 10^5
#    0 <= nums[i] <= 10^5
#    1 <= requests.length <= 10^5
#    requests[i].length == 2
#    0 <= starti <= endi < n

from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        """
        Greedy approach:
        1. Count how many times each index is requested (using difference array)
        2. Sort counts and nums
        3. Pair largest nums with most frequent indices
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Use difference array to count frequency of each index
        freq = [0] * (n + 1)
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1

        # Convert to actual frequencies
        for i in range(1, n):
            freq[i] += freq[i - 1]

        # Remove the extra element
        freq = freq[:n]

        # Sort both arrays
        nums.sort()
        freq.sort()

        # Pair largest with largest
        total = 0
        for i in range(n):
            total = (total + nums[i] * freq[i]) % MOD

        return total


class SolutionDetailed:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        """
        Detailed explanation:

        To maximize total sum:
        - Put larger numbers at more frequently accessed indices
        - Count how many times each index appears in all requests
        - Use difference array for efficient range counting
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Difference array technique:
        # To add 1 to range [l, r], do diff[l] += 1 and diff[r+1] -= 1
        # Then prefix sum gives actual values
        diff = [0] * (n + 1)

        for l, r in requests:
            diff[l] += 1
            diff[r + 1] -= 1

        # Compute prefix sum to get frequency of each index
        count = [0] * n
        count[0] = diff[0]
        for i in range(1, n):
            count[i] = count[i - 1] + diff[i]

        # Greedy: sort and pair
        nums.sort()
        count.sort()

        result = 0
        for num, cnt in zip(nums, count):
            result = (result + num * cnt) % MOD

        return result


class SolutionHeap:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        """
        Alternative using heap (less efficient but conceptually different).
        """
        import heapq

        MOD = 10**9 + 7
        n = len(nums)

        # Count frequencies
        diff = [0] * (n + 1)
        for l, r in requests:
            diff[l] += 1
            diff[r + 1] -= 1

        freq = []
        curr = 0
        for i in range(n):
            curr += diff[i]
            freq.append(curr)

        # Use max heaps
        nums_heap = [-x for x in nums]
        freq_heap = [-x for x in freq]
        heapq.heapify(nums_heap)
        heapq.heapify(freq_heap)

        result = 0
        for _ in range(n):
            num = -heapq.heappop(nums_heap)
            f = -heapq.heappop(freq_heap)
            result = (result + num * f) % MOD

        return result
