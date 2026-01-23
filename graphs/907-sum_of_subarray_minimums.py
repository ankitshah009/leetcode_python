#907. Sum of Subarray Minimums
#Medium
#
#Given an array of integers arr, find the sum of min(b), where b ranges over
#every (contiguous) subarray of arr. Since the answer may be large, return the
#answer modulo 10^9 + 7.
#
#Example 1:
#Input: arr = [3,1,2,4]
#Output: 17
#Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2],
#[1,2,4], [3,1,2,4]. Minimums are 3,1,2,4,1,1,2,1,1,1. Sum = 17.
#
#Example 2:
#Input: arr = [11,81,94,43,3]
#Output: 444
#
#Constraints:
#    1 <= arr.length <= 3 * 10^4
#    1 <= arr[i] <= 3 * 10^4

class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """
        Monotonic stack to find contribution of each element.
        For each element, find how many subarrays it's the minimum of.
        """
        MOD = 10 ** 9 + 7
        n = len(arr)

        # left[i] = number of elements to the left where arr[i] is minimum
        # right[i] = number of elements to the right where arr[i] is minimum
        left = [0] * n
        right = [0] * n

        # Find previous less element
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        # Find next less or equal element
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % MOD

        return result


class SolutionSinglePass:
    """Single pass with monotonic stack"""

    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []  # (index, value)
        result = 0

        for i, num in enumerate(arr):
            while stack and stack[-1][1] > num:
                j, val = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                result = (result + val * left * right) % MOD
            stack.append((i, num))

        # Process remaining elements
        for k in range(len(stack)):
            j, val = stack[k]
            left = j - stack[k-1][0] if k > 0 else j + 1
            right = len(arr) - j
            result = (result + val * left * right) % MOD

        return result


class SolutionDP:
    """DP approach"""

    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)

        # dp[i] = sum of minimums of all subarrays ending at i
        dp = [0] * n
        stack = []  # monotonic increasing stack

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                j = stack[-1]
                dp[i] = dp[j] + arr[i] * (i - j)
            else:
                dp[i] = arr[i] * (i + 1)

            stack.append(i)

        return sum(dp) % MOD
