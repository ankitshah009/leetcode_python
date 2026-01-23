#737. Sentence Similarity II
#Medium
#
#We can represent a sentence as an array of words, for example, the sentence
#"I am happy with leetcode" can be represented as arr = ["I","am","happy",
#"with","leetcode"].
#
#Given two sentences sentence1 and sentence2 each represented as a string array
#and given an array of string pairs similarPairs where similarPairs[i] =
#[xi, yi] indicates that the two words xi and yi are similar.
#
#Return true if sentence1 and sentence2 are similar, or false if they are not.
#
#Two sentences are similar if:
#- They have the same length
#- sentence1[i] and sentence2[i] are similar.
#
#Notice that a word is always similar to itself, also notice that the similarity
#relation is transitive. For example, if the words a and b are similar, and the
#words b and c are similar, then a and c are similar.
#
#Example 1:
#Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama",
#"talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
#Output: true
#Explanation: The two sentences have the same length and each word i is similar.
#
#Example 2:
#Input: sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","oneeli"],
#similarPairs = [["leetcode","code"],["oneeli","code"]]
#Output: true
#
#Constraints:
#    1 <= sentence1.length, sentence2.length <= 1000
#    1 <= sentence1[i].length, sentence2[i].length <= 20
#    sentence1[i] and sentence2[i] consist of lower-case and upper-case English letters.
#    0 <= similarPairs.length <= 2000
#    similarPairs[i].length == 2

class Solution:
    def areSentencesSimilarTwo(self, sentence1: list[str], sentence2: list[str],
                               similarPairs: list[list[str]]) -> bool:
        """
        Union-Find for transitive similarity.
        """
        if len(sentence1) != len(sentence2):
            return False

        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Build union-find
        for w1, w2 in similarPairs:
            union(w1, w2)

        # Check sentences
        for w1, w2 in zip(sentence1, sentence2):
            if find(w1) != find(w2):
                return False

        return True


class SolutionDFS:
    """DFS-based connectivity check"""

    def areSentencesSimilarTwo(self, sentence1: list[str], sentence2: list[str],
                               similarPairs: list[list[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        from collections import defaultdict

        # Build graph
        graph = defaultdict(set)
        for w1, w2 in similarPairs:
            graph[w1].add(w2)
            graph[w2].add(w1)

        def connected(w1, w2, visited):
            if w1 == w2:
                return True
            visited.add(w1)
            for neighbor in graph[w1]:
                if neighbor not in visited:
                    if connected(neighbor, w2, visited):
                        return True
            return False

        for w1, w2 in zip(sentence1, sentence2):
            if not connected(w1, w2, set()):
                return False

        return True


class SolutionBFS:
    """BFS-based connectivity check"""

    def areSentencesSimilarTwo(self, sentence1: list[str], sentence2: list[str],
                               similarPairs: list[list[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        from collections import defaultdict, deque

        graph = defaultdict(set)
        for w1, w2 in similarPairs:
            graph[w1].add(w2)
            graph[w2].add(w1)

        def connected(start, target):
            if start == target:
                return True

            visited = {start}
            queue = deque([start])

            while queue:
                word = queue.popleft()
                if word == target:
                    return True

                for neighbor in graph[word]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return False

        return all(connected(w1, w2) for w1, w2 in zip(sentence1, sentence2))
