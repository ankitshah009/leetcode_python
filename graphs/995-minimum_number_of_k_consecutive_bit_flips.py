#995. Minimum Number of K Consecutive Bit Flips
#Hard
#
#You are given a binary array nums and an integer k.
#
#A k-bit flip is choosing a subarray of length k from nums and simultaneously
#changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
#
#Return the minimum number of k-bit flips required so that there is no 0 in the
#array. If it is not possible, return -1.
#
#Example 1:
#Input: nums = [0,1,0], k = 1
#Output: 2
#
#Example 2:
#Input: nums = [1,1,0], k = 2
#Output: -1
#
#Example 3:
#Input: nums = [0,0,0,1,0,1,1,0], k = 3
#Output: 3
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= k <= nums.length

from collections import deque

class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        """
        Greedy: flip at first 0, track flips with queue.
        """
        n = len(nums)
        flips = 0
        flip_queue = deque()  # Indices where flips started

        for i in range(n):
            # Remove flips that no longer affect current position
            while flip_queue and flip_queue[0] + k <= i:
                flip_queue.popleft()

            # Current value considering flips
            current = nums[i] ^ (len(flip_queue) % 2)

            if current == 0:
                if i + k > n:
                    return -1
                flip_queue.append(i)
                flips += 1

        return flips


class SolutionInPlace:
    """In-place marking"""

    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip_count = 0  # Number of active flips affecting current position

        for i in range(n):
            # Check if flip from k positions ago ended
            if i >= k and nums[i - k] > 1:
                flip_count -= 1
                nums[i - k] -= 2  # Restore

            # Current value
            current = (nums[i] + flip_count) % 2

            if current == 0:
                if i + k > n:
                    return -1
                nums[i] += 2  # Mark flip start
                flip_count += 1
                flips += 1

        return flips


class SolutionDiff:
    """Difference array approach"""

    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        diff = [0] * (n + 1)  # Difference array for flip tracking
        flips = 0
        curr_flips = 0

        for i in range(n):
            curr_flips += diff[i]

            if (nums[i] + curr_flips) % 2 == 0:
                if i + k > n:
                    return -1

                curr_flips += 1
                diff[i + k] -= 1
                flips += 1

        return flips
