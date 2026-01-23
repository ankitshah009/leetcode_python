#805. Split Array With Same Average
#Hard
#
#You are given an integer array nums.
#
#You should move each element of nums into one of the two arrays A and B such
#that A and B are non-empty, and average(A) == average(B).
#
#Return true if it is possible to achieve that move and false otherwise.
#
#Example 1:
#Input: nums = [1,2,3,4,5,6,7,8]
#Output: true
#Explanation: We can split [1,2,3,4,5,6,7,8] into A = [1,4,5,8] and B = [2,3,6,7]
#with average(A) = average(B) = 4.5.
#
#Example 2:
#Input: nums = [3,1]
#Output: false
#
#Constraints:
#    1 <= nums.length <= 30
#    0 <= nums[i] <= 10^4

class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        """
        avg(A) = avg(B) = avg(nums)
        sum(A)/len(A) = sum(nums)/len(nums)
        sum(A) * n = sum(nums) * len(A)

        Find subset with sum = total * k / n for some k in [1, n-1]
        """
        n = len(nums)
        total = sum(nums)

        # Normalize: subtract average from each element
        # Now we need to find subset with sum = 0
        # But use total * k / n check instead

        # Check if any valid k exists
        possible = False
        for k in range(1, n):
            if (total * k) % n == 0:
                possible = True
                break

        if not possible:
            return False

        # Meet in the middle
        half = n // 2

        # Left half: all possible (sum, count) pairs
        left_sums = [set() for _ in range(half + 1)]
        left_sums[0].add(0)

        for num in nums[:half]:
            for k in range(half, 0, -1):
                for s in left_sums[k - 1]:
                    left_sums[k].add(s + num)

        # Right half
        right_half = nums[half:]
        right_len = len(right_half)
        right_sums = [set() for _ in range(right_len + 1)]
        right_sums[0].add(0)

        for num in right_half:
            for k in range(right_len, 0, -1):
                for s in right_sums[k - 1]:
                    right_sums[k].add(s + num)

        # Check all combinations
        for left_count in range(half + 1):
            for left_sum in left_sums[left_count]:
                for right_count in range(right_len + 1):
                    total_count = left_count + right_count
                    if 0 < total_count < n:
                        target_sum = total * total_count
                        if target_sum % n == 0:
                            needed = target_sum // n - left_sum
                            if needed in right_sums[right_count]:
                                return True

        return False


class SolutionDP:
    """Standard DP approach"""

    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        # dp[k] = set of possible sums using exactly k elements
        dp = [set() for _ in range(n + 1)]
        dp[0].add(0)

        for num in nums:
            for k in range(n - 1, 0, -1):
                for s in dp[k - 1]:
                    dp[k].add(s + num)

        for k in range(1, n):
            if (total * k) % n == 0:
                target = total * k // n
                if target in dp[k]:
                    return True

        return False
