#1023. Camelcase Matching
#Medium
#
#Given an array of strings queries and a string pattern, return a boolean
#array answer where answer[i] is true if queries[i] matches pattern, and
#false otherwise.
#
#A query word queries[i] matches pattern if you can insert lowercase English
#letters into pattern so that it equals the query. You may insert each
#character at any position and you may not insert any characters.
#
#Example 1:
#Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],
#       pattern = "FB"
#Output: [true,false,true,true,false]
#Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
#"FootBall" can be generated like this "F" + "oot" + "B" + "all".
#"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
#
#Example 2:
#Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],
#       pattern = "FoBa"
#Output: [true,false,true,false,false]
#
#Example 3:
#Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],
#       pattern = "FoBaT"
#Output: [false,true,false,false,false]
#
#Constraints:
#    1 <= pattern.length, queries.length <= 100
#    1 <= queries[i].length <= 100
#    queries[i] and pattern consist of English letters.

from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        """
        For each query, check if pattern is subsequence
        and no extra uppercase letters exist.
        """
        def matches(query: str) -> bool:
            p_idx = 0
            for c in query:
                if p_idx < len(pattern) and c == pattern[p_idx]:
                    p_idx += 1
                elif c.isupper():
                    return False
            return p_idx == len(pattern)

        return [matches(q) for q in queries]


class SolutionTwoPointer:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        """Explicit two-pointer approach"""
        def matches(query: str) -> bool:
            i, j = 0, 0
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper():
                    return False
                i += 1
            return j == len(pattern)

        return [matches(q) for q in queries]
