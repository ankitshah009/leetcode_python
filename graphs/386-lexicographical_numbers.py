#386. Lexicographical Numbers
#Medium
#
#Given an integer n, return all the numbers in the range [1, n] sorted in
#lexicographical order.
#
#You must write an algorithm that runs in O(n) time and uses O(1) extra space.
#
#Example 1:
#Input: n = 13
#Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
#
#Example 2:
#Input: n = 2
#Output: [1,2]
#
#Constraints:
#    1 <= n <= 5 * 10^4

from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        O(n) time, O(1) space iterative approach.
        Simulate DFS traversal of trie.
        """
        result = []
        current = 1

        for _ in range(n):
            result.append(current)

            if current * 10 <= n:
                # Go deeper (append 0)
                current *= 10
            else:
                # Move to next sibling or backtrack
                while current % 10 == 9 or current >= n:
                    current //= 10
                current += 1

        return result


class SolutionDFS:
    """DFS approach - conceptually clearer"""

    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(current):
            if current > n:
                return

            result.append(current)

            # Try appending digits 0-9
            for digit in range(10):
                next_num = current * 10 + digit
                if next_num > n:
                    return
                dfs(next_num)

        # Start DFS from 1-9
        for i in range(1, 10):
            dfs(i)

        return result


class SolutionStack:
    """Explicit stack version of DFS"""

    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        stack = list(range(min(9, n), 0, -1))  # Start with 9 down to 1

        while stack:
            current = stack.pop()
            result.append(current)

            # Add children in reverse order (9 to 0)
            for digit in range(9, -1, -1):
                child = current * 10 + digit
                if child <= n:
                    stack.append(child)

        return result


class SolutionSort:
    """Simple sorting approach - O(n log n)"""

    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=str)
