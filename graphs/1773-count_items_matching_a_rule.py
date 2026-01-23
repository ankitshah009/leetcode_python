#1773. Count Items Matching a Rule
#Easy
#
#You are given an array items, where each items[i] = [typei, colori, namei]
#describes the type, color, and name of the ith item. You are also given a rule
#represented by two strings, ruleKey and ruleValue.
#
#The ith item is said to match the rule if one of the following is true:
#- ruleKey == "type" and ruleValue == typei.
#- ruleKey == "color" and ruleValue == colori.
#- ruleKey == "name" and ruleValue == namei.
#
#Return the number of items that match the given rule.
#
#Example 1:
#Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
#Output: 1
#
#Example 2:
#Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
#Output: 2
#
#Constraints:
#    1 <= items.length <= 10^4
#    1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
#    ruleKey is equal to either "type", "color", or "name".
#    All strings consist only of lowercase letters.

from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        Map rule key to index and count matches.
        """
        key_to_index = {"type": 0, "color": 1, "name": 2}
        idx = key_to_index[ruleKey]

        return sum(1 for item in items if item[idx] == ruleValue)


class SolutionExplicit:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        Explicit index determination.
        """
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else:
            idx = 2

        count = 0
        for item in items:
            if item[idx] == ruleValue:
                count += 1

        return count


class SolutionDict:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        Using dict comprehension.
        """
        return sum(
            1 for t, c, n in items
            if {"type": t, "color": c, "name": n}[ruleKey] == ruleValue
        )
