#1679. Max Number of K-Sum Pairs
#Medium
#
#You are given an integer array nums and an integer k.
#
#In one operation, you can pick two numbers from the array whose sum equals k
#and remove them from the array.
#
#Return the maximum number of operations you can perform on the array.
#
#Example 1:
#Input: nums = [1,2,3,4], k = 5
#Output: 2
#Explanation: Starting with nums = [1,2,3,4]:
#- Remove 1 and 4. nums = [2,3]
#- Remove 2 and 3. nums = []
#There are no more pairs that sum up to 5, hence 2 operations.
#
#Example 2:
#Input: nums = [3,1,3,4,3], k = 6
#Output: 1
#Explanation: Only one pair sums to 6: (3,3). Remove them once.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^9
#    1 <= k <= 10^9

from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Use counter to count pairs.
        """
        count = Counter(nums)
        operations = 0

        for num in count:
            complement = k - num

            if complement not in count:
                continue

            if num == complement:
                # Same number, count pairs
                operations += count[num] // 2
            elif num < complement:
                # Only count once per pair
                operations += min(count[num], count[complement])

        return operations


class SolutionTwoPointer:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Two pointer approach after sorting.
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                right -= 1

        return operations


class SolutionHashMap:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Single pass with hash map.
        """
        seen = {}
        operations = 0

        for num in nums:
            complement = k - num

            if seen.get(complement, 0) > 0:
                operations += 1
                seen[complement] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1

        return operations


class SolutionCounterSimple:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Counter with explicit tracking.
        """
        count = Counter(nums)
        ops = 0

        for num, freq in count.items():
            comp = k - num
            if comp in count:
                if num == comp:
                    ops += freq // 2
                    count[num] = 0
                else:
                    pairs = min(freq, count[comp])
                    ops += pairs
                    count[num] = 0
                    count[comp] = 0

        return ops


class SolutionCompact:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Compact hash map solution.
        """
        cnt = Counter()
        ans = 0
        for num in nums:
            if cnt[k - num] > 0:
                ans += 1
                cnt[k - num] -= 1
            else:
                cnt[num] += 1
        return ans
