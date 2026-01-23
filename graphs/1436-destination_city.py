#1436. Destination City
#Easy
#
#You are given the array paths, where paths[i] = [cityAi, cityBi] means there
#exists a direct path going from cityAi to cityBi. Return the destination city,
#that is, the city without any path outgoing to another city.
#
#It is guaranteed that the graph of paths forms a line without any loop,
#therefore, there will be exactly one destination city.
#
#Example 1:
#Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
#Output: "Sao Paulo"
#Explanation: Starting at "London" city you will reach "Sao Paulo" city which
#is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
#
#Example 2:
#Input: paths = [["B","C"],["D","B"],["C","A"]]
#Output: "A"
#Explanation: All possible trips are:
#"D" -> "B" -> "C" -> "A".
#"B" -> "C" -> "A".
#"C" -> "A".
#"A".
#Clearly the destination city is "A".
#
#Example 3:
#Input: paths = [["A","Z"]]
#Output: "Z"
#
#Constraints:
#    1 <= paths.length <= 100
#    paths[i].length == 2
#    1 <= cityAi.length, cityBi.length <= 10
#    cityAi != cityBi
#    All strings consist of lowercase and uppercase English letters and the space character.

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        Destination city is the one that only appears as a destination,
        not as a source.
        """
        sources = {path[0] for path in paths}

        for path in paths:
            if path[1] not in sources:
                return path[1]

        return ""


class SolutionAllCities:
    def destCity(self, paths: List[List[str]]) -> str:
        """Find city that's in destinations but not in sources"""
        sources = set()
        destinations = set()

        for src, dst in paths:
            sources.add(src)
            destinations.add(dst)

        # Destination city is in destinations but not in sources
        result = destinations - sources
        return result.pop()


class SolutionMap:
    def destCity(self, paths: List[List[str]]) -> str:
        """Build adjacency and find city with no outgoing edges"""
        outgoing = {}

        for src, dst in paths:
            outgoing[src] = dst
            if dst not in outgoing:
                outgoing[dst] = None

        for city, next_city in outgoing.items():
            if next_city is None:
                return city

        return ""


class SolutionOneLiner:
    def destCity(self, paths: List[List[str]]) -> str:
        """Pythonic one-liner"""
        sources = {p[0] for p in paths}
        return next(p[1] for p in paths if p[1] not in sources)
