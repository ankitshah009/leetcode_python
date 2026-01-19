#387. First Unique Character in a String
#Easy
#
#Given a string s, find the first non-repeating character in it and return its
#index. If it does not exist, return -1.
#
#Example 1:
#Input: s = "leetcode"
#Output: 0
#Explanation: The character 'l' at index 0 is the first character that does not
#occur at any other index.
#
#Example 2:
#Input: s = "loveleetcode"
#Output: 2
#
#Example 3:
#Input: s = "aabb"
#Output: -1
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of only lowercase English letters.

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """Count characters, then find first with count 1"""
        count = Counter(s)

        for i, char in enumerate(s):
            if count[char] == 1:
                return i

        return -1


class SolutionArray:
    """Using array for lowercase letters"""

    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        for i, char in enumerate(s):
            if count[ord(char) - ord('a')] == 1:
                return i

        return -1


class SolutionIndex:
    """Track first and last occurrence"""

    def firstUniqChar(self, s: str) -> int:
        first_idx = {}
        repeated = set()

        for i, char in enumerate(s):
            if char in repeated:
                continue
            if char in first_idx:
                repeated.add(char)
                del first_idx[char]
            else:
                first_idx[char] = i

        if not first_idx:
            return -1

        return min(first_idx.values())


class SolutionOrderedDict:
    """Using OrderedDict to maintain insertion order"""

    def firstUniqChar(self, s: str) -> int:
        from collections import OrderedDict

        char_idx = OrderedDict()
        repeated = set()

        for i, char in enumerate(s):
            if char in repeated:
                continue
            if char in char_idx:
                repeated.add(char)
                del char_idx[char]
            else:
                char_idx[char] = i

        if not char_idx:
            return -1

        # First item in OrderedDict is the first unique character
        return next(iter(char_idx.values()))
