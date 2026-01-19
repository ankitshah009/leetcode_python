#1915. Number of Wonderful Substrings
#Medium
#
#A wonderful string is a string where at most one letter appears an odd number of times.
#
#For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
#
#Given a string word that consists of the first ten lowercase English letters ('a' through 'j'),
#return the number of wonderful non-empty substrings in word. If the same substring appears
#multiple times in word, then count each occurrence separately.
#
#A substring is a contiguous sequence of characters in a string.
#
#Example 1:
#Input: word = "aba"
#Output: 4
#Explanation: The four wonderful substrings are underlined below:
#- "aba" -> "a"
#- "aba" -> "b"
#- "aba" -> "a"
#- "aba" -> "aba"
#
#Example 2:
#Input: word = "aabb"
#Output: 9
#Explanation: The nine wonderful substrings are underlined below:
#- "aabb" -> "a"
#- "aabb" -> "aa"
#- "aabb" -> "aab"
#- "aabb" -> "aabb"
#- "aabb" -> "a"
#- "aabb" -> "abb"
#- "aabb" -> "b"
#- "aabb" -> "bb"
#- "aabb" -> "b"
#
#Example 3:
#Input: word = "he"
#Output: 2
#Explanation: The two wonderful substrings are underlined below:
#- "he" -> "h"
#- "he" -> "e"
#
#Constraints:
#    1 <= word.length <= 10^5
#    word consists of lowercase English letters from 'a' to 'j'.

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Use bitmask to track parity of each character (0-9 for a-j)
        # mask[i] = 1 if character i has appeared odd times
        # Wonderful = all bits 0, or exactly one bit is 1

        count = {0: 1}  # Empty prefix has mask 0
        mask = 0
        result = 0

        for char in word:
            # Toggle bit for current character
            mask ^= (1 << (ord(char) - ord('a')))

            # Count substrings where all characters appear even times
            result += count.get(mask, 0)

            # Count substrings where exactly one character appears odd times
            for i in range(10):
                result += count.get(mask ^ (1 << i), 0)

            count[mask] = count.get(mask, 0) + 1

        return result
