#815. Bus Routes
#Hard
#
#You are given an array routes representing bus routes where routes[i] is a bus
#route that the ith bus repeats forever.
#
#For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in
#the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> ... forever.
#
#You will start at the bus stop source (You are not on any bus initially), and
#you want to go to the bus stop target. You can travel between bus stops by buses only.
#
#Return the least number of buses you must take to travel from source to target.
#Return -1 if it is not possible.
#
#Example 1:
#Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
#Output: 2
#Explanation: The best strategy is take the first bus to stop 7, then take the
#second bus to stop 6.
#
#Example 2:
#Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
#Output: -1
#
#Constraints:
#    1 <= routes.length <= 500.
#    1 <= routes[i].length <= 10^5
#    All the values of routes[i] are unique.
#    sum(routes[i].length) <= 10^5
#    0 <= routes[i][j] < 10^6
#    0 <= source, target < 10^6

from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        """
        BFS on bus routes (not stops).
        """
        if source == target:
            return 0

        # Map each stop to list of routes that contain it
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        # BFS: state is the set of routes we've taken
        visited_routes = set()
        visited_stops = set([source])
        queue = deque([(source, 0)])  # (stop, num_buses)

        while queue:
            stop, buses = queue.popleft()

            for route_idx in stop_to_routes[stop]:
                if route_idx in visited_routes:
                    continue

                visited_routes.add(route_idx)

                for next_stop in routes[route_idx]:
                    if next_stop == target:
                        return buses + 1

                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))

        return -1


class SolutionRouteBFS:
    """BFS on routes directly"""

    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        n = len(routes)
        routes = [set(route) for route in routes]

        # Build graph of routes that share stops
        graph = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                if routes[i] & routes[j]:
                    graph[i].add(j)
                    graph[j].add(i)

        # Find start and end routes
        start_routes = {i for i in range(n) if source in routes[i]}
        end_routes = {i for i in range(n) if target in routes[i]}

        # BFS
        visited = set()
        queue = deque((r, 1) for r in start_routes)
        visited.update(start_routes)

        while queue:
            route, buses = queue.popleft()

            if route in end_routes:
                return buses

            for next_route in graph[route]:
                if next_route not in visited:
                    visited.add(next_route)
                    queue.append((next_route, buses + 1))

        return -1
