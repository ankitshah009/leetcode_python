#781. Rabbits in Forest
#Medium
#
#There is a forest with an unknown number of rabbits. We asked n rabbits "How
#many rabbits have the same color as you?" and collected the answers in an
#integer array answers where answers[i] is the answer of the ith rabbit.
#
#Given the array answers, return the minimum number of rabbits that could be
#in the forest.
#
#Example 1:
#Input: answers = [1,1,2]
#Output: 5
#Explanation: The two rabbits that answered "1" could both be the same color,
#say red. The rabbit that answered "2" can't be red or the answers would be
#inconsistent. Say the rabbit that answered "2" was blue. Then there should be
#2 other blue rabbits in the forest that didn't answer into the array.
#The smallest possible number of rabbits in the forest is 5: 3 red, 2 blue.
#
#Example 2:
#Input: answers = [10,10,10]
#Output: 11
#
#Constraints:
#    1 <= answers.length <= 1000
#    0 <= answers[i] < 1000

from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        """
        Group by answer. If k rabbits say "x", they need ceil(k/(x+1)) groups.
        """
        count = Counter(answers)
        total = 0

        for ans, cnt in count.items():
            group_size = ans + 1
            num_groups = math.ceil(cnt / group_size)
            total += num_groups * group_size

        return total


class SolutionFormula:
    """Using integer arithmetic for ceiling division"""

    def numRabbits(self, answers: list[int]) -> int:
        count = Counter(answers)
        total = 0

        for ans, cnt in count.items():
            group_size = ans + 1
            # Number of complete groups needed
            num_groups = (cnt + group_size - 1) // group_size
            total += num_groups * group_size

        return total
