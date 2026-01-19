#332. Reconstruct Itinerary
#Hard
#
#You are given a list of airline tickets where tickets[i] = [fromi, toi]
#represent the departure and the arrival airports of one flight. Reconstruct
#the itinerary in order and return it.
#
#All of the tickets belong to a man who departs from "JFK", thus, the itinerary
#must begin with "JFK". If there are multiple valid itineraries, you should
#return the itinerary that has the smallest lexical order when read as a single
#string.
#
#You may assume all tickets form at least one valid itinerary. You must use all
#the tickets once and only once.
#
#Example 1:
#Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
#Output: ["JFK","MUC","LHR","SFO","SJC"]
#
#Example 2:
#Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],
#                  ["ATL","SFO"]]
#Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
#Explanation: Another possible reconstruction is
#["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
#
#Constraints:
#    1 <= tickets.length <= 300
#    tickets[i].length == 2
#    fromi.length == 3
#    toi.length == 3
#    fromi and toi consist of uppercase English letters.
#    fromi != toi

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Hierholzer's algorithm for Eulerian path.
        Use min-heap to get lexically smallest destination.
        """
        graph = defaultdict(list)

        # Build graph with destinations in a min-heap
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            route.append(airport)

        dfs("JFK")

        return route[::-1]


class SolutionIterative:
    """Iterative version using stack"""

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        stack = ["JFK"]
        route = []

        while stack:
            while graph[stack[-1]]:
                next_airport = heapq.heappop(graph[stack[-1]])
                stack.append(next_airport)
            route.append(stack.pop())

        return route[::-1]


class SolutionBacktrack:
    """Backtracking approach"""

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Sort destinations for each source
        for src, dst in sorted(tickets):
            graph[src].append(dst)

        route = ["JFK"]
        target_length = len(tickets) + 1

        def backtrack():
            if len(route) == target_length:
                return True

            current = route[-1]
            destinations = graph[current]

            for i in range(len(destinations)):
                dst = destinations[i]
                destinations.pop(i)
                route.append(dst)

                if backtrack():
                    return True

                route.pop()
                destinations.insert(i, dst)

            return False

        backtrack()
        return route
