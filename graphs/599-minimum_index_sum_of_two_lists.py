#599. Minimum Index Sum of Two Lists
#Easy
#
#Given two arrays of strings list1 and list2, find the common strings with the
#least index sum.
#
#A common string is a string that appeared in both list1 and list2.
#
#A common string with the least index sum is a common string such that if it
#appeared at list1[i] and list2[j] then i + j should be the minimum value among
#all the other common strings.
#
#Return all the common strings with the least index sum. Return the answer in any order.
#
#Example 1:
#Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
#       list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
#Output: ["Shogun"]
#
#Example 2:
#Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
#       list2 = ["KFC","Shogun","Burger King"]
#Output: ["Shogun"]
#
#Example 3:
#Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
#Output: ["sad","happy"]
#
#Constraints:
#    1 <= list1.length, list2.length <= 1000
#    1 <= list1[i].length, list2[i].length <= 30
#    list1[i] and list2[i] consist of spaces ' ' and English letters.
#    All the strings of list1 are unique.
#    All the strings of list2 are unique.
#    There is at least one common string between list1 and list2.

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """Hash map for index lookup"""
        index1 = {s: i for i, s in enumerate(list1)}

        min_sum = float('inf')
        result = []

        for j, s in enumerate(list2):
            if s in index1:
                idx_sum = index1[s] + j

                if idx_sum < min_sum:
                    min_sum = idx_sum
                    result = [s]
                elif idx_sum == min_sum:
                    result.append(s)

        return result


class SolutionTwoMaps:
    """Using two hash maps"""

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {s: i for i, s in enumerate(list1)}
        index2 = {s: i for i, s in enumerate(list2)}

        # Find common strings
        common = set(list1) & set(list2)

        # Calculate index sums
        sums = {s: index1[s] + index2[s] for s in common}

        min_sum = min(sums.values())

        return [s for s, total in sums.items() if total == min_sum]
