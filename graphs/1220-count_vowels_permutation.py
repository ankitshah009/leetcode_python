#1220. Count Vowels Permutation
#Hard
#
#Given an integer n, your task is to count how many strings of length n can be
#formed under the following rules:
#    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
#    Each vowel 'a' may only be followed by an 'e'.
#    Each vowel 'e' may only be followed by an 'a' or an 'i'.
#    Each vowel 'i' may not be followed by another 'i'.
#    Each vowel 'o' may only be followed by an 'i' or a 'u'.
#    Each vowel 'u' may only be followed by an 'a'.
#
#Since the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 1
#Output: 5
#Explanation: All possible strings are: "a", "e", "i", "o" and "u".
#
#Example 2:
#Input: n = 2
#Output: 10
#Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
#
#Example 3:
#Input: n = 5
#Output: 68
#
#Constraints:
#    1 <= n <= 2 * 10^4

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        DP: Track count of strings ending with each vowel.

        Transitions (what can follow):
        - a: can be followed by e
        - e: can be followed by a, i
        - i: can be followed by a, e, o, u
        - o: can be followed by i, u
        - u: can be followed by a

        Reverse (what can precede):
        - a: can be preceded by e, i, u
        - e: can be preceded by a, i
        - i: can be preceded by e, o
        - o: can be preceded by i
        - u: can be preceded by i, o
        """
        MOD = 10**9 + 7

        # Count of strings ending with a, e, i, o, u
        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(n - 1):
            # New counts based on what can precede each vowel
            new_a = (e + i + u) % MOD
            new_e = (a + i) % MOD
            new_i = (e + o) % MOD
            new_o = i % MOD
            new_u = (i + o) % MOD

            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u

        return (a + e + i + o + u) % MOD


class SolutionMatrix:
    def countVowelPermutation(self, n: int) -> int:
        """
        Matrix exponentiation for O(log n) solution.
        """
        MOD = 10**9 + 7

        def matrix_mult(A, B):
            """Multiply two 5x5 matrices"""
            result = [[0] * 5 for _ in range(5)]
            for i in range(5):
                for j in range(5):
                    for k in range(5):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        def matrix_pow(M, power):
            """Compute M^power"""
            # Identity matrix
            result = [[1 if i == j else 0 for j in range(5)] for i in range(5)]

            while power > 0:
                if power % 2 == 1:
                    result = matrix_mult(result, M)
                M = matrix_mult(M, M)
                power //= 2

            return result

        # Transition matrix (what can precede each vowel)
        # a  e  i  o  u
        # Columns: what current ends with
        # Rows: what previous ended with
        transition = [
            [0, 1, 0, 0, 0],  # a can follow e
            [1, 0, 1, 0, 0],  # e can follow a, i
            [1, 1, 0, 1, 1],  # i can follow a, e, o, u
            [0, 0, 1, 0, 1],  # o can follow i, u
            [1, 0, 0, 0, 0],  # u can follow a
        ]

        # Actually we need what can precede each vowel
        # a: preceded by e, i, u
        # e: preceded by a, i
        # i: preceded by e, o
        # o: preceded by i
        # u: preceded by i, o
        transition = [
            [0, 1, 1, 0, 1],  # new a from e, i, u
            [1, 0, 1, 0, 0],  # new e from a, i
            [0, 1, 0, 1, 0],  # new i from e, o
            [0, 0, 1, 0, 0],  # new o from i
            [0, 0, 1, 1, 0],  # new u from i, o
        ]

        M = matrix_pow(transition, n - 1)

        # Sum all entries (starting with 1 of each vowel)
        total = 0
        for i in range(5):
            for j in range(5):
                total = (total + M[i][j]) % MOD

        return total
