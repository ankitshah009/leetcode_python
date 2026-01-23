#1839. Longest Substring Of All Vowels in Order
#Medium
#
#A string is considered beautiful if it satisfies the following conditions:
#- Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least
#  once in it.
#- The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's,
#  all 'e's before 'i's, etc.).
#
#For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful,
#but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.
#
#Given a string word consisting of English vowels, return the length of the
#longest beautiful substring of word. If no such substring exists, return 0.
#
#A substring is a contiguous sequence of characters in a string.
#
#Example 1:
#Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
#Output: 13
#
#Example 2:
#Input: word = "aeeeiiiioooauuuaeiou"
#Output: 5
#
#Example 3:
#Input: word = "a"
#Output: 0
#
#Constraints:
#    1 <= word.length <= 5 * 10^5
#    word consists of characters 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        """
        Track length and number of unique vowels in current valid sequence.
        """
        max_len = 0
        length = 1
        unique = 1
        n = len(word)

        for i in range(1, n):
            if word[i] >= word[i - 1]:
                length += 1
                if word[i] != word[i - 1]:
                    unique += 1
            else:
                # Reset
                length = 1
                unique = 1

            if unique == 5:
                max_len = max(max_len, length)

        return max_len


class SolutionTwoPointers:
    def longestBeautifulSubstring(self, word: str) -> int:
        """
        Two pointers approach.
        """
        n = len(word)
        max_len = 0
        i = 0

        while i < n:
            # Start of potential beautiful substring
            if word[i] == 'a':
                j = i
                unique = 1

                while j + 1 < n and word[j + 1] >= word[j]:
                    if word[j + 1] != word[j]:
                        unique += 1
                    j += 1

                if unique == 5:
                    max_len = max(max_len, j - i + 1)

                i = j + 1
            else:
                i += 1

        return max_len


class SolutionState:
    def longestBeautifulSubstring(self, word: str) -> int:
        """
        State machine approach.
        """
        vowels = "aeiou"
        vowel_idx = {v: i for i, v in enumerate(vowels)}

        max_len = 0
        start = 0
        expected_idx = 0  # Index in "aeiou"

        for i, c in enumerate(word):
            idx = vowel_idx[c]

            if idx == expected_idx:
                # Same vowel, continue
                pass
            elif idx == expected_idx + 1:
                # Next vowel in sequence
                expected_idx = idx
            elif idx == 0:
                # Restart with 'a'
                start = i
                expected_idx = 0
            else:
                # Invalid transition
                start = i + 1
                expected_idx = 0

            if expected_idx == 4:  # Reached 'u'
                max_len = max(max_len, i - start + 1)

        return max_len
