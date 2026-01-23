#1189. Maximum Number of Balloons
#Easy
#
#Given a string text, you want to use the characters of text to form as many
#instances of the word "balloon" as possible.
#
#You can use each character in text at most once. Return the maximum number of
#instances that can be formed.
#
#Example 1:
#Input: text = "nlaebolko"
#Output: 1
#
#Example 2:
#Input: text = "loonbalxballpoon"
#Output: 2
#
#Example 3:
#Input: text = "leetcode"
#Output: 0
#
#Constraints:
#    1 <= text.length <= 10^4
#    text consists of lower case English letters only.

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Count chars in text.
        balloon needs: b=1, a=1, l=2, o=2, n=1
        """
        count = Counter(text)

        # Characters needed for "balloon"
        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )


class SolutionExplicit:
    def maxNumberOfBalloons(self, text: str) -> int:
        """More explicit approach"""
        # Count occurrences of each needed character
        b = a = l = o = n = 0

        for c in text:
            if c == 'b':
                b += 1
            elif c == 'a':
                a += 1
            elif c == 'l':
                l += 1
            elif c == 'o':
                o += 1
            elif c == 'n':
                n += 1

        # "balloon" needs: b=1, a=1, l=2, o=2, n=1
        return min(b, a, l // 2, o // 2, n)


class SolutionGeneric:
    def maxNumberOfBalloons(self, text: str) -> int:
        """Generic solution for any target word"""
        target = "balloon"
        text_count = Counter(text)
        target_count = Counter(target)

        result = float('inf')
        for char, needed in target_count.items():
            available = text_count.get(char, 0)
            result = min(result, available // needed)

        return result if result != float('inf') else 0
