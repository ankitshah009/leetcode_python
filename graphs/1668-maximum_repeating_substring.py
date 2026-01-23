#1668. Maximum Repeating Substring
#Easy
#
#For a string sequence, a string word is k-repeating if word concatenated k
#times is a substring of sequence. The word's maximum k-repeating value is the
#highest value k where word is k-repeating in sequence. If word is not a
#substring of sequence, word's maximum k-repeating value is 0.
#
#Given strings sequence and word, return the maximum k-repeating value of word
#in sequence.
#
#Example 1:
#Input: sequence = "ababc", word = "ab"
#Output: 2
#Explanation: "abab" is a substring in "ababc".
#
#Example 2:
#Input: sequence = "ababc", word = "ba"
#Output: 1
#Explanation: "ba" is a substring in "ababc". "baba" is not a substring.
#
#Example 3:
#Input: sequence = "ababc", word = "ac"
#Output: 0
#Explanation: "ac" is not a substring in "ababc".
#
#Constraints:
#    1 <= sequence.length <= 100
#    1 <= word.length <= 100
#    sequence and word contains only lowercase English letters.

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        Try increasing values of k until word*k is not in sequence.
        """
        k = 0
        while word * (k + 1) in sequence:
            k += 1
        return k


class SolutionBinarySearch:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        Binary search for maximum k.
        """
        if word not in sequence:
            return 0

        left, right = 1, len(sequence) // len(word)

        while left < right:
            mid = (left + right + 1) // 2
            if word * mid in sequence:
                left = mid
            else:
                right = mid - 1

        return left


class SolutionDP:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        DP approach - track repeating count at each position.
        """
        n, m = len(sequence), len(word)
        # dp[i] = k if sequence[i-k*m:i] == word * k
        dp = [0] * (n + 1)

        for i in range(m, n + 1):
            if sequence[i - m:i] == word:
                dp[i] = dp[i - m] + 1

        return max(dp)


class SolutionKMP:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        KMP-based approach for pattern matching.
        """
        def compute_lps(pattern: str) -> list:
            m = len(pattern)
            lps = [0] * m
            length = 0
            i = 1

            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1

            return lps

        if word not in sequence:
            return 0

        # Find all starting positions of word in sequence
        positions = []
        n, m = len(sequence), len(word)
        lps = compute_lps(word)

        i = j = 0
        while i < n:
            if sequence[i] == word[j]:
                i += 1
                j += 1

                if j == m:
                    positions.append(i - m)
                    j = lps[j - 1]
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        # Find maximum consecutive occurrences
        if not positions:
            return 0

        max_k = 1
        current_k = 1

        for i in range(1, len(positions)):
            if positions[i] == positions[i - 1] + m:
                current_k += 1
                max_k = max(max_k, current_k)
            else:
                current_k = 1

        return max_k


class SolutionSimple:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        Simple iterative approach.
        """
        max_possible = len(sequence) // len(word)

        for k in range(max_possible, 0, -1):
            if word * k in sequence:
                return k

        return 0
