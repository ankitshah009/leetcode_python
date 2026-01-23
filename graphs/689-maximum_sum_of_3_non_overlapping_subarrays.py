#689. Maximum Sum of 3 Non-Overlapping Subarrays
#Hard
#
#Given an integer array nums and an integer k, find three non-overlapping
#subarrays of length k with maximum sum and return them.
#
#Return the result as a list of indices representing the starting position of
#each interval (0-indexed). If there are multiple answers, return the
#lexicographically smallest one.
#
#Example 1:
#Input: nums = [1,2,1,2,6,7,5,1], k = 2
#Output: [0,3,5]
#Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting
#indices [0, 3, 5]. We could have also taken [2, 1], but answer [1, 3, 5]
#would be lexicographically smaller.
#
#Example 2:
#Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
#Output: [0,2,4]
#
#Constraints:
#    1 <= nums.length <= 2 * 10^4
#    1 <= nums[i] < 2^16
#    1 <= k <= floor(nums.length / 3)

class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        """
        DP approach:
        1. Compute prefix sums of all k-length subarrays
        2. Compute best left index up to each position
        3. Compute best right index from each position
        4. Find best middle that maximizes total sum
        """
        n = len(nums)

        # Compute sum of each k-length subarray
        window_sums = []
        curr_sum = sum(nums[:k])
        window_sums.append(curr_sum)

        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]
            window_sums.append(curr_sum)

        # left[i] = index of max window sum in [0, i]
        left = [0] * len(window_sums)
        best_idx = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[best_idx]:
                best_idx = i
            left[i] = best_idx

        # right[i] = index of max window sum in [i, end]
        right = [0] * len(window_sums)
        best_idx = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[best_idx]:
                best_idx = i
            right[i] = best_idx

        # Find best middle
        result = [-1, -1, -1]
        max_sum = 0

        for mid in range(k, len(window_sums) - k):
            l = left[mid - k]
            r = right[mid + k]
            total = window_sums[l] + window_sums[mid] + window_sums[r]

            if total > max_sum:
                max_sum = total
                result = [l, mid, r]

        return result


class SolutionDP:
    """General DP for any number of subarrays"""

    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)

        # Compute window sums
        window_sums = [0] * (n - k + 1)
        curr = sum(nums[:k])
        window_sums[0] = curr
        for i in range(1, n - k + 1):
            curr += nums[i + k - 1] - nums[i - 1]
            window_sums[i] = curr

        # dp[i][j] = (max_sum, indices) using i subarrays up to position j
        m = len(window_sums)

        # dp[num_arrays][end_pos] = (sum, list of start indices)
        dp = [[(0, []) for _ in range(m)] for _ in range(4)]

        for j in range(m):
            dp[1][j] = (window_sums[j], [j])
            if j > 0 and dp[1][j - 1][0] > dp[1][j][0]:
                dp[1][j] = dp[1][j - 1]

        for i in range(2, 4):
            for j in range((i - 1) * k, m):
                # Don't take window at j
                dp[i][j] = dp[i][j - 1] if j > 0 else (0, [])

                # Take window at j
                if j >= k:
                    prev_sum, prev_indices = dp[i - 1][j - k]
                    new_sum = prev_sum + window_sums[j]
                    if new_sum > dp[i][j][0]:
                        dp[i][j] = (new_sum, prev_indices + [j])

        return dp[3][m - 1][1]
