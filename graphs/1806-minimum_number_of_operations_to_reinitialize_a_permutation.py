#1806. Minimum Number of Operations to Reinitialize a Permutation
#Medium
#
#You are given an even integer n. You initially have a permutation perm of size
#n where perm[i] == i (0-indexed).
#
#In one operation, you will create a new array arr, and for each i:
#- If i % 2 == 0, then arr[i] = perm[i / 2].
#- If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].
#
#You will then assign arr to perm.
#
#Return the minimum non-zero number of operations you need to perform on perm
#to return the permutation to its initial value.
#
#Example 1:
#Input: n = 2
#Output: 1
#
#Example 2:
#Input: n = 4
#Output: 2
#
#Example 3:
#Input: n = 6
#Output: 4
#
#Constraints:
#    2 <= n <= 1000
#    n is even.

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        """
        Track position 1 (or any position except 0 and n-1).
        Position 0 and n-1 are fixed.
        """
        # Position i goes to:
        # - 2*i if i < n/2
        # - 2*i - n + 1 if i >= n/2

        pos = 1
        ops = 0

        while True:
            # Apply transformation
            if pos < n // 2:
                pos = 2 * pos
            else:
                pos = 2 * pos - n + 1
            ops += 1

            if pos == 1:
                break

        return ops


class SolutionMath:
    def reinitializePermutation(self, n: int) -> int:
        """
        Mathematical approach: find multiplicative order of 2 mod (n-1).
        Position 1 follows: pos -> 2*pos mod (n-1)
        """
        if n == 2:
            return 1

        ops = 1
        pos = 2

        while pos != 1:
            pos = (pos * 2) % (n - 1)
            ops += 1

        return ops


class SolutionSimulation:
    def reinitializePermutation(self, n: int) -> int:
        """
        Full simulation.
        """
        original = list(range(n))
        perm = original[:]
        ops = 0

        while True:
            arr = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            perm = arr
            ops += 1

            if perm == original:
                break

        return ops
