#1316. Distinct Echo Substrings
#Hard
#
#Return the number of distinct non-empty substrings of text that can be written
#as the concatenation of some string with itself (i.e., it can be written as
#a + a where a is some string).
#
#Example 1:
#Input: text = "abcabcabc"
#Output: 3
#Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
#
#Example 2:
#Input: text = "leetcodeleetcode"
#Output: 2
#Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
#
#Constraints:
#    1 <= text.length <= 2000
#    text has only lowercase English letters.

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """
        Check all substrings of even length.
        Use rolling hash for efficient comparison.
        """
        n = len(text)
        result = set()
        BASE = 26
        MOD = 10**9 + 7

        # For each starting position
        for i in range(n):
            hash1 = 0
            hash2 = 0
            power = 1

            # Try all half-lengths
            for j in range(i, n):
                half_len = j - i + 1

                # Update hash for first half
                hash1 = (hash1 * BASE + ord(text[j]) - ord('a')) % MOD

                # Check if we can form second half
                second_end = j + half_len
                if second_end > n:
                    break

                # Update hash for second half
                for k in range(j + 1, second_end + 1):
                    if k <= j + half_len:
                        hash2 = (hash2 * BASE + ord(text[k - 1 + half_len - (k - 1 - i)]) - ord('a')) % MOD

                # Actually compute second half hash properly
                # Reset and compute fresh
                hash2 = 0
                for k in range(j + 1, second_end + 1):
                    hash2 = (hash2 * BASE + ord(text[k]) - ord('a')) % MOD

                if hash1 == hash2:
                    # Verify with actual string comparison
                    first = text[i:j+1]
                    second = text[j+1:second_end+1]
                    if first == second:
                        result.add(first + second)

        return len(result)


class SolutionSimple:
    def distinctEchoSubstrings(self, text: str) -> int:
        """Straightforward O(n^3) approach"""
        n = len(text)
        seen = set()

        for length in range(2, n + 1, 2):  # Only even lengths
            half = length // 2
            for i in range(n - length + 1):
                first = text[i:i + half]
                second = text[i + half:i + length]
                if first == second:
                    seen.add(first + second)

        return len(seen)


class SolutionRollingHash:
    def distinctEchoSubstrings(self, text: str) -> int:
        """Optimized rolling hash approach"""
        n = len(text)
        BASE = 31
        MOD = 10**18 + 9

        # Precompute powers and prefix hashes
        powers = [1] * (n + 1)
        for i in range(1, n + 1):
            powers[i] = (powers[i - 1] * BASE) % MOD

        prefix_hash = [0] * (n + 1)
        for i in range(n):
            prefix_hash[i + 1] = (prefix_hash[i] * BASE + ord(text[i])) % MOD

        def get_hash(l, r):
            """Get hash of text[l:r]"""
            return (prefix_hash[r] - prefix_hash[l] * powers[r - l]) % MOD

        result = set()

        for half_len in range(1, n // 2 + 1):
            for i in range(n - 2 * half_len + 1):
                h1 = get_hash(i, i + half_len)
                h2 = get_hash(i + half_len, i + 2 * half_len)

                if h1 == h2:
                    # Verify and add
                    sub = text[i:i + 2 * half_len]
                    if sub[:half_len] == sub[half_len:]:
                        result.add(sub)

        return len(result)
