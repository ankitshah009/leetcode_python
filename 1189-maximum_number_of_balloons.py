#1189. Maximum Number of Balloons
#Easy
#
#Given a string text, you want to use the characters of text to form as many instances of the
#word "balloon" as possible.
#
#You can use each character in text at most once. Return the maximum number of instances that
#can be formed.
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
        count = Counter(text)

        # "balloon" needs: b, a, l, l, o, o, n
        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )
