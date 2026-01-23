#1156. Swap For Longest Repeated Character Substring
#Medium
#
#You are given a string text. You can swap two of the characters in the text.
#
#Return the length of the longest substring with repeated characters.
#
#Example 1:
#Input: text = "ababa"
#Output: 3
#Explanation: We can swap the first 'b' with the last 'a', or swap the last 'b'
#with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.
#
#Example 2:
#Input: text = "aaabaaa"
#Output: 6
#Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get
#longest repeated character substring "aaaaaa" with length 6.
#
#Example 3:
#Input: text = "aaaaa"
#Output: 5
#
#Constraints:
#    1 <= text.length <= 2 * 10^4
#    text consist of lowercase English letters only.

from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        """
        Group consecutive chars, then consider merging groups
        separated by one different char.
        """
        # Count total occurrences of each char
        total = Counter(text)

        # Create groups of consecutive same chars
        groups = []
        i = 0
        while i < len(text):
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1
            groups.append((text[i], j - i))
            i = j

        result = 0
        n = len(groups)

        for i, (char, length) in enumerate(groups):
            # Case 1: Single group, can extend by 1 if more chars exist
            extend = min(length + 1, total[char])
            result = max(result, extend)

            # Case 2: Two groups of same char separated by one different char
            if i + 2 < n and groups[i + 1][1] == 1 and groups[i + 2][0] == char:
                combined = length + groups[i + 2][1]
                # Can extend by 1 if more chars of same type exist elsewhere
                if total[char] > combined:
                    combined += 1
                result = max(result, combined)

        return result


class SolutionSlidingWindow:
    def maxRepOpt1(self, text: str) -> int:
        """Sliding window for each character"""
        total = Counter(text)
        result = 0

        for char in set(text):
            # Find longest window containing only 'char' with at most 1 swap
            left = 0
            count = 0  # Count of 'char' in window
            max_len = 0

            for right in range(len(text)):
                if text[right] == char:
                    count += 1

                # Window is valid if non-char count <= 1
                while (right - left + 1) - count > 1:
                    if text[left] == char:
                        count -= 1
                    left += 1

                # Can only use chars that exist
                window_len = min(right - left + 1, total[char])
                max_len = max(max_len, window_len)

            result = max(result, max_len)

        return result
