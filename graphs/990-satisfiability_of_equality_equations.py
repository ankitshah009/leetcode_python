#990. Satisfiability of Equality Equations
#Medium
#
#You are given an array of strings equations that represent relationships
#between variables where each string equations[i] is of length 4 and takes one
#of two different forms: "xi==xj" or "xi!=xj".
#
#Return true if it is possible to assign integers to variable names so as to
#satisfy all the given equations, or false otherwise.
#
#Example 1:
#Input: equations = ["a==b","b!=a"]
#Output: false
#
#Example 2:
#Input: equations = ["b==a","a==b"]
#Output: true
#
#Constraints:
#    1 <= equations.length <= 500
#    equations[i].length == 4
#    equations[i][0] is a lowercase letter.
#    equations[i][1] is either '=' or '!'.
#    equations[i][2] is either '=' or '!'.
#    equations[i][3] is a lowercase letter.

class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        """
        Union-Find: first process ==, then check !=.
        """
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        def char_to_idx(c):
            return ord(c) - ord('a')

        # First pass: process equalities
        for eq in equations:
            if eq[1] == '=':
                x = char_to_idx(eq[0])
                y = char_to_idx(eq[3])
                union(x, y)

        # Second pass: check inequalities
        for eq in equations:
            if eq[1] == '!':
                x = char_to_idx(eq[0])
                y = char_to_idx(eq[3])
                if find(x) == find(y):
                    return False

        return True


class SolutionDFS:
    """DFS on graph"""

    def equationsPossible(self, equations: list[str]) -> bool:
        from collections import defaultdict

        # Build graph from equalities
        graph = defaultdict(set)

        for eq in equations:
            if eq[1] == '=':
                x, y = eq[0], eq[3]
                graph[x].add(y)
                graph[y].add(x)

        # Find connected components
        component = {}
        comp_id = 0

        def dfs(node, cid):
            component[node] = cid
            for neighbor in graph[node]:
                if neighbor not in component:
                    dfs(neighbor, cid)

        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in graph and c not in component:
                dfs(c, comp_id)
                comp_id += 1

        # Check inequalities
        for eq in equations:
            if eq[1] == '!':
                x, y = eq[0], eq[3]
                if x == y:
                    return False
                if x in component and y in component:
                    if component[x] == component[y]:
                        return False

        return True
