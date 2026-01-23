#1652. Defuse the Bomb
#Easy
#
#You have a bomb to defuse, and your time is running out! Your informer will
#provide you with a circular array code of length of n and a key k.
#
#To decrypt the code, you must replace every number. All the numbers are
#replaced simultaneously.
#- If k > 0, replace the ith number with the sum of the next k numbers.
#- If k < 0, replace the ith number with the sum of the previous k numbers.
#- If k == 0, replace the ith number with 0.
#
#As code is circular, the next element of code[n-1] is code[0], and the
#previous element of code[0] is code[n-1].
#
#Example 1:
#Input: code = [5,7,1,4], k = 3
#Output: [12,10,16,13]
#Explanation: Each number is replaced by the sum of the next 3 numbers.
#
#Example 2:
#Input: code = [1,2,3,4], k = 0
#Output: [0,0,0,0]
#
#Example 3:
#Input: code = [2,4,9,3], k = -2
#Output: [12,5,6,13]
#
#Constraints:
#    n == code.length
#    1 <= n <= 100
#    1 <= code[i] <= 100
#    -(n - 1) <= k <= n - 1

from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Sliding window approach for O(n) time.
        """
        n = len(code)

        if k == 0:
            return [0] * n

        result = [0] * n

        # Determine window bounds
        if k > 0:
            start, end = 1, k + 1
        else:
            start, end = k, 0

        # Initial window sum
        window_sum = sum(code[i % n] for i in range(start, end))

        for i in range(n):
            result[i] = window_sum
            # Slide window
            window_sum -= code[(i + start) % n]
            window_sum += code[(i + end) % n]

        return result


class SolutionBruteForce:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Direct computation for each position.
        """
        n = len(code)

        if k == 0:
            return [0] * n

        result = []

        for i in range(n):
            if k > 0:
                # Sum next k elements
                total = sum(code[(i + j) % n] for j in range(1, k + 1))
            else:
                # Sum previous |k| elements
                total = sum(code[(i + j) % n] for j in range(k, 0))

            result.append(total)

        return result


class SolutionPrefixSum:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Using prefix sum on doubled array.
        """
        n = len(code)

        if k == 0:
            return [0] * n

        # Double the array for circular handling
        doubled = code + code
        prefix = [0] * (2 * n + 1)

        for i in range(2 * n):
            prefix[i + 1] = prefix[i] + doubled[i]

        result = []

        for i in range(n):
            if k > 0:
                # Sum of elements from i+1 to i+k (inclusive)
                total = prefix[i + k + 1] - prefix[i + 1]
            else:
                # Sum of elements from i+k to i-1 (inclusive)
                # Map to doubled array indices
                left = i + k + n
                right = i + n - 1
                total = prefix[right + 1] - prefix[left]

            result.append(total)

        return result


class SolutionCompact:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Compact one-liner approach.
        """
        n = len(code)
        if k == 0:
            return [0] * n

        code2 = code * 2
        if k > 0:
            return [sum(code2[i+1:i+1+k]) for i in range(n)]
        else:
            return [sum(code2[i+n+k:i+n]) for i in range(n)]
