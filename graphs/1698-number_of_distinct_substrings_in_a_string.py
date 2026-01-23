#1698. Number of Distinct Substrings in a String
#Medium
#
#Given a string s, return the number of distinct substrings of s.
#
#A substring of a string is obtained by deleting any number of characters
#(possibly zero) from the beginning of the string and any number of characters
#(possibly zero) from the end of the string.
#
#Example 1:
#Input: s = "aabbaba"
#Output: 21
#Explanation: The set of distinct substrings is:
#["a","b","aa","ab","ba","bb","aab","abb","bab","bba","aba","aabb","abba",
#"bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
#
#Example 2:
#Input: s = "abcdefg"
#Output: 28
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of lowercase English letters.

class Solution:
    def countDistinct(self, s: str) -> int:
        """
        Use set to store all unique substrings.
        O(n^2) space and time.
        """
        substrings = set()

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substrings.add(s[i:j])

        return len(substrings)


class SolutionTrie:
    def countDistinct(self, s: str) -> int:
        """
        Trie-based approach for better space efficiency.
        """
        class TrieNode:
            def __init__(self):
                self.children = {}

        root = TrieNode()
        count = 0

        for i in range(len(s)):
            node = root
            for j in range(i, len(s)):
                char = s[j]
                if char not in node.children:
                    node.children[char] = TrieNode()
                    count += 1
                node = node.children[char]

        return count


class SolutionRollingHash:
    def countDistinct(self, s: str) -> int:
        """
        Rolling hash for substring comparison.
        """
        n = len(s)
        MOD = 2**63 - 1
        BASE = 31

        substrings = set()

        for length in range(1, n + 1):
            # Compute hash for first substring of this length
            h = 0
            power = 1

            for i in range(length):
                h = (h * BASE + ord(s[i]) - ord('a') + 1) % MOD
                if i < length - 1:
                    power = (power * BASE) % MOD

            substrings.add(h)

            # Rolling hash for remaining substrings
            for i in range(length, n):
                h = ((h - (ord(s[i - length]) - ord('a') + 1) * power) * BASE +
                     ord(s[i]) - ord('a') + 1) % MOD
                substrings.add(h)

        return len(substrings)


class SolutionSuffixArray:
    def countDistinct(self, s: str) -> int:
        """
        Suffix array approach for O(n log n) solution.
        Number of distinct substrings = n*(n+1)/2 - sum(LCP)
        """
        n = len(s)

        # Build suffix array
        suffix_array = sorted(range(n), key=lambda i: s[i:])

        # Compute LCP array
        def lcp(i: int, j: int) -> int:
            length = 0
            while i + length < n and j + length < n and s[i + length] == s[j + length]:
                length += 1
            return length

        total_lcp = 0
        for i in range(1, n):
            total_lcp += lcp(suffix_array[i - 1], suffix_array[i])

        total_substrings = n * (n + 1) // 2
        return total_substrings - total_lcp


class SolutionCompact:
    def countDistinct(self, s: str) -> int:
        """
        Compact set-based solution.
        """
        return len({s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)})
