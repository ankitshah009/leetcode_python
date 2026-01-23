#839. Similar String Groups
#Hard
#
#Two strings, X and Y, are considered similar if either they are identical or
#we can make them equivalent by swapping at most two letters (in distinct
#positions) within the string X.
#
#For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and
#"rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
#
#Together, these form two connected groups by similarity: {"tars", "rats", "arts"}
#and {"star"}. Notice that "tars" and "arts" are in the same group even though
#they are not similar. Formally, each group is such that a word is in the group
#if and only if it is similar to at least one other word in the group.
#
#We are given a list strs of strings where every string in strs is an anagram
#of every other string in strs. How many groups are there?
#
#Example 1:
#Input: strs = ["tars","rats","arts","star"]
#Output: 2
#
#Example 2:
#Input: strs = ["omv","ovm"]
#Output: 1
#
#Constraints:
#    1 <= strs.length <= 300
#    1 <= strs[i].length <= 300
#    strs[i] consists of lowercase letters only.
#    All words in strs have the same length and are anagrams of each other.

class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        """
        Union-Find: union similar strings.
        """
        n = len(strs)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        def is_similar(s1, s2):
            """Check if s1 and s2 differ by at most 2 positions"""
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    union(i, j)

        # Count unique roots
        return len(set(find(i) for i in range(n)))


class SolutionDFS:
    """DFS to find connected components"""

    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        visited = [False] * n

        def is_similar(s1, s2):
            diff = sum(c1 != c2 for c1, c2 in zip(s1, s2))
            return diff <= 2

        def dfs(i):
            visited[i] = True
            for j in range(n):
                if not visited[j] and is_similar(strs[i], strs[j]):
                    dfs(j)

        groups = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                groups += 1

        return groups


class SolutionBFS:
    """BFS to find connected components"""

    def numSimilarGroups(self, strs: list[str]) -> int:
        from collections import deque

        n = len(strs)
        visited = [False] * n

        def is_similar(s1, s2):
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        groups = 0

        for start in range(n):
            if visited[start]:
                continue

            groups += 1
            queue = deque([start])
            visited[start] = True

            while queue:
                i = queue.popleft()
                for j in range(n):
                    if not visited[j] and is_similar(strs[i], strs[j]):
                        visited[j] = True
                        queue.append(j)

        return groups
