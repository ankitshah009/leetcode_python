#89. Gray Code
#Medium
#
#An n-bit gray code sequence is a sequence of 2^n integers where:
#- Every integer is in the inclusive range [0, 2^n - 1]
#- The first integer is 0
#- An integer appears no more than once in the sequence
#- The binary representation of every pair of adjacent integers differs by
#  exactly one bit
#- The binary representation of the first and last integers differs by exactly
#  one bit
#
#Given an integer n, return any valid n-bit gray code sequence.
#
#Example 1:
#Input: n = 2
#Output: [0,1,3,2]
#Explanation: 00 - 0, 01 - 1, 11 - 3, 10 - 2
#
#Example 2:
#Input: n = 1
#Output: [0,1]
#
#Constraints:
#    1 <= n <= 16

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        Formula: G(i) = i XOR (i >> 1)
        """
        return [i ^ (i >> 1) for i in range(1 << n)]


class SolutionReflection:
    def grayCode(self, n: int) -> List[int]:
        """
        Reflection/Mirror approach - build from smaller n.
        """
        result = [0]

        for i in range(n):
            # Add mirror of current result with (1 << i) prefix
            size = len(result)
            for j in range(size - 1, -1, -1):
                result.append(result[j] | (1 << i))

        return result


class SolutionBacktrack:
    def grayCode(self, n: int) -> List[int]:
        """
        Backtracking approach.
        """
        result = []
        visited = set()

        def backtrack(num: int) -> bool:
            if len(result) == (1 << n):
                return True

            result.append(num)
            visited.add(num)

            for i in range(n):
                next_num = num ^ (1 << i)
                if next_num not in visited:
                    if backtrack(next_num):
                        return True

            result.pop()
            visited.remove(num)
            return False

        backtrack(0)
        return result


class SolutionIterative:
    def grayCode(self, n: int) -> List[int]:
        """
        Iterative construction.
        """
        if n == 0:
            return [0]

        result = [0, 1]

        for i in range(1, n):
            bit = 1 << i
            # Append reverse of result with bit set
            for j in range(len(result) - 1, -1, -1):
                result.append(result[j] + bit)

        return result
