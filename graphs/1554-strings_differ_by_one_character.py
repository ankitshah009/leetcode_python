#1554. Strings Differ by One Character
#Medium
#
#Given a list of strings dict where all the strings are of the same length.
#
#Return true if there are 2 strings that only differ by 1 character in the same
#index, otherwise return false.
#
#Example 1:
#Input: dict = ["abcd","acbd", "aacd"]
#Output: true
#Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.
#
#Example 2:
#Input: dict = ["ab","cd","yz"]
#Output: false
#
#Example 3:
#Input: dict = ["abcd","cccc","abyd","abab"]
#Output: true
#
#Constraints:
#    The number of characters in dict <= 10^5
#    dict[i].length == dict[j].length
#    dict[i] should be unique.
#    dict[i] contains only lowercase English letters.

from typing import List

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        """
        For each position, create a pattern with that position masked.
        Two strings differ by one char if they match in all but one position.

        Use hashing to check for duplicates efficiently.
        """
        if not dict:
            return False

        n = len(dict)
        m = len(dict[0])

        for pos in range(m):
            # Create patterns with position pos masked
            seen = set()

            for s in dict:
                # Create pattern: s[:pos] + '*' + s[pos+1:]
                pattern = s[:pos] + s[pos + 1:]

                if pattern in seen:
                    return True
                seen.add(pattern)

        return False


class SolutionRollingHash:
    def differByOne(self, dict: List[str]) -> bool:
        """
        Rolling hash approach for O(n * m) time complexity.
        """
        if not dict:
            return False

        n = len(dict)
        m = len(dict[0])
        MOD = 10**9 + 7
        BASE = 26

        # Compute hash for each string
        hashes = []
        for s in dict:
            h = 0
            for c in s:
                h = (h * BASE + ord(c) - ord('a')) % MOD
            hashes.append(h)

        # Precompute powers of BASE
        powers = [1] * (m + 1)
        for i in range(1, m + 1):
            powers[i] = (powers[i - 1] * BASE) % MOD

        # For each position, compute hash with that char removed
        for pos in range(m):
            seen = {}

            for i, s in enumerate(dict):
                # Hash without char at position pos
                char_val = ord(s[pos]) - ord('a')
                contribution = (char_val * powers[m - 1 - pos]) % MOD
                new_hash = (hashes[i] - contribution) % MOD

                if new_hash in seen:
                    # Verify to avoid hash collision
                    for j in seen[new_hash]:
                        if self.differ_by_one_at(s, dict[j], pos):
                            return True
                    seen[new_hash].append(i)
                else:
                    seen[new_hash] = [i]

        return False

    def differ_by_one_at(self, s1: str, s2: str, pos: int) -> bool:
        """Check if s1 and s2 differ only at position pos."""
        for i in range(len(s1)):
            if i != pos and s1[i] != s2[i]:
                return False
        return s1[pos] != s2[pos]


class SolutionBruteForce:
    def differByOne(self, dict: List[str]) -> bool:
        """
        Brute force: Check all pairs.
        O(n^2 * m) time - works for small inputs.
        """
        n = len(dict)

        for i in range(n):
            for j in range(i + 1, n):
                diff_count = 0
                for k in range(len(dict[i])):
                    if dict[i][k] != dict[j][k]:
                        diff_count += 1
                        if diff_count > 1:
                            break

                if diff_count == 1:
                    return True

        return False


class SolutionTrie:
    def differByOne(self, dict: List[str]) -> bool:
        """
        Trie-based approach with wildcard matching.
        """
        class TrieNode:
            def __init__(self):
                self.children = {}

        root = TrieNode()

        for word in dict:
            # Insert word into trie
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]

        # For each word, try searching with one char different
        for word in dict:
            if self.search_with_one_diff(root, word, 0, False):
                return True

        return False

    def search_with_one_diff(self, node, word, idx, diffed):
        if idx == len(word):
            return diffed

        c = word[idx]

        for char, child in node.children.items():
            if char == c:
                if self.search_with_one_diff(child, word, idx + 1, diffed):
                    return True
            elif not diffed:
                if self.search_with_one_diff(child, word, idx + 1, True):
                    return True

        return False
