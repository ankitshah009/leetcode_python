#1590. Make Sum Divisible by P
#Medium
#
#Given an array of positive integers nums, remove the smallest subarray
#(possibly empty) such that the sum of the remaining elements is divisible by p.
#It is not allowed to remove the whole array.
#
#Return the length of the smallest subarray that you need to remove, or -1 if
#it's impossible.
#
#A subarray is defined as a contiguous block of elements in the array.
#
#Example 1:
#Input: nums = [3,1,4,2], p = 6
#Output: 1
#Explanation: The sum of the elements is 10, which is not divisible by 6.
#We can remove [4], making the sum 6, which is divisible by 6.
#
#Example 2:
#Input: nums = [6,3,5,2], p = 9
#Output: 2
#Explanation: We cannot remove a single element to get a sum divisible by 9.
#The best way is to remove [5,2], leaving [6,3] with sum 9.
#
#Example 3:
#Input: nums = [1,2,3], p = 3
#Output: 0
#Explanation: The sum is 6 which is already divisible by 3. No need to remove.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i] <= 10^9
#    1 <= p <= 10^9

from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        Find smallest subarray with sum ≡ total_sum (mod p).

        If total_sum % p == 0, answer is 0.
        Otherwise, we need to find shortest subarray with sum % p == target.

        Use prefix sum and hash map:
        - prefix[j] - prefix[i] ≡ target (mod p)
        - prefix[j] ≡ prefix[i] + target (mod p)

        For each j, look for prefix[i] ≡ prefix[j] - target (mod p).
        """
        n = len(nums)
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        # Map: prefix_mod -> most recent index
        prefix_map = {0: -1}
        prefix = 0
        min_len = n  # Can't remove whole array

        for j in range(n):
            prefix = (prefix + nums[j]) % p

            # We want: prefix[i] such that (prefix[j] - prefix[i]) % p == target
            # => prefix[i] % p == (prefix[j] - target) % p
            need = (prefix - target) % p

            if need in prefix_map:
                min_len = min(min_len, j - prefix_map[need])

            prefix_map[prefix] = j

        return min_len if min_len < n else -1


class SolutionDetailed:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        Detailed solution with step-by-step explanation.

        Goal: Remove subarray so remaining sum % p == 0
        Let S = total sum, and we remove subarray with sum R
        We need: (S - R) % p == 0
        => R % p == S % p

        So we need to find shortest subarray with sum ≡ S (mod p).

        Using prefix sums:
        - Let prefix[i] = sum of first i elements
        - Subarray [i+1, j] has sum = prefix[j] - prefix[i]
        - We want: (prefix[j] - prefix[i]) % p == target
        - Rearranging: prefix[i] % p == (prefix[j] - target) % p
        """
        n = len(nums)
        total_sum = sum(nums) % p

        if total_sum == 0:
            return 0  # Already divisible

        # Hash map: remainder -> index
        last_seen = {0: -1}  # Empty prefix has sum 0, "at index -1"

        min_length = n
        current_prefix = 0

        for i in range(n):
            current_prefix = (current_prefix + nums[i]) % p

            # What prefix sum would make the subarray sum ≡ total_sum (mod p)?
            required = (current_prefix - total_sum + p) % p

            if required in last_seen:
                length = i - last_seen[required]
                min_length = min(min_length, length)

            last_seen[current_prefix] = i

        # Can't remove entire array
        return -1 if min_length >= n else min_length


class SolutionCompact:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        Compact implementation.
        """
        target = sum(nums) % p
        if target == 0:
            return 0

        seen = {0: -1}
        prefix = 0
        ans = len(nums)

        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            want = (prefix - target) % p
            if want in seen:
                ans = min(ans, i - seen[want])
            seen[prefix] = i

        return ans if ans < len(nums) else -1
