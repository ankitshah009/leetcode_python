#159. Longest Substring with At Most Two Distinct Characters
#Medium
#
#Given a string s, return the length of the longest substring that contains at
#most two distinct characters.
#
#Example 1:
#Input: s = "eceba"
#Output: 3
#Explanation: The substring is "ece" which its length is 3.
#
#Example 2:
#Input: s = "ccaabbb"
#Output: 5
#Explanation: The substring is "aabbb" which its length is 5.
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of English letters.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict

        char_count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            char_count[s[right]] += 1

            # Shrink window until we have at most 2 distinct characters
            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

    # Alternative approach tracking last occurrence index
    def lengthOfLongestSubstringTwoDistinctAlt(self, s: str) -> int:
        last_occurrence = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            last_occurrence[char] = right

            if len(last_occurrence) > 2:
                # Remove character with smallest last occurrence
                min_idx = min(last_occurrence.values())
                del last_occurrence[s[min_idx]]
                left = min_idx + 1

            max_len = max(max_len, right - left + 1)

        return max_len
