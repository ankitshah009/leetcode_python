#659. Split Array into Consecutive Subsequences
#Medium
#
#You are given an integer array nums that is sorted in non-decreasing order.
#
#Determine if it is possible to split nums into one or more subsequences such
#that both of the following conditions are true:
#
#- Each subsequence is a consecutive increasing sequence (i.e. each integer is
#  exactly one more than the previous integer).
#- All subsequences have a length of 3 or more.
#
#Return true if you can split nums according to the above conditions, or false otherwise.
#
#Example 1:
#Input: nums = [1,2,3,3,4,5]
#Output: true
#Explanation: nums can be split into [1,2,3] and [3,4,5].
#
#Example 2:
#Input: nums = [1,2,3,3,4,4,5,5]
#Output: true
#Explanation: nums can be split into [1,2,3,4,5] and [3,4,5].
#
#Example 3:
#Input: nums = [1,2,3,4,4,5]
#Output: false
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -1000 <= nums[i] <= 1000
#    nums is sorted in non-decreasing order.

from typing import List
from collections import Counter, defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        Greedy approach with two hash maps:
        - freq: remaining count of each number
        - tails: count of subsequences ending at each number
        """
        freq = Counter(nums)
        tails = defaultdict(int)  # tails[x] = number of subsequences ending at x

        for num in nums:
            if freq[num] == 0:
                continue

            freq[num] -= 1

            # Option 1: Extend existing subsequence
            if tails[num - 1] > 0:
                tails[num - 1] -= 1
                tails[num] += 1
            # Option 2: Start new subsequence of length 3
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                tails[num + 2] += 1
            else:
                return False

        return True


class SolutionHeap:
    """Min heap approach - track subsequence lengths"""

    def isPossible(self, nums: List[int]) -> bool:
        import heapq

        # Map from ending number to min heap of subsequence lengths
        subsequences = defaultdict(list)

        for num in nums:
            # Try to extend shortest subsequence ending at num-1
            if subsequences[num - 1]:
                length = heapq.heappop(subsequences[num - 1])
                heapq.heappush(subsequences[num], length + 1)
            else:
                # Start new subsequence
                heapq.heappush(subsequences[num], 1)

        # Check all subsequences have length >= 3
        for end in subsequences:
            for length in subsequences[end]:
                if length < 3:
                    return False

        return True


class SolutionDP:
    """DP approach tracking counts"""

    def isPossible(self, nums: List[int]) -> bool:
        # p1, p2, p3 = subsequences of length 1, 2, 3+ ending at prev
        prev = float('-inf')
        p1 = p2 = p3 = 0

        freq = Counter(nums)

        for num in sorted(freq.keys()):
            count = freq[num]

            if num != prev + 1:
                # Gap in sequence
                if p1 > 0 or p2 > 0:
                    return False
                p1 = count
                p2 = 0
                p3 = 0
            else:
                # Consecutive
                if count < p1 + p2:
                    return False

                # Extend existing subsequences first
                new_p3 = p2 + min(p3, count - p1 - p2)
                new_p2 = p1
                new_p1 = max(0, count - p1 - p2 - p3)

                p1, p2, p3 = new_p1, new_p2, new_p3

            prev = num

        return p1 == 0 and p2 == 0
