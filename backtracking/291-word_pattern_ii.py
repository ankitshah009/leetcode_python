#291. Word Pattern II
#Medium
#
#Given a pattern and a string s, return true if s matches the pattern.
#
#A string s matches a pattern if there is some bijective mapping of single
#characters to non-empty strings such that if each character in pattern is
#replaced by the string it maps to, then the resulting string is s. A bijective
#mapping means that no two characters map to the same string, and no character
#maps to two different strings.
#
#Example 1:
#Input: pattern = "abab", s = "redblueredblue"
#Output: true
#Explanation: One possible mapping is as follows:
#'a' -> "red"
#'b' -> "blue"
#
#Example 2:
#Input: pattern = "aaaa", s = "asdasdasdasd"
#Output: true
#Explanation: One possible mapping is as follows:
#'a' -> "asd"
#
#Example 3:
#Input: pattern = "aabb", s = "xyzabcxzyabc"
#Output: false
#
#Constraints:
#    1 <= pattern.length, s.length <= 20
#    pattern and s consist of only lowercase English letters.

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        word_to_char = {}

        def backtrack(p_idx, s_idx):
            # Base case: both pattern and string exhausted
            if p_idx == len(pattern) and s_idx == len(s):
                return True

            # One exhausted but not the other
            if p_idx == len(pattern) or s_idx == len(s):
                return False

            char = pattern[p_idx]

            # If character already mapped
            if char in char_to_word:
                word = char_to_word[char]
                # Check if string starts with mapped word
                if not s[s_idx:].startswith(word):
                    return False
                return backtrack(p_idx + 1, s_idx + len(word))

            # Try all possible substrings as mapping for current character
            for i in range(s_idx + 1, len(s) + 1):
                word = s[s_idx:i]

                # Skip if word already mapped to different character
                if word in word_to_char:
                    continue

                # Try this mapping
                char_to_word[char] = word
                word_to_char[word] = char

                if backtrack(p_idx + 1, i):
                    return True

                # Backtrack
                del char_to_word[char]
                del word_to_char[word]

            return False

        return backtrack(0, 0)

    # With pruning optimization
    def wordPatternMatchOptimized(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        word_to_char = {}

        def backtrack(p_idx, s_idx):
            if p_idx == len(pattern) and s_idx == len(s):
                return True

            if p_idx == len(pattern) or s_idx == len(s):
                return False

            char = pattern[p_idx]

            if char in char_to_word:
                word = char_to_word[char]
                if not s[s_idx:].startswith(word):
                    return False
                return backtrack(p_idx + 1, s_idx + len(word))

            # Pruning: remaining pattern chars need at least 1 char each
            remaining_pattern = len(pattern) - p_idx
            remaining_string = len(s) - s_idx

            for i in range(s_idx + 1, s_idx + remaining_string - remaining_pattern + 2):
                word = s[s_idx:i]

                if word in word_to_char:
                    continue

                char_to_word[char] = word
                word_to_char[word] = char

                if backtrack(p_idx + 1, i):
                    return True

                del char_to_word[char]
                del word_to_char[word]

            return False

        return backtrack(0, 0)
