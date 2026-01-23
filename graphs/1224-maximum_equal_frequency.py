#1224. Maximum Equal Frequency
#Hard
#
#Given an array nums of positive integers, return the longest possible length
#of an array prefix of nums, such that it is possible to remove exactly one
#element from this prefix so that every number that has appeared in it will
#have the same number of occurrences.
#
#If after removing one element there are no remaining elements, it's still
#considered that every appeared number has the same number of occurrences (0).
#
#Example 1:
#Input: nums = [2,2,1,1,5,3,3,5]
#Output: 7
#Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4] = 5,
#we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
#
#Example 2:
#Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
#Output: 13
#
#Constraints:
#    2 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^5

from typing import List
from collections import defaultdict

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        """
        Track count of each number and count of counts.
        Valid states after removing one element:
        1. All numbers appear once (remove any)
        2. Only one unique number (remove one occurrence)
        3. All counts same, and one number has count+1 (remove from that one)
        4. All counts same, and one number has count 1 (remove that number entirely)
        5. All numbers have same count c, and unique_count * c == n - 1
        """
        count = defaultdict(int)  # num -> count
        count_freq = defaultdict(int)  # count -> how many numbers have this count
        max_count = 0
        result = 0

        for i, num in enumerate(nums):
            n = i + 1  # Current prefix length

            # Update count
            if count[num] > 0:
                count_freq[count[num]] -= 1
                if count_freq[count[num]] == 0:
                    del count_freq[count[num]]

            count[num] += 1
            count_freq[count[num]] += 1
            max_count = max(max_count, count[num])

            unique = len(count)

            # Check valid conditions
            # Case 1: All elements same, can remove one
            if max_count == 1:
                result = n

            # Case 2: All occurrences of one number
            elif unique == 1:
                result = n

            # Case 3: max_count * unique == n + 1 and one number has max_count
            # (all have max_count except we need to remove one from a number with max_count)
            elif max_count * unique == n + 1 and count_freq[max_count] == 1:
                result = n

            # Case 4: (max_count - 1) * unique + 1 == n and all but one have max_count-1
            # (one number has max_count, rest have max_count-1)
            elif (max_count - 1) * unique + 1 == n and count_freq[max_count] == 1:
                result = n

            # Case 5: max_count * (unique - 1) + 1 == n
            # (one number appears once, rest appear max_count times)
            elif max_count * (unique - 1) + 1 == n and count_freq[1] == 1:
                result = n

        return result


class SolutionSimplified:
    def maxEqualFreq(self, nums: List[int]) -> int:
        """Simplified logic"""
        count = defaultdict(int)
        freq = defaultdict(int)
        max_freq = 0
        result = 0

        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            freq[count[num]] += 1
            max_freq = max(max_freq, count[num])

            n = i + 1
            unique = len(count)

            # Valid if removing one element makes all frequencies equal
            if max_freq == 1 or \
               unique == 1 or \
               (max_freq * freq[max_freq] == n - 1 and freq[max_freq - 1] == unique - 1) or \
               ((max_freq - 1) * freq[max_freq - 1] == n - 1 and freq[max_freq] == 1) or \
               (max_freq == n):
                result = n

        return result
