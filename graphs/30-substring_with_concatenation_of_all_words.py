#30. Substring with Concatenation of All Words
#Hard
#
#You are given a string s and an array of strings words. All the strings of words
#are of the same length.
#
#A concatenated string is a string that exactly contains all the strings of any
#permutation of words concatenated.
#
#Return an array of the starting indices of all the concatenated substrings in s.
#You can return the answer in any order.
#
#Example 1:
#Input: s = "barfoothefoobarman", words = ["foo","bar"]
#Output: [0,9]
#Explanation: The substring starting at 0 is "barfoo". It is the concatenation
#of ["bar","foo"] which is a permutation of words.
#The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"]
#which is a permutation of words.
#
#Example 2:
#Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
#Output: []
#
#Example 3:
#Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
#Output: [6,9,12]
#
#Constraints:
#    1 <= s.length <= 10^4
#    1 <= words.length <= 5000
#    1 <= words[i].length <= 30
#    s and words[i] consist of lowercase English letters.

from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Sliding window with word counting.
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            current_freq = Counter()
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_freq:
                    current_freq[word] += 1
                    count += 1

                    # Shrink window if word appears too many times
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Check if all words are matched
                    if count == word_count:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    # Reset window
                    current_freq.clear()
                    count = 0
                    left = j + word_len

        return result


class SolutionBruteForce:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Check each starting position - O(n * m * k) where n = len(s),
        m = word count, k = word length.
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []

        for i in range(len(s) - total_len + 1):
            seen = Counter()
            valid = True

            for j in range(word_count):
                word_start = i + j * word_len
                word = s[word_start:word_start + word_len]

                if word not in word_freq:
                    valid = False
                    break

                seen[word] += 1

                if seen[word] > word_freq[word]:
                    valid = False
                    break

            if valid:
                result.append(i)

        return result


class SolutionOptimized:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Optimized with early termination checks.
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)

        if n < total_len:
            return []

        word_freq = Counter(words)
        result = []

        # Check each possible starting position within word_len
        for start in range(word_len):
            window_freq = Counter()
            left = start
            matched = 0

            for right in range(start, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_freq:
                    window_freq[word] += 1

                    if window_freq[word] == word_freq[word]:
                        matched += 1
                    elif window_freq[word] == word_freq[word] + 1:
                        matched -= 1

                    # Shrink from left if window too large
                    while right - left >= total_len:
                        left_word = s[left:left + word_len]
                        if window_freq[left_word] == word_freq[left_word]:
                            matched -= 1
                        elif window_freq[left_word] == word_freq[left_word] + 1:
                            matched += 1
                        window_freq[left_word] -= 1
                        left += word_len

                    if matched == len(word_freq):
                        result.append(left)
                else:
                    window_freq.clear()
                    matched = 0
                    left = right + word_len

        return result
