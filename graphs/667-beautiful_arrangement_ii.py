#667. Beautiful Arrangement II
#Medium
#
#Given two integers n and k, construct a list answer that contains n different
#positive integers ranging from 1 to n and obeys the following requirement:
#
#Suppose this list is answer = [a1, a2, a3, ... , an], then the list
#[|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
#
#Return the list answer. If there exist multiple valid answers, return any of them.
#
#Example 1:
#Input: n = 3, k = 1
#Output: [1,2,3]
#Explanation: [1,2,3] has 1 distinct difference (1).
#
#Example 2:
#Input: n = 3, k = 2
#Output: [1,3,2]
#Explanation: [1,3,2] has 2 distinct differences (2, 1).
#
#Constraints:
#    1 <= k < n <= 10^4

from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """
        Pattern: Use 1, 2, 3, ..., n-k for differences of 1
        Then zigzag for the last k+1 elements to get k distinct differences.
        """
        result = list(range(1, n - k))

        # Zigzag pattern for last k+1 elements
        low, high = n - k, n
        for i in range(k + 1):
            if i % 2 == 0:
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        return result


class SolutionAlt:
    """Alternative: Start with zigzag, then ascending"""

    def constructArray(self, n: int, k: int) -> List[int]:
        result = []
        low, high = 1, k + 1

        # First k+1 elements with zigzag
        for i in range(k + 1):
            if i % 2 == 0:
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        # Remaining elements in ascending order
        for i in range(k + 2, n + 1):
            result.append(i)

        return result


class SolutionFlip:
    """Build by flipping segments"""

    def constructArray(self, n: int, k: int) -> List[int]:
        result = list(range(1, n + 1))

        # Flip segments to create different differences
        for i in range(1, k):
            result[i:] = result[i:][::-1]

        return result
