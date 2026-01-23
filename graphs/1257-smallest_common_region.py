#1257. Smallest Common Region
#Medium
#
#You are given some lists of regions where the first region of each list
#includes all other regions in that list.
#
#Naturally, if a region x contains another region y then x is bigger than y.
#Also, by definition, a region x contains itself.
#
#Given two regions: region1 and region2, return the smallest region that
#contains both of them.
#
#If you are given regions r1, r2, and r3 such that r1 includes r3, it is
#guaranteed there is no r2 such that r2 includes r3.
#
#It is guaranteed the smallest region exists.
#
#Example 1:
#Input:
#regions = [["Earth","North America","South America"],
#           ["North America","United States","Canada"],
#           ["United States","New York","Boston"],
#           ["Canada","Ontario","Quebec"],
#           ["South America","Brazil"]],
#region1 = "Quebec",
#region2 = "New York"
#Output: "North America"
#
#Example 2:
#Input:
#regions = [["Earth", "North America", "South America"],
#           ["North America", "United States", "Canada"],
#           ["United States", "New York", "Boston"],
#           ["Canada", "Ontario", "Quebec"],
#           ["South America", "Brazil"]],
#region1 = "Canada",
#region2 = "South America"
#Output: "Earth"
#
#Constraints:
#    2 <= regions.length <= 10^4
#    2 <= regions[i].length <= 20
#    1 <= regions[i][j].length, region1.length, region2.length <= 20
#    region1 != region2
#    regions[i][j], region1, and region2 consist of English letters.

from typing import List

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        """
        Build parent map, then find LCA (Lowest Common Ancestor).
        """
        # Build child -> parent map
        parent = {}
        for region_list in regions:
            parent_region = region_list[0]
            for child in region_list[1:]:
                parent[child] = parent_region

        # Get ancestors of region1
        ancestors1 = set()
        curr = region1
        while curr:
            ancestors1.add(curr)
            curr = parent.get(curr)

        # Find first ancestor of region2 that's also in ancestors1
        curr = region2
        while curr:
            if curr in ancestors1:
                return curr
            curr = parent.get(curr)

        return ""  # Shouldn't reach here if input is valid


class SolutionPathIntersection:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        """Build paths and find intersection"""
        parent = {}
        for region_list in regions:
            for child in region_list[1:]:
                parent[child] = region_list[0]

        # Build path from region1 to root
        path1 = []
        curr = region1
        while curr:
            path1.append(curr)
            curr = parent.get(curr)

        # Build path from region2 to root
        path2 = set()
        curr = region2
        while curr:
            path2.add(curr)
            curr = parent.get(curr)

        # Find first node in path1 that's in path2
        for region in path1:
            if region in path2:
                return region

        return ""
