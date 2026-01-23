#854. K-Similar Strings
#Hard
#
#Strings s1 and s2 are k-similar (for some non-negative integer k) if we can
#swap the positions of two letters in s1 exactly k times so that the resulting
#string equals s2.
#
#Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are
#k-similar.
#
#Example 1:
#Input: s1 = "ab", s2 = "ba"
#Output: 1
#
#Example 2:
#Input: s1 = "abc", s2 = "bca"
#Output: 2
#
#Constraints:
#    1 <= s1.length <= 20
#    s2.length == s1.length
#    s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
#    s2 is an anagram of s1.

from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        """
        BFS: each state is a string, find minimum swaps to reach s2.
        """
        if s1 == s2:
            return 0

        visited = {s1}
        queue = deque([(s1, 0)])

        while queue:
            current, swaps = queue.popleft()

            # Find first mismatch
            i = 0
            while current[i] == s2[i]:
                i += 1

            # Try swapping with later positions that fix position i
            for j in range(i + 1, len(current)):
                if current[j] == s2[i] and current[j] != s2[j]:
                    # Swap positions i and j
                    new_str = current[:i] + current[j] + current[i+1:j] + current[i] + current[j+1:]

                    if new_str == s2:
                        return swaps + 1

                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append((new_str, swaps + 1))

        return -1


class SolutionDFS:
    """DFS with memoization"""

    def kSimilarity(self, s1: str, s2: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def min_swaps(s):
            if s == s2:
                return 0

            # Find first mismatch
            i = 0
            while s[i] == s2[i]:
                i += 1

            best = float('inf')

            for j in range(i + 1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    # Swap
                    new_s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                    best = min(best, 1 + min_swaps(new_s))

            return best

        return min_swaps(s1)


class SolutionGreedy:
    """Greedy with backtracking"""

    def kSimilarity(self, s1: str, s2: str) -> int:
        def min_swaps(s):
            s = list(s)
            swaps = 0

            for i in range(len(s)):
                if s[i] != s2[i]:
                    # Find best swap partner
                    for j in range(i + 1, len(s)):
                        if s[j] == s2[i]:
                            # Prefer swaps that fix both positions
                            if s[i] == s2[j]:
                                s[i], s[j] = s[j], s[i]
                                swaps += 1
                                break
                    else:
                        # No perfect swap, find any valid swap
                        for j in range(i + 1, len(s)):
                            if s[j] == s2[i]:
                                s[i], s[j] = s[j], s[i]
                                swaps += 1
                                break

            return swaps

        return min_swaps(s1)
