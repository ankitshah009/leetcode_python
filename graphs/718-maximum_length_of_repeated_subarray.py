#718. Maximum Length of Repeated Subarray
#Medium
#
#Given two integer arrays nums1 and nums2, return the maximum length of a
#subarray that appears in both arrays.
#
#Example 1:
#Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
#Output: 3
#Explanation: The repeated subarray with maximum length is [3,2,1].
#
#Example 2:
#Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
#Output: 5
#Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 1000
#    0 <= nums1[i], nums2[i] <= 100

class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        """
        DP: dp[i][j] = length of longest common suffix ending at i-1, j-1
        """
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])

        return max_len


class SolutionSpaceOptimized:
    """O(n) space using rolling array"""

    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        max_len = 0

        for i in range(1, m + 1):
            # Traverse right to left to avoid overwriting
            for j in range(n, 0, -1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                    max_len = max(max_len, dp[j])
                else:
                    dp[j] = 0

        return max_len


class SolutionBinarySearch:
    """Binary search on length + rolling hash"""

    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        def check(length):
            # Check if common subarray of given length exists
            MOD = 10**9 + 7
            BASE = 113

            # Compute hash power
            power = pow(BASE, length, MOD)

            # Hash all subarrays of length in nums1
            seen = set()
            h = 0
            for i in range(len(nums1)):
                h = (h * BASE + nums1[i]) % MOD
                if i >= length:
                    h = (h - nums1[i - length] * power) % MOD
                if i >= length - 1:
                    seen.add(h)

            # Check if any hash in nums2 matches
            h = 0
            for i in range(len(nums2)):
                h = (h * BASE + nums2[i]) % MOD
                if i >= length:
                    h = (h - nums2[i - length] * power) % MOD
                if i >= length - 1 and h in seen:
                    return True

            return False

        left, right = 0, min(len(nums1), len(nums2))

        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left
