#767. Reorganize String
#Medium
#
#Given a string s, rearrange the characters of s so that any two adjacent
#characters are not the same.
#
#Return any possible rearrangement of s or return "" if not possible.
#
#Example 1:
#Input: s = "aab"
#Output: "aba"
#
#Example 2:
#Input: s = "aaab"
#Output: ""
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of lowercase English letters.

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Use max-heap to always pick the most frequent char that isn't the previous.
        """
        count = Counter(s)
        n = len(s)

        # Check if possible
        max_count = max(count.values())
        if max_count > (n + 1) // 2:
            return ""

        # Max-heap (negate for max behavior)
        heap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(heap)

        result = []
        prev_cnt, prev_char = 0, ''

        while heap:
            cnt, char = heapq.heappop(heap)
            result.append(char)

            # Put previous back if it still has count
            if prev_cnt < 0:
                heapq.heappush(heap, (prev_cnt, prev_char))

            prev_cnt, prev_char = cnt + 1, char  # cnt is negative

        return ''.join(result)


class SolutionSorting:
    """Sort by frequency and fill alternating positions"""

    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)

        max_count = max(count.values())
        if max_count > (n + 1) // 2:
            return ""

        # Sort chars by frequency (descending)
        sorted_chars = sorted(count.keys(), key=lambda x: -count[x])

        # Flatten into list of chars
        chars = []
        for char in sorted_chars:
            chars.extend([char] * count[char])

        # Fill even indices first, then odd
        result = [''] * n
        idx = 0

        for char in chars:
            result[idx] = char
            idx += 2
            if idx >= n:
                idx = 1

        return ''.join(result)


class SolutionOddEven:
    """Fill most frequent at even positions"""

    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)

        max_count = max(count.values())
        if max_count > (n + 1) // 2:
            return ""

        result = [''] * n
        idx = 0

        # Sort by count, most frequent first
        for char, cnt in count.most_common():
            for _ in range(cnt):
                result[idx] = char
                idx += 2
                if idx >= n:
                    idx = 1

        return ''.join(result)
