#1996. The Number of Weak Characters in the Game
#Medium
#
#You are playing a game that contains multiple characters, and each of the
#characters has two main properties: attack and defense. You are given a 2D
#integer array properties where properties[i] = [attacki, defensei] represents
#the properties of the ith character in the game.
#
#A character is said to be weak if any other character has both attack and
#defense levels strictly greater than this character's attack and defense
#levels. More formally, a character i is said to be weak if there exists another
#character j where attackj > attacki and defensej > defensei.
#
#Return the number of weak characters.
#
#Example 1:
#Input: properties = [[5,5],[6,3],[3,6]]
#Output: 0
#
#Example 2:
#Input: properties = [[2,2],[3,3]]
#Output: 1
#
#Example 3:
#Input: properties = [[1,5],[10,4],[4,3]]
#Output: 1
#
#Constraints:
#    2 <= properties.length <= 10^5
#    properties[i].length == 2
#    1 <= attacki, defensei <= 10^5

from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        Sort by attack descending, defense ascending.
        Track max defense seen; character is weak if defense < max.
        """
        # Sort: highest attack first, then lowest defense first (for same attack)
        properties.sort(key=lambda x: (-x[0], x[1]))

        max_defense = 0
        weak_count = 0

        for attack, defense in properties:
            if defense < max_defense:
                weak_count += 1
            else:
                max_defense = defense

        return weak_count


class SolutionExplained:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        Detailed explanation:

        Key insight: Sort by attack descending, and for same attack,
        by defense ascending.

        Why defense ascending for same attack?
        - Characters with same attack can't make each other weak
        - Processing lower defense first prevents false positives

        Then scan: if current defense < max_defense_seen, it's weak.
        The max_defense came from a character with higher attack.
        """
        # Sort: -attack (descending), defense (ascending)
        properties.sort(key=lambda x: (-x[0], x[1]))

        max_def = 0
        weak = 0

        for atk, def_ in properties:
            # All previous characters have attack >= current attack
            # Due to sorting, if defense < max, there exists one with
            # strictly greater attack and defense
            if def_ < max_def:
                weak += 1
            max_def = max(max_def, def_)

        return weak


class SolutionBuckets:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        Bucket approach: group by attack level.
        """
        max_attack = max(p[0] for p in properties)

        # max_defense[i] = max defense among characters with attack > i
        max_defense_after = [0] * (max_attack + 2)

        # Group by attack
        attack_to_defense = {}
        for atk, def_ in properties:
            if atk not in attack_to_defense:
                attack_to_defense[atk] = []
            attack_to_defense[atk].append(def_)

        # Build suffix max of defense
        suffix_max = 0
        for atk in range(max_attack, 0, -1):
            max_defense_after[atk] = suffix_max
            if atk in attack_to_defense:
                suffix_max = max(suffix_max, max(attack_to_defense[atk]))

        # Count weak characters
        weak = 0
        for atk, def_ in properties:
            if def_ < max_defense_after[atk]:
                weak += 1

        return weak
