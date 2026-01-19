#269. Alien Dictionary
#Hard
#
#There is a new alien language that uses the English alphabet. However, the order
#of the letters is unknown to you.
#
#You are given a list of strings words from the alien language's dictionary. The
#strings in words are sorted lexicographically by the rules of this new language.
#
#Return a string of the unique letters in the new alien language sorted in
#lexicographically increasing order by the new language's rules. If there is no
#solution, return "". If there are multiple solutions, return any of them.
#
#Example 1:
#Input: words = ["wrt","wrf","er","ett","rftt"]
#Output: "wertf"
#
#Example 2:
#Input: words = ["z","x"]
#Output: "zx"
#
#Example 3:
#Input: words = ["z","x","z"]
#Output: ""
#Explanation: The order is invalid, so return "".
#
#Constraints:
#    1 <= words.length <= 100
#    1 <= words[i].length <= 100
#    words[i] consists of only lowercase English letters.

from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Build graph using topological sort
        # Node = character, Edge a->b means a comes before b

        # Get all unique characters
        chars = set()
        for word in words:
            chars.update(word)

        # Build adjacency list and in-degree count
        adj = defaultdict(set)
        in_degree = {c: 0 for c in chars}

        # Compare adjacent words to find ordering relationships
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            # Check for invalid case: prefix comes after longer word
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""

            # Find first different character
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    break

        # Topological sort using BFS (Kahn's algorithm)
        queue = deque([c for c in chars if in_degree[c] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check for cycle
        if len(result) != len(chars):
            return ""

        return "".join(result)

    # DFS approach with cycle detection
    def alienOrderDFS(self, words: List[str]) -> str:
        chars = set()
        for word in words:
            chars.update(word)

        adj = defaultdict(set)

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""

            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    adj[c1].add(c2)
                    break

        # DFS with states: 0=unvisited, 1=visiting, 2=visited
        state = {c: 0 for c in chars}
        result = []

        def dfs(char):
            if state[char] == 1:  # Cycle detected
                return False
            if state[char] == 2:  # Already processed
                return True

            state[char] = 1
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False

            state[char] = 2
            result.append(char)
            return True

        for char in chars:
            if not dfs(char):
                return ""

        return "".join(reversed(result))
