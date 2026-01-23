#1203. Sort Items by Groups Respecting Dependencies
#Hard
#
#There are n items each belonging to zero or one of m groups where group[i] is
#the group that the i-th item belongs to and it's equal to -1 if the i-th item
#belongs to no group. The items and the groups are zero indexed. A group can
#have no item belonging to it.
#
#Return a sorted list of the items such that:
#    The items that belong to the same group are next to each other in the
#    sorted list.
#    There are some relations between these items where beforeItems[i] is a
#    list containing all the items that should come before the i-th item in
#    the sorted array (to the left of the i-th item).
#
#Return any solution if there is more than one solution and return an empty
#list if there is no solution.
#
#Example 1:
#Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
#Output: [6,3,4,1,5,2,0,7]
#
#Example 2:
#Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
#Output: []
#Explanation: This is the same as example 1 except that 4 needs to be before 6.
#
#Constraints:
#    1 <= m <= n <= 3 * 10^4
#    group.length == beforeItems.length == n
#    -1 <= group[i] <= m - 1
#    0 <= beforeItems[i].length <= n - 1
#    0 <= beforeItems[i][j] <= n - 1
#    i != beforeItems[i][j]
#    beforeItems[i] does not contain duplicates elements.

from typing import List
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """
        Two-level topological sort:
        1. Sort items within each group
        2. Sort groups relative to each other

        Assign unique group IDs to items with group = -1.
        """
        # Assign unique groups to items with no group
        next_group = m
        for i in range(n):
            if group[i] == -1:
                group[i] = next_group
                next_group += 1

        total_groups = next_group

        # Build graphs
        # Item graph: edges between items
        item_graph = defaultdict(list)
        item_indegree = [0] * n

        # Group graph: edges between groups
        group_graph = defaultdict(list)
        group_indegree = [0] * total_groups

        for i in range(n):
            for before in beforeItems[i]:
                # Item dependency
                item_graph[before].append(i)
                item_indegree[i] += 1

                # Group dependency (if different groups)
                if group[before] != group[i]:
                    group_graph[group[before]].append(group[i])
                    group_indegree[group[i]] += 1

        def topo_sort(graph, indegree, nodes):
            """Topological sort for given nodes"""
            queue = deque([node for node in nodes if indegree[node] == 0])
            result = []

            while queue:
                node = queue.popleft()
                result.append(node)
                for neighbor in graph[node]:
                    if neighbor in nodes:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            queue.append(neighbor)

            return result if len(result) == len(nodes) else []

        # Group items by their group
        group_items = defaultdict(list)
        for i in range(n):
            group_items[group[i]].append(i)

        # Sort items within each group
        sorted_group_items = {}
        for g in range(total_groups):
            items = group_items[g]
            if items:
                sorted_items = topo_sort(item_graph, item_indegree[:], set(items))
                if len(sorted_items) != len(items):
                    return []
                sorted_group_items[g] = sorted_items

        # Sort groups
        all_groups = set(range(total_groups))
        sorted_groups = topo_sort(group_graph, group_indegree, all_groups)
        if len(sorted_groups) != total_groups:
            return []

        # Build final result
        result = []
        for g in sorted_groups:
            if g in sorted_group_items:
                result.extend(sorted_group_items[g])

        return result
