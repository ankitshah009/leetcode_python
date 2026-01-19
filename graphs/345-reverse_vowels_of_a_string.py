#345. Reverse Vowels of a String
#Easy
#
#Given a string s, reverse only all the vowels in the string and return it.
#
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
#and upper cases, more than once.
#
#Example 1:
#Input: s = "hello"
#Output: "holle"
#
#Example 2:
#Input: s = "leetcode"
#Output: "leotcede"
#
#Constraints:
#    1 <= s.length <= 3 * 10^5
#    s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        """Two pointers approach"""
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return ''.join(s_list)


class SolutionStack:
    """Extract vowels, reverse, put back"""

    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')

        # Extract all vowels
        vowels_in_s = [c for c in s if c in vowels]

        # Build result
        result = []
        for c in s:
            if c in vowels:
                result.append(vowels_in_s.pop())
            else:
                result.append(c)

        return ''.join(result)


class SolutionRegex:
    """Using regex (less efficient but concise)"""

    def reverseVowels(self, s: str) -> str:
        import re

        vowels = re.findall(r'[aeiouAEIOU]', s)
        return re.sub(r'[aeiouAEIOU]', lambda _: vowels.pop(), s)
