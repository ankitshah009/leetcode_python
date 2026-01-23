#1830. Minimum Number of Operations to Make String Sorted
#Hard
#
#You are given a string s (0-indexed). You are asked to perform the following
#operation on s until you get a sorted string:
#
#1. Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
#2. Find the largest index j such that i <= j < s.length and s[k] < s[i - 1]
#   for all the possible values of k in the range [i, j] inclusive.
#3. Swap the two characters at indices i - 1 and j.
#4. Reverse the suffix starting at index i.
#
#Return the number of operations needed to make the string sorted. Since the
#answer can be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: s = "cba"
#Output: 5
#
#Example 2:
#Input: s = "aabaa"
#Output: 2
#
#Constraints:
#    1 <= s.length <= 3000
#    s consists only of lowercase English letters.

class Solution:
    def makeStringSorted(self, s: str) -> int:
        """
        The operation is the inverse of next permutation.
        Count = number of permutations lexicographically smaller than s.

        For position i, count permutations where we choose a smaller char.
        """
        MOD = 10**9 + 7
        n = len(s)

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        # Count frequency of each character
        freq = [0] * 26

        result = 0

        # Process from right to left
        for i in range(n - 1, -1, -1):
            char_idx = ord(s[i]) - ord('a')
            freq[char_idx] += 1

            # Count characters smaller than s[i] to the right
            smaller = sum(freq[:char_idx])

            # Number of permutations with smaller char at position i
            remaining = n - i - 1
            perms = smaller * fact[remaining] % MOD

            # Divide by factorials of repeated characters
            for f in freq:
                if f > 1:
                    perms = perms * inv_fact[f] % MOD

            result = (result + perms) % MOD

        return result


class SolutionExplained:
    def makeStringSorted(self, s: str) -> int:
        """
        Detailed explanation:

        The operation described is exactly the previous permutation operation.
        Number of operations = rank of string among all permutations.

        For a string like "dcab":
        - Strings starting with 'a' come before: count perms of remaining
        - Strings starting with 'b' come before: count perms of remaining
        - Strings starting with 'c' come before: count perms of remaining
        - For strings starting with 'd':
          - Strings with 'd' then 'a' come before
          - etc.

        Use multinomial formula for permutations with repetition.
        """
        MOD = 10**9 + 7
        n = len(s)

        # Precompute
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def multinomial(freq, length):
            """Permutations of length elements with given frequencies."""
            result = fact[length]
            for f in freq:
                result = result * inv_fact[f] % MOD
            return result

        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        result = 0

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            remaining = n - i - 1

            # Count smaller characters available
            for j in range(idx):
                if freq[j] > 0:
                    freq[j] -= 1
                    result = (result + multinomial(freq, remaining)) % MOD
                    freq[j] += 1

            freq[idx] -= 1

        return result
