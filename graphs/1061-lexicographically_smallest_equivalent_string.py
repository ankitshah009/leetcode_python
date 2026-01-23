#1061. Lexicographically Smallest Equivalent String
#Medium
#
#You are given two strings of the same length s1 and s2 and a string baseStr.
#
#We say s1[i] and s2[i] are equivalent characters.
#For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd',
#and 'c' == 'e'.
#
#Equivalent characters follow the usual rules of any equivalence relation:
#    Reflexivity: 'a' == 'a'.
#    Symmetry: 'a' == 'b' implies 'b' == 'a'.
#    Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
#
#For example, given the equivalency information from s1 = "abc" and s2 = "cde",
#"acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the
#lexicographically smallest equivalent string of baseStr.
#
#Return the lexicographically smallest equivalent string of baseStr by using
#the equivalency information from s1 and s2.
#
#Example 1:
#Input: s1 = "parker", s2 = "morris", baseStr = "parser"
#Output: "makkek"
#
#Example 2:
#Input: s1 = "hello", s2 = "world", baseStr = "hold"
#Output: "hdld"
#
#Example 3:
#Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
#Output: "aauaaaaada"
#
#Constraints:
#    1 <= s1.length, s2.length, baseStr.length <= 1000
#    s1.length == s2.length
#    s1, s2, and baseStr consist of lowercase English letters.

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Union-Find with path compression.
        Keep track of smallest character in each component.
        """
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                # Union to smaller character
                if px < py:
                    parent[py] = px
                else:
                    parent[px] = py

        # Build equivalence relation
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        # Transform baseStr
        result = []
        for c in baseStr:
            smallest = find(ord(c) - ord('a'))
            result.append(chr(smallest + ord('a')))

        return ''.join(result)


class SolutionDFS:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """DFS to find smallest in component"""
        from collections import defaultdict

        graph = defaultdict(set)
        for c1, c2 in zip(s1, s2):
            graph[c1].add(c2)
            graph[c2].add(c1)

        # Find smallest in component using DFS
        smallest = {}

        def dfs(start):
            if start in smallest:
                return smallest[start]

            visited = set()
            stack = [start]
            component = []

            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                component.append(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            min_char = min(component)
            for c in component:
                smallest[c] = min_char

            return min_char

        result = []
        for c in baseStr:
            if c in graph or c in smallest:
                result.append(dfs(c))
            else:
                result.append(c)

        return ''.join(result)
