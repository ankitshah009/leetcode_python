#1282. Group the People Given the Group Size They Belong To
#Medium
#
#There are n people that are split into some unknown number of groups. Each
#person is labeled with a unique ID from 0 to n - 1.
#
#You are given an integer array groupSizes, where groupSizes[i] is the size of
#the group that person i is in. For example, if groupSizes[1] = 3, then person
#1 must be in a group of size 3.
#
#Return a list of groups such that each person i is in a group of size groupSizes[i].
#
#Each person should appear in exactly one group, and every person must be in a
#group. If there are multiple answers, return any of them. It is guaranteed
#that there will be at least one valid solution for the given input.
#
#Example 1:
#Input: groupSizes = [3,3,3,3,3,1,3]
#Output: [[5],[0,1,2],[3,4,6]]
#Explanation:
#The first group is [5]. The size is 1, and groupSizes[5] = 1.
#The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
#The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
#
#Example 2:
#Input: groupSizes = [2,1,3,3,3,2]
#Output: [[1],[0,5],[2,3,4]]
#
#Constraints:
#    groupSizes.length == n
#    1 <= n <= 500
#    1 <= groupSizes[i] <= n

from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        Group people by their group size.
        When a group reaches its target size, add to result.
        """
        groups = defaultdict(list)  # size -> list of people
        result = []

        for person, size in enumerate(groupSizes):
            groups[size].append(person)

            # When group is full, add to result and start new group
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result


class SolutionExplicit:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """More explicit approach"""
        # Group people by size
        by_size = defaultdict(list)
        for i, size in enumerate(groupSizes):
            by_size[size].append(i)

        # Split each size group into proper-sized groups
        result = []
        for size, people in by_size.items():
            for i in range(0, len(people), size):
                result.append(people[i:i + size])

        return result
