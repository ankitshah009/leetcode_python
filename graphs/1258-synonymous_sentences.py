#1258. Synonymous Sentences
#Medium
#
#You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti]
#indicates that si and ti are equivalent strings. You are also given a sentence text.
#
#Return all possible synonymous sentences sorted lexicographically.
#
#Example 1:
#Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
#text = "I am happy today but was sad yesterday"
#Output: ["I am cheerful today but was sad yesterday",
#         "I am cheerful today but was sorrow yesterday",
#         "I am happy today but was sad yesterday",
#         "I am happy today but was sorrow yesterday",
#         "I am joy today but was sad yesterday",
#         "I am joy today but was sorrow yesterday"]
#
#Example 2:
#Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
#Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
#
#Constraints:
#    0 <= synonyms.length <= 10
#    synonyms[i].length == 2
#    1 <= si.length, ti.length <= 10
#    si != ti
#    text consists of at most 10 words.
#    All the pairs of synonyms are unique.
#    The words of text are separated by single spaces.

from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        """
        Union-Find to group synonyms.
        Generate all combinations.
        """
        uf = UnionFind()

        # Union synonyms
        for s, t in synonyms:
            uf.union(s, t)

        # Group words by root
        groups = defaultdict(set)
        for s, t in synonyms:
            root = uf.find(s)
            groups[root].add(s)
            groups[root].add(t)

        # Generate sentences
        words = text.split()
        result = []

        def backtrack(idx, current):
            if idx == len(words):
                result.append(' '.join(current))
                return

            word = words[idx]
            root = uf.find(word)

            if root in groups and word in groups[root]:
                # Word has synonyms
                for syn in sorted(groups[root]):
                    backtrack(idx + 1, current + [syn])
            else:
                # Word has no synonyms
                backtrack(idx + 1, current + [word])

        backtrack(0, [])
        return sorted(result)


class SolutionDFS:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        """Using DFS to build synonym groups"""
        # Build graph
        graph = defaultdict(set)
        for s, t in synonyms:
            graph[s].add(t)
            graph[t].add(s)

        # Find connected components using DFS
        def get_synonyms(word):
            if word not in graph:
                return [word]

            visited = set()
            stack = [word]
            synonyms = []

            while stack:
                w = stack.pop()
                if w not in visited:
                    visited.add(w)
                    synonyms.append(w)
                    for neighbor in graph[w]:
                        if neighbor not in visited:
                            stack.append(neighbor)

            return sorted(synonyms)

        # Generate sentences
        words = text.split()
        result = [[]]

        for word in words:
            syns = get_synonyms(word)
            new_result = []
            for sentence in result:
                for syn in syns:
                    new_result.append(sentence + [syn])
            result = new_result

        return sorted(' '.join(s) for s in result)
