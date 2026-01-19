#267. Palindrome Permutation II
#Medium
#
#Given a string s, return all the palindromic permutations (without duplicates)
#of it.
#
#You may return the answer in any order. If s has no palindromic permutation,
#return an empty list.
#
#Example 1:
#Input: s = "aabb"
#Output: ["abba","baab"]
#
#Example 2:
#Input: s = "abc"
#Output: []
#
#Constraints:
#    1 <= s.length <= 16
#    s consists of only lowercase English letters.

from collections import Counter

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # Count character frequencies
        count = Counter(s)

        # Check if palindrome is possible
        # At most one character can have odd frequency
        odd_chars = [char for char, freq in count.items() if freq % 2 == 1]

        if len(odd_chars) > 1:
            return []

        # Build half of palindrome
        middle = odd_chars[0] if odd_chars else ""
        half_chars = []
        for char, freq in count.items():
            half_chars.extend([char] * (freq // 2))

        # Generate permutations of half
        result = []
        used = [False] * len(half_chars)
        half_chars.sort()  # Sort to handle duplicates

        def backtrack(path):
            if len(path) == len(half_chars):
                half = ''.join(path)
                result.append(half + middle + half[::-1])
                return

            for i in range(len(half_chars)):
                # Skip used characters
                if used[i]:
                    continue
                # Skip duplicates
                if i > 0 and half_chars[i] == half_chars[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(half_chars[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return result

    # Using itertools permutations
    def generatePalindromesItertools(self, s: str) -> List[str]:
        from itertools import permutations

        count = Counter(s)
        odd_chars = [char for char, freq in count.items() if freq % 2 == 1]

        if len(odd_chars) > 1:
            return []

        middle = odd_chars[0] if odd_chars else ""
        half_chars = []
        for char, freq in count.items():
            half_chars.extend([char] * (freq // 2))

        result = set()
        for perm in permutations(half_chars):
            half = ''.join(perm)
            result.add(half + middle + half[::-1])

        return list(result)
