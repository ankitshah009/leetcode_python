#1781. Sum of Beauty of All Substrings
#Medium
#
#The beauty of a string is the difference in frequencies between the most
#frequent and least frequent characters.
#
#For example, the beauty of "abaacc" is 3 - 1 = 2.
#
#Given a string s, return the sum of beauty of all of its substrings.
#
#Example 1:
#Input: s = "aabcb"
#Output: 5
#
#Example 2:
#Input: s = "aabcbaa"
#Output: 17
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of only lowercase English letters.

class Solution:
    def beautySum(self, s: str) -> int:
        """
        Check all substrings, track frequency counts.
        """
        n = len(s)
        total = 0

        for i in range(n):
            count = [0] * 26

            for j in range(i, n):
                count[ord(s[j]) - ord('a')] += 1

                # Find max and min frequency (ignoring zeros)
                max_freq = max(count)
                min_freq = min(c for c in count if c > 0)

                total += max_freq - min_freq

        return total


class SolutionCounter:
    def beautySum(self, s: str) -> int:
        """
        Using Counter.
        """
        from collections import Counter

        n = len(s)
        total = 0

        for i in range(n):
            freq = Counter()
            for j in range(i, n):
                freq[s[j]] += 1
                max_freq = max(freq.values())
                min_freq = min(freq.values())
                total += max_freq - min_freq

        return total


class SolutionOptimized:
    def beautySum(self, s: str) -> int:
        """
        Track max and min more efficiently with frequency of frequencies.
        """
        from collections import Counter

        n = len(s)
        total = 0

        for i in range(n):
            char_freq = Counter()  # char -> frequency
            freq_count = Counter()  # frequency -> count of chars with that freq
            max_freq = 0

            for j in range(i, n):
                c = s[j]
                old_freq = char_freq[c]

                if old_freq > 0:
                    freq_count[old_freq] -= 1
                    if freq_count[old_freq] == 0:
                        del freq_count[old_freq]

                new_freq = old_freq + 1
                char_freq[c] = new_freq
                freq_count[new_freq] += 1
                max_freq = max(max_freq, new_freq)

                min_freq = min(freq_count.keys())
                total += max_freq - min_freq

        return total
