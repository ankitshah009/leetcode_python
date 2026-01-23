#1087. Brace Expansion
#Medium
#
#You are given a string s representing a list of words. Each letter in the
#word has one or more options.
#    If there is one option, the letter is represented as is.
#    If there is more than one option, then curly braces delimit the options.
#    For example, "{a,b,c}" represents options ["a", "b", "c"].
#
#For example, if s = "a{b,c}", the first letter is always 'a', but the
#second letter can be 'b' or 'c'. The original list is ["ab", "ac"].
#
#Return all words that can be formed in this manner, sorted in lexicographical
#order.
#
#Example 1:
#Input: s = "{a,b}c{d,e}f"
#Output: ["acdf","acef","bcdf","bcef"]
#
#Example 2:
#Input: s = "abcd"
#Output: ["abcd"]
#
#Constraints:
#    1 <= s.length <= 50
#    s consists of curly brackets '{}', commas ',', and lowercase English
#    letters.
#    s is guaranteed to be a valid input.
#    There are no nested curly brackets.
#    All characters inside a pair of consecutive opening and ending curly
#    brackets are different.

from typing import List

class Solution:
    def expand(self, s: str) -> List[str]:
        """
        Parse groups, then generate all combinations.
        """
        # Parse into list of character options
        groups = []
        i = 0

        while i < len(s):
            if s[i] == '{':
                # Find closing brace
                j = i + 1
                while s[j] != '}':
                    j += 1
                # Extract options
                options = sorted(s[i+1:j].split(','))
                groups.append(options)
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1

        # Generate all combinations
        result = []

        def backtrack(idx, current):
            if idx == len(groups):
                result.append(''.join(current))
                return

            for option in groups[idx]:
                current.append(option)
                backtrack(idx + 1, current)
                current.pop()

        backtrack(0, [])
        return result


class SolutionIterative:
    def expand(self, s: str) -> List[str]:
        """Iterative cartesian product"""
        from itertools import product

        groups = []
        i = 0

        while i < len(s):
            if s[i] == '{':
                j = s.index('}', i)
                options = sorted(s[i+1:j].split(','))
                groups.append(options)
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1

        return sorted(''.join(combo) for combo in product(*groups))


class SolutionQueue:
    def expand(self, s: str) -> List[str]:
        """BFS-style generation"""
        from collections import deque

        groups = []
        i = 0

        while i < len(s):
            if s[i] == '{':
                j = s.index('}', i)
                groups.append(sorted(s[i+1:j].split(',')))
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1

        result = ['']
        for group in groups:
            new_result = []
            for prefix in result:
                for char in group:
                    new_result.append(prefix + char)
            result = new_result

        return sorted(result)
