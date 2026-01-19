#767. Reorganize String
#Medium
#
#Given a string s, rearrange the characters of s so that any two adjacent characters are not
#the same.
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
        count = Counter(s)
        n = len(s)

        # Check if possible
        max_count = max(count.values())
        if max_count > (n + 1) // 2:
            return ""

        # Use max heap (negate for max heap behavior)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        result = []
        prev_freq, prev_char = 0, ''

        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char)

            # Add back the previous character if it still has remaining count
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            prev_freq = freq + 1  # Use one occurrence
            prev_char = char

        return ''.join(result)
