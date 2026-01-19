#395. Longest Substring with At Least K Repeating Characters
#Medium
#
#Given a string s and an integer k, return the length of the longest substring
#of s such that the frequency of each character in this substring is greater
#than or equal to k.
#
#if no such substring exists, return 0.
#
#Example 1:
#Input: s = "aaabb", k = 3
#Output: 3
#Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
#
#Example 2:
#Input: s = "ababbc", k = 2
#Output: 5
#Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and
#'b' is repeated 3 times.
#
#Constraints:
#    1 <= s.length <= 10^4
#    s consists of only lowercase English letters.
#    1 <= k <= 10^5

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Divide and conquer.
        Split on characters that appear < k times (they can't be in answer).
        """
        if len(s) < k:
            return 0

        count = Counter(s)

        # Find a character that appears < k times
        for char in count:
            if count[char] < k:
                # Split and recurse
                return max(self.longestSubstring(sub, k)
                          for sub in s.split(char))

        # All characters appear >= k times
        return len(s)


class SolutionSlidingWindow:
    """Sliding window with unique character count constraint"""

    def longestSubstring(self, s: str, k: int) -> int:
        max_length = 0

        # Try all possible unique character counts (1 to 26)
        for unique_target in range(1, 27):
            max_length = max(max_length,
                           self._longest_with_unique(s, k, unique_target))

        return max_length

    def _longest_with_unique(self, s, k, unique_target):
        """Find longest substring with exactly unique_target unique chars,
           each appearing >= k times"""
        count = {}
        left = 0
        max_length = 0
        unique = 0  # Unique characters in window
        count_at_least_k = 0  # Characters appearing >= k times

        for right in range(len(s)):
            # Add right character
            char = s[right]
            if char not in count:
                count[char] = 0
            count[char] += 1

            if count[char] == 1:
                unique += 1
            if count[char] == k:
                count_at_least_k += 1

            # Shrink window if too many unique characters
            while unique > unique_target:
                left_char = s[left]
                if count[left_char] == k:
                    count_at_least_k -= 1
                count[left_char] -= 1
                if count[left_char] == 0:
                    unique -= 1
                    del count[left_char]
                left += 1

            # Check if valid
            if unique == unique_target and unique == count_at_least_k:
                max_length = max(max_length, right - left + 1)

        return max_length


class SolutionIterative:
    """Iterative divide and conquer with queue"""

    def longestSubstring(self, s: str, k: int) -> int:
        from collections import deque

        if k <= 1:
            return len(s)

        max_length = 0
        queue = deque([(0, len(s))])

        while queue:
            start, end = queue.popleft()
            if end - start < k:
                continue

            count = Counter(s[start:end])
            split_char = None

            for char, cnt in count.items():
                if cnt < k:
                    split_char = char
                    break

            if split_char is None:
                max_length = max(max_length, end - start)
            else:
                # Split on this character
                i = start
                while i < end:
                    # Skip split characters
                    while i < end and s[i] == split_char:
                        i += 1
                    j = i
                    # Find end of segment
                    while j < end and s[j] != split_char:
                        j += 1
                    if j - i >= k:
                        queue.append((i, j))
                    i = j

        return max_length
