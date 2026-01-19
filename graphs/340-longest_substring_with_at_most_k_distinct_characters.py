#340. Longest Substring with At Most K Distinct Characters
#Medium
#
#Given a string s and an integer k, return the length of the longest substring
#of s that contains at most k distinct characters.
#
#Example 1:
#Input: s = "eceba", k = 2
#Output: 3
#Explanation: The substring is "ece" with length 3.
#
#Example 2:
#Input: s = "aa", k = 1
#Output: 2
#Explanation: The substring is "aa" with length 2.
#
#Constraints:
#    1 <= s.length <= 5 * 10^4
#    0 <= k <= 50

from collections import defaultdict, OrderedDict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Sliding window with hash map"""
        if k == 0:
            return 0

        char_count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            char_count[s[right]] += 1

            # Shrink window if we have more than k distinct characters
            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


class SolutionOrderedDict:
    """Using OrderedDict to track last occurrence"""

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        # Map character to its rightmost index
        last_seen = OrderedDict()
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # Remove and re-add to update order
            if char in last_seen:
                del last_seen[char]
            last_seen[char] = right

            if len(last_seen) > k:
                # Remove leftmost character
                _, left_idx = last_seen.popitem(last=False)
                left = left_idx + 1

            max_len = max(max_len, right - left + 1)

        return max_len


class SolutionArray:
    """Using array for ASCII characters"""

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        count = [0] * 128
        distinct = 0
        left = 0
        max_len = 0

        for right in range(len(s)):
            if count[ord(s[right])] == 0:
                distinct += 1
            count[ord(s[right])] += 1

            while distinct > k:
                count[ord(s[left])] -= 1
                if count[ord(s[left])] == 0:
                    distinct -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
