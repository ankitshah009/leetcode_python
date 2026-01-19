#30. Substring with Concatenation of All Words
#Hard
#
#You are given a string s and an array of strings words. All the strings of words are of
#the same length.
#
#A concatenated string is a string that exactly contains all the strings of any permutation
#of words concatenated.
#
#Return an array of the starting indices of all the concatenated substrings in s. You can
#return the answer in any order.
#
#Example 1:
#Input: s = "barfoothefoobarman", words = ["foo","bar"]
#Output: [0,9]
#Explanation:
#The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
#The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
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

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(len(s) - total_len + 1):
            seen = {}
            j = 0
            while j < num_words:
                word = s[i + j * word_len:i + (j + 1) * word_len]
                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    if seen[word] > word_count[word]:
                        break
                else:
                    break
                j += 1

            if j == num_words:
                result.append(i)

        return result
