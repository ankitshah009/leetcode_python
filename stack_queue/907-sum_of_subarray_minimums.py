#907. Sum of Subarray Minimums
#Medium
#
#Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous)
#subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.
#
#Example 1:
#Input: arr = [3,1,2,4]
#Output: 17
#Explanation:
#Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
#Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
#Sum is 17.
#
#Example 2:
#Input: arr = [11,81,94,43,3]
#Output: 444
#
#Constraints:
#    1 <= arr.length <= 3 * 10^4
#    1 <= arr[i] <= 3 * 10^4

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # For each element, find how many subarrays it is the minimum of
        # left[i] = distance to previous smaller element
        # right[i] = distance to next smaller or equal element

        left = [0] * n
        right = [0] * n
        stack = []

        # Find previous less element
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        stack = []

        # Find next less or equal element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % MOD

        return result
