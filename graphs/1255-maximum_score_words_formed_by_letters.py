#1255. Maximum Score Words Formed by Letters
#Hard
#
#Given a list of words, list of single letters (might be repeating) and score
#of every character.
#
#Return the maximum score of any valid set of words formed by using the given
#letters (words[i] cannot be used two or more times).
#
#It is not necessary to use all characters in letters and each letter can only
#be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by
#score[0], score[1], ... , score[25] respectively.
#
#Example 1:
#Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"],
#score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
#Output: 23
#Explanation: Score  a=1, c=9, d=5, g=3, o=2
#"dad" (5+1+5) = 11
#"good" (3+2+2+5) = 12
#Score = 11 + 12 = 23
#
#Example 2:
#Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"],
#score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
#Output: 27
#Explanation: Score  a=4, b=4, c=4, x=5, z=10
#"ax" (4+5) = 9
#"bx" (4+5) = 9
#"cx" (4+5) = 9
#Score = 9 + 9 + 9 = 27
#
#Constraints:
#    1 <= words.length <= 14
#    1 <= words[i].length <= 15
#    1 <= letters.length <= 100
#    letters[i].length == 1
#    score.length == 26
#    0 <= score[i] <= 10

from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        Backtracking: Try all subsets of words.
        n <= 14, so 2^14 subsets is manageable.
        """
        available = Counter(letters)
        n = len(words)

        def word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)

        def word_count(word):
            return Counter(word)

        def can_form(word_cnt, avail):
            return all(word_cnt[c] <= avail[c] for c in word_cnt)

        max_score = 0

        def backtrack(idx, current_score, avail):
            nonlocal max_score
            max_score = max(max_score, current_score)

            for i in range(idx, n):
                word = words[i]
                cnt = word_count(word)

                if can_form(cnt, avail):
                    # Use this word
                    new_avail = avail.copy()
                    for c in cnt:
                        new_avail[c] -= cnt[c]

                    backtrack(i + 1, current_score + word_score(word), new_avail)

        backtrack(0, 0, available)
        return max_score


class SolutionBitmask:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """Enumerate all subsets using bitmask"""
        available = [0] * 26
        for c in letters:
            available[ord(c) - ord('a')] += 1

        n = len(words)
        max_score = 0

        for mask in range(1 << n):
            # Check if this subset is valid
            used = [0] * 26
            total_score = 0

            for i in range(n):
                if mask & (1 << i):
                    for c in words[i]:
                        idx = ord(c) - ord('a')
                        used[idx] += 1
                        total_score += score[idx]

            # Validate
            valid = all(used[i] <= available[i] for i in range(26))
            if valid:
                max_score = max(max_score, total_score)

        return max_score
