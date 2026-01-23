#851. Loud and Rich
#Medium
#
#There is a group of n people labeled from 0 to n - 1 where each person has a
#different amount of money and a different level of quietness.
#
#You are given an array richer where richer[i] = [ai, bi] indicates that ai has
#more money than bi and an integer array quiet where quiet[i] is the quietness
#of the ith person.
#
#Return an integer array answer where answer[x] = y if y is the least quiet
#person (that is, the person y with the smallest value of quiet[y]) among all
#people who definitely have equal to or more money than the person x.
#
#Example 1:
#Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
#Output: [5,5,2,5,4,5,6,7]
#
#Example 2:
#Input: richer = [], quiet = [0]
#Output: [0]
#
#Constraints:
#    n == quiet.length
#    1 <= n <= 500
#    0 <= quiet[i] < n
#    All the values of quiet are unique.
#    0 <= richer.length <= n * (n - 1) / 2
#    0 <= ai, bi < n
#    ai != bi
#    All the pairs of richer are unique.
#    The observations are all logically consistent.

from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        """
        DFS with memoization: for each person, find quietest among richer people.
        """
        n = len(quiet)

        # Build graph: richer[i] -> list of people richer than i
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)  # a is richer than b

        answer = [-1] * n

        def dfs(person):
            if answer[person] != -1:
                return answer[person]

            answer[person] = person  # Start with self

            for richer_person in graph[person]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[answer[person]]:
                    answer[person] = candidate

            return answer[person]

        for i in range(n):
            dfs(i)

        return answer


class SolutionTopological:
    """Topological sort approach"""

    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        from collections import deque

        n = len(quiet)

        # Build graph and in-degree
        graph = defaultdict(list)
        in_degree = [0] * n

        for a, b in richer:
            graph[a].append(b)  # Propagate from a to b
            in_degree[b] += 1

        # Initialize answer with self
        answer = list(range(n))

        # Start with richest people (in_degree = 0)
        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            person = queue.popleft()

            for poorer in graph[person]:
                # Update if person's answer is quieter
                if quiet[answer[person]] < quiet[answer[poorer]]:
                    answer[poorer] = answer[person]

                in_degree[poorer] -= 1
                if in_degree[poorer] == 0:
                    queue.append(poorer)

        return answer
