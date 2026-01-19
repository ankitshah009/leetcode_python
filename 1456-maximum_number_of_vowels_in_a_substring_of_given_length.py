#1456. Maximum Number of Vowels in a Substring of Given Length
#Medium
#
#Given a string s and an integer k, return the maximum number of vowel letters in any
#substring of s with length k.
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
        vowels = set('aeiou')

        # Count vowels in first window
        count = sum(1 for char in s[:k] if char in vowels)
        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            # Add new character
            if s[i] in vowels:
                count += 1
            # Remove old character
            if s[i - k] in vowels:
                count -= 1

            max_count = max(max_count, count)

        return max_count
