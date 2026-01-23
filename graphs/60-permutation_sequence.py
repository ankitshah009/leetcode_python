#60. Permutation Sequence
#Hard
#
#The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
#
#By listing and labeling all of the permutations in order, we get the following
#sequence for n = 3:
#1. "123"
#2. "132"
#3. "213"
#4. "231"
#5. "312"
#6. "321"
#
#Given n and k, return the kth permutation sequence.
#
#Example 1:
#Input: n = 3, k = 3
#Output: "213"
#
#Example 2:
#Input: n = 4, k = 9
#Output: "2314"
#
#Example 3:
#Input: n = 3, k = 1
#Output: "123"
#
#Constraints:
#    1 <= n <= 9
#    1 <= k <= n!

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Mathematical approach using factorial number system.
        """
        # Precompute factorials
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        # Available numbers
        numbers = list(range(1, n + 1))
        k -= 1  # Convert to 0-indexed

        result = []

        for i in range(n, 0, -1):
            # Find which number goes in this position
            index = k // factorial[i - 1]
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= factorial[i - 1]

        return ''.join(result)


class SolutionIterative:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Iterative approach.
        """
        import math

        numbers = list(range(1, n + 1))
        k -= 1  # 0-indexed
        result = []

        for i in range(n):
            # Number of permutations with (n-i-1) remaining numbers
            fact = math.factorial(n - i - 1)
            index = k // fact
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact

        return ''.join(result)


class SolutionBacktrack:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Backtracking with counting (less efficient).
        """
        from math import factorial

        numbers = list(range(1, n + 1))
        result = []

        k -= 1  # 0-indexed

        for _ in range(n):
            # Each number leads (n-len(result)-1)! permutations
            fact = factorial(len(numbers) - 1)
            index = k // fact
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact

        return ''.join(result)
