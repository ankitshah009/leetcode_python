#1055. Shortest Way to Form String
#Medium
#
#A subsequence of a string is a new string that is formed from the original
#string by deleting some (can be none) of the characters without disturbing
#the relative positions of the remaining characters.
#
#Given two strings source and target, return the minimum number of subsequences
#of source such that their concatenation equals target. If the task is
#impossible, return -1.
#
#Example 1:
#Input: source = "abc", target = "abcbc"
#Output: 2
#Explanation: The target "abcbc" can be formed by "abc" and "bc", which are
#subsequences of source "abc".
#
#Example 2:
#Input: source = "abc", target = "acdbc"
#Output: -1
#Explanation: The target string cannot be constructed from the subsequences
#of source string due to the character "d" in target string.
#
#Example 3:
#Input: source = "xyz", target = "xzyxz"
#Output: 3
#Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
#
#Constraints:
#    1 <= source.length, target.length <= 1000
#    source and target consist of lowercase English letters.

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        Greedy: For each iteration through source, match as many
        characters of target as possible.
        """
        source_chars = set(source)

        # Check if all target chars exist in source
        for c in target:
            if c not in source_chars:
                return -1

        count = 0
        target_idx = 0

        while target_idx < len(target):
            count += 1
            # Go through source and match target chars
            for c in source:
                if target_idx < len(target) and c == target[target_idx]:
                    target_idx += 1

        return count


class SolutionBinarySearch:
    def shortestWay(self, source: str, target: str) -> int:
        """
        Precompute positions of each character in source.
        Use binary search to find next occurrence.
        """
        from collections import defaultdict
        import bisect

        # Map char -> sorted list of indices
        char_indices = defaultdict(list)
        for i, c in enumerate(source):
            char_indices[c].append(i)

        count = 1
        source_idx = 0

        for c in target:
            if c not in char_indices:
                return -1

            indices = char_indices[c]
            # Find smallest index >= source_idx
            pos = bisect.bisect_left(indices, source_idx)

            if pos == len(indices):
                # Wrap around to new iteration of source
                count += 1
                source_idx = indices[0] + 1
            else:
                source_idx = indices[pos] + 1

        return count


class SolutionNextChar:
    def shortestWay(self, source: str, target: str) -> int:
        """
        Precompute next[i][c] = next position of char c starting from i.
        """
        m = len(source)

        # next_char[i][c] = smallest j >= i where source[j] = c, or -1
        # For efficiency, store next occurrence for each position
        next_char = [[-1] * 26 for _ in range(m + 1)]

        for c in range(26):
            next_pos = -1
            for i in range(m - 1, -1, -1):
                if ord(source[i]) - ord('a') == c:
                    next_pos = i
                next_char[i][c] = next_pos

        count = 1
        source_idx = 0

        for c in target:
            c_idx = ord(c) - ord('a')

            if next_char[0][c_idx] == -1:
                return -1

            if next_char[source_idx][c_idx] == -1:
                # Need new iteration
                count += 1
                source_idx = next_char[0][c_idx] + 1
            else:
                source_idx = next_char[source_idx][c_idx] + 1

        return count
