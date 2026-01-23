#1456. Maximum Number of Vowels in a Substring of Given Length
#Medium
#
#Given a string s and an integer k, return the maximum number of vowel letters
#in any substring of s with length k.
#
#Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
#
#Example 1:
#Input: s = "abciiidef", k = 3
#Output: 3
#Explanation: The substring "iii" contains 3 vowel letters.
#
#Example 2:
#Input: s = "aeiou", k = 2
#Output: 2
#Explanation: Any substring of length 2 contains 2 vowels.
#
#Example 3:
#Input: s = "leetcode", k = 3
#Output: 2
#Explanation: "lee", "eet" and "ode" contain 2 vowels.
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of lowercase English letters.
#    1 <= k <= s.length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Sliding window of size k.
        Track vowel count, update as window slides.
        """
        vowels = set('aeiou')

        # Count vowels in first window
        current = sum(1 for c in s[:k] if c in vowels)
        max_vowels = current

        # Slide window
        for i in range(k, len(s)):
            # Remove leftmost character
            if s[i - k] in vowels:
                current -= 1
            # Add new character
            if s[i] in vowels:
                current += 1

            max_vowels = max(max_vowels, current)

        return max_vowels


class SolutionExplicit:
    def maxVowels(self, s: str, k: int) -> int:
        """More explicit sliding window"""
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)

        # Initial window
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count

        # Slide
        for right in range(k, n):
            left = right - k

            # Add right, remove left
            if s[right] in vowels:
                count += 1
            if s[left] in vowels:
                count -= 1

            max_count = max(max_count, count)

        return max_count


class SolutionBitmap:
    def maxVowels(self, s: str, k: int) -> int:
        """Using precomputed vowel array"""
        is_vowel = [c in 'aeiou' for c in s]

        current = sum(is_vowel[:k])
        max_vowels = current

        for i in range(k, len(s)):
            current += is_vowel[i] - is_vowel[i - k]
            max_vowels = max(max_vowels, current)

        return max_vowels
