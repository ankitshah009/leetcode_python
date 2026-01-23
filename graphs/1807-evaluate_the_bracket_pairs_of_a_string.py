#1807. Evaluate the Bracket Pairs of a String
#Medium
#
#You are given a string s that contains some bracket pairs, with each pair
#containing a non-empty key.
#
#For example, in the string "(name)is(age)yearsold", there are two bracket
#pairs that contain the keys "name" and "age".
#
#You know the values of a wide range of keys. This is represented by a 2D
#string array knowledge where each knowledge[i] = [key_i, value_i] indicates
#that key key_i has a value of value_i.
#
#You are tasked to evaluate all of the bracket pairs. When you evaluate a
#bracket pair that contains some key key_i, you will:
#- Replace key_i and the bracket pair with the key's corresponding value_i.
#- If you do not know the value of the key, you will replace key_i and the
#  bracket pair with a question mark "?" (without the quotation marks).
#
#Each key will appear at most once in your knowledge. There will not be any
#nested brackets in s.
#
#Return the resulting string after evaluating all of the bracket pairs.
#
#Example 1:
#Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
#Output: "bobistwoyearsold"
#
#Example 2:
#Input: s = "hi(name)", knowledge = [["a","b"]]
#Output: "hi?"
#
#Constraints:
#    1 <= s.length <= 10^5
#    0 <= knowledge.length <= 10^5
#    knowledge[i].length == 2
#    1 <= key_i.length, value_i.length <= 10
#    s consists of lowercase English letters and round brackets '(' and ')'.
#    Every open bracket '(' in s will have a corresponding close bracket ')'.
#    The key in each bracket pair of s will be non-empty.
#    There will not be any nested bracket pairs in s.
#    key_i and value_i consist of lowercase English letters.
#    Each key_i in knowledge is unique.

from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        """
        Build dict from knowledge and parse string.
        """
        lookup = {key: value for key, value in knowledge}
        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                # Find closing bracket
                j = i + 1
                while s[j] != ')':
                    j += 1
                key = s[i+1:j]
                result.append(lookup.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)


class SolutionRegex:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        """
        Using regex for replacement.
        """
        import re
        lookup = dict(knowledge)
        return re.sub(r'\((\w+)\)', lambda m: lookup.get(m.group(1), '?'), s)


class SolutionSplit:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        """
        Split by brackets approach.
        """
        lookup = dict(knowledge)
        result = []
        parts = s.replace(')', '(').split('(')

        for i, part in enumerate(parts):
            if i % 2 == 0:
                result.append(part)
            else:
                result.append(lookup.get(part, '?'))

        return ''.join(result)
